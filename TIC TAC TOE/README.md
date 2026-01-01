# 🎮 Tic Tac Toe - Modern Web App

A beautiful, modern Tic Tac Toe game with natural aesthetic colors, glassmorphism UI, and smooth animations.

## 🎨 Features

- **Natural Color Palette**: Forest green, warm terracotta, ocean blue, and soft gold
- **Glassmorphism Design**: Semi-transparent UI with backdrop blur effects
- **Smooth Animations**: Hover effects, victory celebrations, and transitions
- **Score Tracking**: Keeps track of wins and draws across multiple games
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI/UX**: Premium aesthetics with micro-interactions

## 🚀 How to Run the App

### Method 1: Double-Click (Simplest)

1. Navigate to the folder: `d:\Coddy World\ShowCase Python\ShowCase-Python-\TIC TAC TOE`
2. Double-click on `index.html`
3. The game will open in your default web browser

### Method 2: Using Python HTTP Server (Recommended)

1. Open **PowerShell** or **Command Prompt**
2. Navigate to the game folder:
   ```powershell
   cd "d:\Coddy World\ShowCase Python\ShowCase-Python-\TIC TAC TOE"
   ```
3. Start the Python HTTP server:
   ```powershell
   python -m http.server 8000
   ```
4. Open your web browser and go to:
   ```
   http://localhost:8000/index.html
   ```
5. To stop the server, press `Ctrl+C` in the terminal


## 📁 Project Structure

```
TIC TAC TOE/
├── index.html      # Main HTML structure
├── style.css       # Styling with natural colors and animations
├── script.js       # Game logic (ported from Python)
├── main.py         # Original Python console version
└── README.md       # This file
```

## 🎯 How to Play

1. **Start the Game**: Open the app using any method above
2. **Make Your Move**: Click on any empty cell to place your mark
3. **Win Condition**: Get three marks in a row (horizontal, vertical, or diagonal)
4. **New Game**: Click the "New Game" button to reset the board
5. **Track Scores**: Your wins are tracked in the score board at the bottom

## 🎨 Color Scheme

| Element | Color | Hex Code |
|---------|-------|----------|
| Player X | Forest Green | `#2d6a4f` |
| Player O | Warm Terracotta | `#d4a373` |
| Background | Ocean Blue Gradient | `#1a1a2e → #0f3460` |
| Accents | Soft Gold | `#e9c46a` |
| Highlights | Sage Green | `#52b788` |

## 🛠️ Technologies Used

- **HTML5**: Semantic structure
- **CSS3**: Glassmorphism, animations, responsive design
- **JavaScript (ES6)**: Game logic and interactivity
- **Google Fonts**: Poppins font family

## 📱 Browser Compatibility

Works on all modern browsers:
- ✅ Chrome / Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera

## 💡 Tips

- **Hard Refresh**: If you don't see updates, press `Ctrl+F5` (Windows) or `Cmd+Shift+R` (Mac)
- **Best Experience**: Use Chrome or Edge for the best glassmorphism effects
- **Mobile**: The game is fully responsive and touch-enabled for mobile devices

## 🎮 Game Features

### Core Gameplay
- ✅ Two-player turn-based gameplay
- ✅ Win detection for all 8 possible combinations
- ✅ Draw detection when board is full
- ✅ Cell validation (can't overwrite taken cells)

### Visual Features
- ✅ Animated gradient background
- ✅ Glassmorphism container with blur
- ✅ Pulsing player turn indicator
- ✅ Mark appearance animations
- ✅ Victory cell highlighting
- ✅ Full-screen victory overlay
- ✅ Smooth hover and click effects

### User Experience
- ✅ Persistent score tracking
- ✅ Keyboard support (ESC to close victory screen)
- ✅ Touch support for mobile
- ✅ Responsive design for all screen sizes

## 📝 Original Python Version

The original Python console version is still available in `main.py`. To run it:

```powershell
python main.py
```

## 🎉 Enjoy!

Have fun playing this beautiful, modern Tic Tac Toe game! The natural color scheme provides a calming, aesthetic experience while you play.

---

**Created**: 2026-01-02  
**Version**: 1.0  
**Design**: Modern Glassmorphism with Natural Aesthetic Colors
