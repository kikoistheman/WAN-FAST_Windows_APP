# Video App (Consumer Setup)
<p align="center">
  <video src="assets/demo.mp4" width="800" controls muted loop></video>
</p>
This guide helps you run the app even if you’ve never used Python and don’t know what an API key is.

## 1) What is a Gemini API key?
- It’s like a password that lets the app generate smarter prompts using Google’s AI.
- You create it once, copy it, and paste it into the app. You can delete it later from your account.

## 2) Create a Gemini API key (free tier available)
1. Open Google AI Studio: https://aistudio.google.com/app/apikey
2. Sign in with your Google account.
3. Click “Create API key”.
4. Copy the key that looks like: AIza... (keep it secret).

## 3) Windows (recommended)
- You don’t need to manually install Python. The launcher can set things up for you.

Steps:
1. Download this project folder to your computer (e.g., Desktop\VEO).
2. Double-click `start_consumer.py` (or right‑click → Open with → Python if needed).
3. Paste your Gemini API key in the window.
4. Click “Start App”.
5. The launcher will install needed parts (this can take a minute). Then the main app opens.

Tips:
- If you’re asked to allow the app in SmartScreen, click “More info” → “Run anyway”.
- For embedded video playback, you can also install VLC (optional):
  - Open PowerShell and run: `winget install -e --id VideoLAN.VLC`

## 4) macOS
- If you already have Python 3.10+ installed, double‑click `start_consumer.py`.
- If it doesn’t open, install Python: https://www.python.org/downloads/

Then:
1. Open Terminal.
2. Change directory to the app folder. Example:
   ```
   cd ~/Desktop/VEO
   ```
3. Launch the consumer starter:
   ```
   python3 start_consumer.py
   ```
4. Paste your Gemini API key and click Start.

Optional (for embedded playback):
- Install VLC from https://www.videolan.org/vlc/

## 5) Linux
1. Make sure Python 3.10+ is installed.
2. In a terminal:
   ```
   cd /path/to/VEO
   python3 start_consumer.py
   ```
3. Paste your Gemini API key.

Optional: install VLC via your package manager (e.g., `sudo apt install vlc`).

## 6) How to use the app
- Prompt: Type a description or use a Template.
- Elements Brush: set an element, or enable Randomize for fresh prompts per video.
- Pouring Breakfast: enter Liquid and Surface (e.g., “milk” + “cereals”).
- Set Number of videos and click Generate.
- Videos appear in the list; select one to play inside the app. Use the controls to play/pause/stop/replay, next/prev, mute, or hide the player.

## 7) Privacy
- Your API key is only used locally to create text prompts and is passed to the app via an environment variable. The app doesn’t upload your key to any server.

## 8) Troubleshooting
- If you see messages about installing packages, wait until it finishes.
- If embedded playback fails, the app will try another player or open the file with your default video player.
- If nothing opens:
  - Run the launcher from a terminal to see messages:
    - Windows: open PowerShell, `cd` to the folder, run `python start_consumer.py`
    - macOS/Linux: `python3 start_consumer.py`

## 9) Uninstall / Cleanup
- You can simply delete the folder. This removes the app and any downloaded videos.
- To revoke your API key, visit `https://aistudio.google.com/app/apikey` and delete it.
