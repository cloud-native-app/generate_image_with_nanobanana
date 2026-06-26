from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(r"C:\Users\javam\OneDrive\Documents\그림만들기\나노바나나_전체_수정대상_작업팩_v2")
IMG = ROOT / "03_수정완료" / "Part3" / "P3-F12.png"
FONT = Path(r"C:\Windows\Fonts\malgun.ttf")
BOLD = Path(r"C:\Windows\Fonts\malgunbd.ttf")


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(BOLD if bold else FONT), size=size)


def main() -> None:
    image = Image.open(IMG).convert("RGB")
    draw = ImageDraw.Draw(image)

    # Remove whole-image title banners that Part3 figures must not contain.
    bg = image.getpixel((25, 20))
    draw.rectangle((0, 0, image.width, 140), fill=bg)

    # Fix a model typo in the right-side Step 1 explanation.
    draw.rounded_rectangle((1288, 255, 1542, 302), radius=8, fill=(245, 248, 250))
    draw.text((1316, 256), "발신 MTA 등", font=font(31, True), fill=(0, 0, 0))

    image.save(IMG)
    print(IMG)


if __name__ == "__main__":
    main()
