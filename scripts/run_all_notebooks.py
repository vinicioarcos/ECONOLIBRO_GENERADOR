from pathlib import Path
import argparse
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOOK = "economia_computacional_python"


def main() -> int:
    parser = argparse.ArgumentParser(description="Ejecutar notebooks de un libro.")
    parser.add_argument(
        "--book",
        default=DEFAULT_BOOK,
        help="Slug del libro dentro de books/.",
    )
    args = parser.parse_args()

    notebooks_dir = ROOT / "books" / args.book / "notebooks"
    notebooks = sorted(notebooks_dir.glob("chapter_*/*.ipynb"))
    if not notebooks:
        print("No hay notebooks para ejecutar.")
        return 0
    for notebook in notebooks:
        print(f"Ejecutando {notebook}")
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                "--inplace",
                str(notebook),
            ],
            check=False,
        )
        if result.returncode != 0:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
