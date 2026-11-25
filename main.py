"""One word, first thought: vellichor.

The strange strangeness of used bookstores.
"""
import os
from pathlib import Path


def main():
    word_path = Path(__file__).resolve().parent / "word.txt"
    word = word_path.read_text(encoding="utf-8").strip()
    print(word)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        Path(out_dir).mkdir(parents=True, exist_ok=True)
        (Path(out_dir) / "output.txt").write_text(word + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
