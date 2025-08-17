<p align="center">
  <img src="assets/demo.gif" width="800" alt="Demo video (GIF preview)">
  <br/>
  <a href="assets/demo.mp4">Download full MP4</a>
</p>

### VEO – Fast video generator with GUI
Generate short videos from prompts with a simple desktop GUI. Includes a consumer launcher that asks for your Gemini API key and installs what’s needed.

### New to this? Start here (super simple)
1) Get a Gemini API key (free tier available):
   - Go to `https://aistudio.google.com/app/apikey`
   - Sign in → Create API key → Copy it (looks like `AIza...`). Keep it secret.
2) Start the app (Windows):
   - Open PowerShell, run:
     ```powershell
     cd C:\Users\kikox\Desktop\VEO
     python start_consumer.py
     ```
   - Paste your key when asked. Click Start App. The app opens after installing what’s needed.
3) Start the app (macOS/Linux):
   ```bash
   cd ~/Desktop/VEO
   python3 start_consumer.py
   ```
   Paste your key → Start App.

Optional (better embedded playback):
- Windows:
  ```powershell
  winget install -e --id VideoLAN.VLC
  ```
- macOS: install VLC from videolan.org

### Using the app
- Choose a template or type your own prompt.
- Elements Brush: check Randomize to get a new style and wording for every video.
- Pouring Breakfast: enter a Liquid (e.g., milk, tahini) and a Surface (e.g., cereals, toast).
- Set number of videos → Generate. Select a video under Downloads to play. Use the controls (Play/Pause/Stop/Replay, Next/Prev, Mute, Hide Player).

### Privacy
- Your API key is stored in memory and passed via `GEMINI_API_KEY` to the app.
- The app does not upload your key anywhere.

---
Tip: GIF previews load inline on GitHub. For best quality, view the MP4.
