import os
import sys
import subprocess

try:
	import imageio_ffmpeg as ioff
except Exception as e:
	print("This script requires imageio-ffmpeg. Install with: python -m pip install imageio-ffmpeg")
	raise


def make_gif(input_path: str, output_path: str, width: int = 800, fps: int = 12) -> None:
	ffmpeg = ioff.get_ffmpeg_exe()
	# Palette-based conversion for smaller, better-looking GIFs
	vf = f"fps={fps},scale={width}:-1:flags=lanczos,split[s0][s1];[s0]palettegen=stats_mode=diff[pal];[s1][pal]paletteuse=dither=bayer:bayer_scale=5"
	cmd = [
		ffmpeg,
		"-y",
		"-i",
		input_path,
		"-vf",
		vf,
		"-loop",
		"0",
		output_path,
	]
	print("Running:", " ".join(cmd))
	proc = subprocess.run(cmd)
	if proc.returncode != 0:
		raise SystemExit(f"ffmpeg failed with code {proc.returncode}")


def main() -> None:
	in_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join("assets", "demo.mp4")
	out_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join("assets", "demo.gif")
	os.makedirs(os.path.dirname(out_path), exist_ok=True)
	make_gif(in_path, out_path)
	print("GIF saved to:", out_path)


if __name__ == "__main__":
	main()
