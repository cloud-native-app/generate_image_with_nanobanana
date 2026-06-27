from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw


def default_root() -> Path:
    candidates = [
        path
        for path in Path.cwd().iterdir()
        if path.is_dir() and path.name not in {".git", "scripts", ".gh-temp"}
    ]
    if len(candidates) != 1:
        raise FileNotFoundError("Run from the repository root or pass a single workpack directory.")
    return candidates[0]


def first_dir(root: Path, prefix: str) -> Path:
    matches = sorted(path for path in root.iterdir() if path.is_dir() and path.name.startswith(prefix))
    if not matches:
        raise FileNotFoundError(f"No directory under {root} starts with {prefix!r}.")
    return matches[0]


def part1_dir(root: Path) -> Path:
    return first_dir(root, "03_") / "Part1"


def remove_p1_f46_tracking_code(path: Path) -> None:
    image = Image.open(path).convert("RGB")
    draw = ImageDraw.Draw(image)
    width, height = image.size
    draw.rectangle((int(width * 0.86), int(height * 0.88), width, height), fill=(255, 255, 255))
    image.save(path)


def main() -> int:
    root = default_root()
    remove_p1_f46_tracking_code(part1_dir(root) / "P1-F46.png")
    print("fixed P1-F46 tracking code artifact")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
