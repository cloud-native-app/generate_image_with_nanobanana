from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


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


def part2_dir(root: Path) -> Path:
    return first_dir(root, "03_") / "Part2"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/malgunbd.ttf") if bold else Path("C:/Windows/Fonts/malgun.ttf"),
        Path("C:/Windows/Fonts/malgun.ttf"),
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def cover(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], fill: tuple[int, int, int]) -> None:
    draw.rounded_rectangle(xy, radius=8, fill=fill)


def fix_p2_f15(path: Path) -> None:
    image = Image.open(path).convert("RGB")
    draw = ImageDraw.Draw(image)
    draw.rectangle((745, 774, 870, 844), fill=(249, 251, 252))
    image.save(path)


def fix_p2_f52(path: Path) -> None:
    image = Image.open(path).convert("RGB")
    draw = ImageDraw.Draw(image)
    # Clarify top-down rule evaluation text in the lower example panel.
    cover(draw, (175, 436, 625, 468), (250, 252, 253))
    draw.text(
        (178, 437),
        "규칙 순서 예시 (위에서 아래로 평가, First Match)",
        fill=(13, 35, 58),
        font=font(22, bold=True),
    )
    image.save(path)


def fix_p2_f55(path: Path) -> None:
    image = Image.open(path).convert("RGB")
    draw = ImageDraw.Draw(image)
    # Make the tuning trade-off explicit to avoid sensitivity/specificity ambiguity.
    cover(draw, (1056, 520, 1452, 646), (242, 248, 250))
    draw.text((1065, 525), "튜닝 (Sensitivity <-> Specificity)", fill=(13, 35, 58), font=font(20, bold=True))
    draw.text((1065, 558), "민감도↑(임계값↓) -> 미탐(FN)↓, 오탐(FP)↑", fill=(13, 35, 58), font=font(16))
    draw.text((1065, 586), "특이도↑(임계값↑) -> 오탐(FP)↓, 미탐(FN)↑", fill=(13, 35, 58), font=font(16))
    draw.text((1065, 614), "환경에 맞는 임계값·예외 조정 필요", fill=(13, 86, 92), font=font(16, bold=True))
    image.save(path)


def main() -> int:
    root = default_root()
    directory = part2_dir(root)
    fix_p2_f15(directory / "P2-F15.png")
    fix_p2_f52(directory / "P2-F52.png")
    fix_p2_f55(directory / "P2-F55.png")
    print("fixed P2-F15 P2-F52 P2-F55")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
