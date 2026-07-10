# Using Pytube

# from pytube import YouTube
# from sys import argv

# link = argv[1]
# yt = YouTube(link)

# print("Title: ", yt.title)

# print("Views: ", yt.views)

# yd = yt.streams.get_highest_resolution()
# yd.download('C:/Users/anony/Downloads')

# Using yt_dlp
import yt_dlp

url = "https://youtu.be/Jjm3dVWRyS8?si=O4jqKM1cymryb5hz"
audio_only = False  # set True to download audio (mp3) instead of video

ydl_opts = {
    "format": "bestaudio/best" if audio_only else "bestvideo+bestaudio/best",
    "outtmpl": "C:/Users/anony/Downloads/%(title)s.%(ext)s",
    "merge_output_format": "mp4",
}

if audio_only:
    ydl_opts["postprocessors"] = [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
    }]

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print(f"✅ Downloaded: {info.get('title')}")
except Exception as e:
    print(f"❌ Error: {e}")