from pathlib import Path
import argparse


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOOK = "economia_computacional_python"


def main() -> None:
    parser = argparse.ArgumentParser(description="Preparar limpieza de datos de un libro.")
    parser.add_argument("--book", default=DEFAULT_BOOK, help="Slug del libro dentro de books/.")
    args = parser.parse_args()

    book_data = ROOT / "books" / args.book / "data"
    processed_dir = book_data / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)
    print(
        "Limpieza pendiente: leer desde "
        f"{(book_data / 'raw').relative_to(ROOT)} y escribir derivados en "
        f"{processed_dir.relative_to(ROOT)}."
    )
    print("No sobrescribir archivos originales.")


if __name__ == "__main__":
    main()
