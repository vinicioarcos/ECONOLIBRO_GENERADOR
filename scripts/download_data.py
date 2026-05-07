from pathlib import Path
import argparse


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOOK = "economia_computacional_python"


def main() -> None:
    parser = argparse.ArgumentParser(description="Preparar carpeta data/raw de un libro.")
    parser.add_argument("--book", default=DEFAULT_BOOK, help="Slug del libro dentro de books/.")
    args = parser.parse_args()

    raw_dir = ROOT / "books" / args.book / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    print("Descarga pendiente: registrar fuente real antes de descargar datos.")
    print(f"Regla: este script puede guardar originales en {raw_dir.relative_to(ROOT)} sin transformarlos.")


if __name__ == "__main__":
    main()
