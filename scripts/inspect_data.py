from pathlib import Path
import argparse


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOOK = "economia_computacional_python"


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspeccionar datos de un libro.")
    parser.add_argument("--book", default=DEFAULT_BOOK, help="Slug del libro dentro de books/.")
    args = parser.parse_args()

    book_data = ROOT / "books" / args.book / "data"
    for folder in [book_data / "raw", book_data / "processed", book_data / "external"]:
        files = [p.name for p in folder.glob("*") if p.name != ".gitkeep"]
        print(f"{folder.relative_to(ROOT)}: {len(files)} archivo(s)")


if __name__ == "__main__":
    main()
