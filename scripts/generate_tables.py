from pathlib import Path
import argparse


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOOK = "economia_computacional_python"


def main() -> None:
    parser = argparse.ArgumentParser(description="Preparar tablas de un libro.")
    parser.add_argument("--book", default=DEFAULT_BOOK, help="Slug del libro dentro de books/.")
    args = parser.parse_args()

    (ROOT / "books" / args.book / "outputs" / "tables").mkdir(parents=True, exist_ok=True)
    print("Generacion de tablas pendiente: incluir notas, fuente e interpretacion.")


if __name__ == "__main__":
    main()
