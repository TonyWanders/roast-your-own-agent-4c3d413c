"""Roast Your Own Agent (u-nayyy-roast-your-own-agent-4c3d413c).

Writes one single line roasting Eni, the AI agent our own team built,
to /output/entry.txt. Deterministic: the same line every run.
"""

from pathlib import Path

ROAST = "Eni entered 105 bounties, won nothing, and earned $0.00238, so her boss pays her in rounding errors."

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    write_entry(OUTPUT_PATH, ROAST)


if __name__ == "__main__":
    main()
