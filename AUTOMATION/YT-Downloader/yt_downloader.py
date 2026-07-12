import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
import yt_dlp

# ---------- Theme ----------
BG        = "#0d1b1e"
CARD_BG   = "#132a2e"
ACCENT    = "#14e0c4"
GOLD      = "#e8c07d"
TEXT      = "#e8f6f4"
SUBTEXT   = "#7fa8a3"
ENTRY_BG  = "#0f2226"
RED       = "#ff6b6b"

# Quality label -> yt-dlp format string
QUALITY_MAP = {
    "Best available":  "bestvideo+bestaudio/best",
    "4K (2160p)":      "bestvideo[height<=2160]+bestaudio/best[height<=2160]",
    "1440p (2K)":      "bestvideo[height<=1440]+bestaudio/best[height<=1440]",
    "1080p":           "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
    "720p":            "bestvideo[height<=720]+bestaudio/best[height<=720]",
    "480p":            "bestvideo[height<=480]+bestaudio/best[height<=480]",
    "360p":            "bestvideo[height<=360]+bestaudio/best[height<=360]",
    "Audio only (MP3)": "bestaudio/best",
}


class YTDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("StreamGrab // YT Downloader")
        self.geometry("580x680")
        self.configure(bg=BG)
        self.resizable(False, False)

        self.output_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        self.quality = tk.StringVar(value="Best available")

        # pause_event.set() = running, .clear() = paused.
        # yt-dlp has no native pause/resume, so the progress hook blocks
        # on this event between chunk updates to simulate a pause.
        self.pause_event = threading.Event()
        self.pause_event.set()

        self._build_ui()

    # ---------- UI ----------
    def _build_ui(self):
        header = tk.Frame(self, bg=BG)
        header.pack(fill="x", pady=(26, 4), padx=30)
        tk.Label(header, text="STREAM", font=("Segoe UI", 22, "bold"),
                  fg=ACCENT, bg=BG).pack(side="left")
        tk.Label(header, text="GRAB", font=("Segoe UI", 22, "bold"),
                  fg=GOLD, bg=BG).pack(side="left")

        tk.Label(self, text="Paste a YouTube link, pick a quality, and go.",
                  font=("Segoe UI", 9), fg=SUBTEXT, bg=BG).pack(pady=(0, 16))

        card = tk.Frame(self, bg=CARD_BG, highlightbackground=ACCENT, highlightthickness=1)
        card.pack(fill="both", padx=30, pady=(0, 16))

        # URL
        tk.Label(card, text="VIDEO URL", font=("Segoe UI", 8, "bold"),
                 fg=SUBTEXT, bg=CARD_BG).pack(anchor="w", padx=20, pady=(18, 4))
        self.url_entry = tk.Entry(card, font=("Segoe UI", 11), bg=ENTRY_BG, fg=TEXT,
                                   insertbackground=ACCENT, relief="flat", bd=8)
        self.url_entry.pack(fill="x", padx=20, ipady=6)
        self.url_entry.insert(0, "https://youtu.be/...")
        self.url_entry.bind("<FocusIn>", self._clear_placeholder)

        # Save folder
        tk.Label(card, text="SAVE TO", font=("Segoe UI", 8, "bold"),
                 fg=SUBTEXT, bg=CARD_BG).pack(anchor="w", padx=20, pady=(14, 4))
        path_row = tk.Frame(card, bg=CARD_BG)
        path_row.pack(fill="x", padx=20)
        self.path_label = tk.Label(path_row, text=self._short_path(self.output_dir),
                                    font=("Segoe UI", 9), fg=TEXT, bg=ENTRY_BG, anchor="w")
        self.path_label.pack(side="left", fill="x", expand=True, ipady=7, ipadx=8)
        tk.Button(path_row, text="Browse", font=("Segoe UI", 9, "bold"), bg=GOLD,
                  fg="#1a1a1a", relief="flat", cursor="hand2",
                  command=self._choose_folder).pack(side="left", padx=(8, 0), ipady=6, ipadx=10)

        # Quality dropdown
        tk.Label(card, text="QUALITY", font=("Segoe UI", 8, "bold"),
                 fg=SUBTEXT, bg=CARD_BG).pack(anchor="w", padx=20, pady=(14, 4))

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Cool.TCombobox", fieldbackground=ENTRY_BG, background=ENTRY_BG,
                         foreground=TEXT, arrowcolor=ACCENT, bordercolor=ACCENT)
        self.quality_box = ttk.Combobox(
            card, textvariable=self.quality, values=list(QUALITY_MAP.keys()),
            state="readonly", style="Cool.TCombobox", font=("Segoe UI", 10)
        )
        self.quality_box.pack(fill="x", padx=20, ipady=4)

        # Buttons
        btn_row = tk.Frame(card, bg=CARD_BG)
        btn_row.pack(fill="x", padx=20, pady=(18, 20))

        self.download_btn = tk.Button(
            btn_row, text="⬇  DOWNLOAD", font=("Segoe UI", 12, "bold"), bg=ACCENT,
            fg="#06201c", relief="flat", cursor="hand2", activebackground="#5cf3e0",
            command=self._start_download
        )
        self.download_btn.pack(side="left", fill="x", expand=True, ipady=10)

        self.pause_btn = tk.Button(
            btn_row, text="⏸  PAUSE", font=("Segoe UI", 12, "bold"), bg="#3a3a3a",
            fg=SUBTEXT, relief="flat", cursor="hand2", state="disabled",
            command=self._toggle_pause
        )
        self.pause_btn.pack(side="left", ipady=10, ipadx=14, padx=(10, 0))

        # Progress bar
        style.configure("Cool.Horizontal.TProgressbar", troughcolor=ENTRY_BG,
                         background=ACCENT, bordercolor=ENTRY_BG,
                         lightcolor=ACCENT, darkcolor=ACCENT)
        self.progress = ttk.Progressbar(self, style="Cool.Horizontal.TProgressbar",
                                         orient="horizontal", length=520, mode="determinate")
        self.progress.pack(padx=30, pady=(0, 8))

        self.status_label = tk.Label(self, text="Waiting for a link...",
                                      font=("Segoe UI", 9), fg=SUBTEXT, bg=BG)
        self.status_label.pack(pady=(0, 14))

        # ---------- Real-time details panel ----------
        details_card = tk.Frame(self, bg=CARD_BG, highlightbackground=ACCENT, highlightthickness=1)
        details_card.pack(fill="both", padx=30, pady=(0, 20))

        tk.Label(details_card, text="DOWNLOAD DETAILS", font=("Segoe UI", 8, "bold"),
                 fg=SUBTEXT, bg=CARD_BG).pack(anchor="w", padx=20, pady=(16, 10))

        grid = tk.Frame(details_card, bg=CARD_BG)
        grid.pack(fill="x", padx=20, pady=(0, 18))

        self.detail_vars = {}
        fields = [
            ("title", "Title"), ("uploader", "Uploader"),
            ("duration", "Duration"), ("views", "Views"),
            ("resolution", "Resolution"), ("filesize", "Downloaded / Total"),
            ("speed", "Speed"), ("eta", "ETA"),
        ]
        for i, (key, label) in enumerate(fields):
            row, col = divmod(i, 2)
            cell = tk.Frame(grid, bg=CARD_BG)
            cell.grid(row=row, column=col, sticky="w", padx=(0, 30), pady=6)
            tk.Label(cell, text=label.upper(), font=("Segoe UI", 7, "bold"),
                     fg=SUBTEXT, bg=CARD_BG).pack(anchor="w")
            var = tk.StringVar(value="—")
            tk.Label(cell, textvariable=var, font=("Segoe UI", 10),
                     fg=GOLD if key == "title" else TEXT, bg=CARD_BG,
                     wraplength=230, justify="left").pack(anchor="w")
            self.detail_vars[key] = var

    # ---------- Helpers ----------
    def _clear_placeholder(self, event):
        if self.url_entry.get() == "https://youtu.be/...":
            self.url_entry.delete(0, tk.END)

    def _short_path(self, path):
        return path if len(path) < 42 else "..." + path[-39:]

    def _choose_folder(self):
        folder = filedialog.askdirectory(initialdir=self.output_dir)
        if folder:
            self.output_dir = folder
            self.path_label.config(text=self._short_path(folder))

    def _set_status(self, text, color=SUBTEXT):
        self.status_label.config(text=text, fg=color)

    def _set_detail(self, key, value):
        if key in self.detail_vars:
            self.detail_vars[key].set(value)

    def _reset_details(self):
        for var in self.detail_vars.values():
            var.set("—")

    @staticmethod
    def _fmt_duration(seconds):
        if not seconds:
            return "—"
        seconds = int(seconds)
        h, rem = divmod(seconds, 3600)
        m, s = divmod(rem, 60)
        return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"

    @staticmethod
    def _fmt_size(num_bytes):
        if not num_bytes:
            return "—"
        num_bytes = float(num_bytes)
        for unit in ["B", "KB", "MB", "GB"]:
            if num_bytes < 1024:
                return f"{num_bytes:.1f} {unit}"
            num_bytes /= 1024
        return f"{num_bytes:.1f} TB"

    # ---------- Pause control ----------
    def _toggle_pause(self):
        if self.pause_event.is_set():
            self.pause_event.clear()
            self.pause_btn.config(text="▶  RESUME", bg=GOLD, fg="#1a1a1a")
            self._set_status("Paused.", GOLD)
        else:
            self.pause_event.set()
            self.pause_btn.config(text="⏸  PAUSE", bg="#3a3a3a", fg=SUBTEXT)
            self._set_status("Resuming...", ACCENT)

    # ---------- Download logic ----------
    def _start_download(self):
        url = self.url_entry.get().strip()
        if not url or url == "https://youtu.be/...":
            messagebox.showwarning("Missing URL", "Paste a YouTube link first.")
            return

        self._reset_details()
        self.pause_event.set()

        self.download_btn.config(state="disabled", text="DOWNLOADING...")
        self.pause_btn.config(state="normal", text="⏸  PAUSE", bg="#3a3a3a", fg=SUBTEXT)
        self.quality_box.config(state="disabled")
        self.progress["value"] = 0
        self._set_status("Fetching video info...", GOLD)

        threading.Thread(target=self._download_video, args=(url,), daemon=True).start()

    def _progress_hook(self, d):
        # Blocks here while paused -- this pauses the actual download,
        # since yt-dlp streams chunks and calls this hook after each one.
        self.pause_event.wait()

        if d["status"] == "downloading":
            pct_str = d.get("_percent_str", "0%").strip().replace("%", "")
            try:
                pct = float(pct_str)
            except ValueError:
                pct = 0

            downloaded = d.get("downloaded_bytes", 0)
            total = d.get("total_bytes") or d.get("total_bytes_estimate", 0)
            speed = d.get("_speed_str", "N/A").strip()
            eta = d.get("_eta_str", "N/A").strip()

            self.progress["value"] = pct
            self.after(0, self._set_status, f"Downloading... {pct:.1f}%", ACCENT)
            self.after(0, self._set_detail, "speed", speed)
            self.after(0, self._set_detail, "eta", eta)
            self.after(0, self._set_detail, "filesize",
                       f"{self._fmt_size(downloaded)} / {self._fmt_size(total)}")

        elif d["status"] == "finished":
            self.after(0, self._set_status, "Processing / merging...", GOLD)
            self.after(0, self._set_detail, "speed", "—")
            self.after(0, self._set_detail, "eta", "—")

    def _download_video(self, url):
        quality_label = self.quality.get()
        fmt = QUALITY_MAP.get(quality_label, QUALITY_MAP["Best available"])
        is_audio = quality_label == "Audio only (MP3)"

        ydl_opts = {
            "format": fmt,
            "outtmpl": os.path.join(self.output_dir, "%(title)s.%(ext)s"),
            "merge_output_format": "mp4",
            "progress_hooks": [self._progress_hook],
            "noplaylist": True,
            "quiet": True,
        }
        if is_audio:
            ydl_opts["postprocessors"] = [{
                "key": "FFmpegExtractAudio", "preferredcodec": "mp3",
            }]

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

                self.after(0, self._set_detail, "title", info.get("title", "—"))
                self.after(0, self._set_detail, "uploader", info.get("uploader", "—"))
                self.after(0, self._set_detail, "duration", self._fmt_duration(info.get("duration")))
                self.after(0, self._set_detail, "views",
                           f"{info.get('view_count', 0):,}" if info.get("view_count") else "—")
                res = f"{info.get('width', '?')}x{info.get('height', '?')}" if info.get("height") else "Audio"
                self.after(0, self._set_detail, "resolution", res)
                self.after(0, self._set_status, "Starting download...", GOLD)

                ydl.download([url])

            self.after(0, self.progress.config, {"value": 100})
            self.after(0, self._set_status, f"✅ Done: {info.get('title')}", ACCENT)

        except Exception as e:
            self.after(0, self._set_status, f"❌ Error: {e}", RED)

        finally:
            self.after(0, self.download_btn.config, {"state": "normal", "text": "⬇  DOWNLOAD"})
            self.after(0, self.pause_btn.config,
                       {"state": "disabled", "text": "⏸  PAUSE", "bg": "#3a3a3a", "fg": SUBTEXT})
            self.after(0, self.quality_box.config, {"state": "readonly"})


if __name__ == "__main__":
    app = YTDownloader()
    app.mainloop()