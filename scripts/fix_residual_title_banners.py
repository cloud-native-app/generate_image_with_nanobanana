from __future__ import annotations

from pathlib import Path

from PIL import Image


TITLE_CROPS = {
    "P4-F75": 105,
    "P4-F05": 100,
    "P5-F19": 100,
    "P5-F62": 158,
}


def find_completed_image(root: Path, code: str) -> Path:
    matches = [
        path
        for path in root.rglob(f"{code}.png")
        if "03_" in str(path) and path.parent.name.startswith("Part")
    ]
    if len(matches) != 1:
        raise FileNotFoundError(f"Expected one completed image for {code}, found {len(matches)}.")
    return matches[0]


def edge_background(image: Image.Image) -> tuple[int, int, int]:
    width, height = image.size
    samples = []
    for x in (0, width // 2, width - 1):
        for y in range(max(0, height - 24), height):
            samples.append(image.getpixel((x, y)))
    return tuple(sorted(channel)[len(channel) // 2] for channel in zip(*samples))


def remove_top_band(path: Path, crop_px: int) -> None:
    with Image.open(path) as source:
        image = source.convert("RGB")
    width, height = image.size
    cropped = image.crop((0, crop_px, width, height))
    fixed = Image.new("RGB", (width, height), edge_background(image))
    fixed.paste(cropped, (0, 0))
    fixed.save(path, "PNG")


def main() -> None:
    root = Path.cwd()
    for code, crop_px in TITLE_CROPS.items():
        path = find_completed_image(root, code)
        remove_top_band(path, crop_px)
        print(f"fixed {code}: removed top {crop_px}px from {path}")


if __name__ == "__main__":
    main()
