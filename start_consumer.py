import os
import sys
import subprocess
import threading
import tkinter as tk
from tkinter import ttk, messagebox

# Minimal list of runtime dependencies needed by test.py
REQUIRED_PACKAGES = [
    "requests",
    "Pillow",
    "google-generativeai",
    "imageio",
    "imageio-ffmpeg",
    # At least one embedded player backend; we'll try tkintervideo first, VLC is optional fallback
    "tkintervideo",
]

OPTIONAL_PACKAGES = [
    # VLC backend if users prefer installing VLC app; optional
    "python-vlc",
    # Alternative video widget
    "tkVideoPlayer",
]

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
APP_FILE = os.path.join(THIS_DIR, "test.py")


def run_pip_install(packages: list[str]) -> tuple[bool, str]:
    exe = sys.executable
    try:
        cmd = [exe, "-m", "pip", "install", "--upgrade"] + packages
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        ok = proc.returncode == 0
        out = proc.stdout + "\n" + proc.stderr
        return ok, out
    except Exception as e:
        return False, str(e)


def check_imports() -> list[str]:
    missing: list[str] = []
    for pkg in REQUIRED_PACKAGES:
        try:
            __import__(pkg.split("==")[0].replace("-", "_"))
        except Exception:
            missing.append(pkg)
    return missing


def launch_app(gemini_api_key: str) -> None:
    if not os.path.exists(APP_FILE):
        messagebox.showerror("Error", f"Could not find app file: {APP_FILE}")
        return

    env = os.environ.copy()
    env["GEMINI_API_KEY"] = gemini_api_key.strip()

    exe = sys.executable
    try:
        subprocess.Popen([exe, APP_FILE], env=env)
    except Exception as e:
        messagebox.showerror("Launch failed", f"Could not launch app: {e}")
        return


def on_start_clicked(entry_key: tk.Entry, btn: ttk.Button, status_lbl: ttk.Label, root: tk.Tk) -> None:
    key = entry_key.get().strip()
    if not key:
        messagebox.showwarning("Missing API Key", "Please paste your Gemini API key.")
        return

    btn.configure(state="disabled")
    status_lbl.configure(text="Checking and installing dependencies (this may take a minute)...")

    def worker():
        missing = check_imports()
        ok = True
        log_msgs: list[str] = []
        if missing:
            ok, out = run_pip_install(missing)
            log_msgs.append(out)
        # Optional packages (best-effort)
        if ok:
            run_pip_install(OPTIONAL_PACKAGES)
        def after():
            if not ok:
                messagebox.showwarning(
                    "Dependencies",
                    "Some dependencies failed to install. The app may still work.\n\n"
                    + "\n\n".join(log_msgs[:1])
                )
            status_lbl.configure(text="Launching app...")
            launch_app(key)
            root.after(600, root.destroy)
        root.after(0, after)

    threading.Thread(target=worker, daemon=True).start()


def build_gui() -> tk.Tk:
    root = tk.Tk()
    root.title("Video App Launcher")
    root.geometry("520x240")

    container = ttk.Frame(root, padding=16)
    container.pack(fill="both", expand=True)

    title = ttk.Label(container, text="Enter your Gemini API Key", font=("Segoe UI", 12, "bold"))
    title.pack(anchor="w")

    help_txt = ttk.Label(
        container,
        text=(
            "Paste the key you created in your Google AI Studio account.\n"
            "We will only use it to generate prompts locally and won’t upload it."
        ),
        justify="left",
        wraplength=480,
    )
    help_txt.pack(anchor="w", pady=(4, 10))

    entry = ttk.Entry(container, show="*", width=56)
    entry.pack(anchor="w")

    show_var = tk.BooleanVar(value=False)

    def toggle_show():
        entry.configure(show="" if show_var.get() else "*")

    show_chk = ttk.Checkbutton(container, text="Show key", variable=show_var, command=toggle_show)
    show_chk.pack(anchor="w", pady=(6, 6))

    status_lbl = ttk.Label(container, text="")
    status_lbl.pack(anchor="w", pady=(4, 8))

    start_btn = ttk.Button(container, text="Start App", command=lambda: on_start_clicked(entry, start_btn, status_lbl, root))
    start_btn.pack(anchor="e")

    return root


def main() -> None:
    try:
        root = build_gui()
        try:
            ttk.Style().theme_use("clam")
        except Exception:
            pass
        root.mainloop()
    except Exception as e:
        # Fallback to CLI prompt
        print("GUI failed to start. Falling back to console.")
        key = input("Paste your GEMINI API key: ").strip()
        if not key:
            print("No API key provided. Exiting.")
            return
        missing = check_imports()
        if missing:
            print("Installing required packages... This may take a minute...")
            ok, out = run_pip_install(missing)
            if not ok:
                print("Warning: Some dependencies failed to install. The app may still work.")
                print(out)
        launch_app(key)


if __name__ == "__main__":
    main()
