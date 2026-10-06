"""Regenerate legacy (API < 26) launcher PNGs from app/src/main/res/drawable-nodpi/logo.png.
Usage: python3 tools/make_icons.py   (needs Pillow)"""
from PIL import Image
import pathlib
res = pathlib.Path(__file__).resolve().parent.parent / "app/src/main/res"
logo = Image.open(res / "drawable-nodpi/logo.png").convert("RGBA")
BG = (11, 93, 59, 255)  # match @color/iconBackground
for d, px in {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}.items():
    canvas = Image.new("RGBA", (px, px), BG)
    size = round(px * 0.72)  # 14% padding each side -> logo fully visible
    l = logo.copy(); l.thumbnail((size, size), Image.LANCZOS)
    canvas.alpha_composite(l, ((px - l.width) // 2, (px - l.height) // 2))
    for name in ("ic_launcher", "ic_launcher_round"):
        canvas.save(res / f"mipmap-{d}" / f"{name}.png")
