from pathlib import Path
import argparse


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOOK = "economia_computacional_python"


def main() -> None:
    parser = argparse.ArgumentParser(description="Preparar variables construidas de un libro.")
    parser.add_argument("--book", default=DEFAULT_BOOK, help="Slug del libro dentro de books/.")
    args = parser.parse_args()

    (ROOT / "books" / args.book / "data" / "processed").mkdir(parents=True, exist_ok=True)
    print("Feature engineering pendiente: documentar cada variable construida.")


if __name__ == "__main__":
    main()
