from pathlib import Path
import subprocess
import sys


def main() -> int:
    notebooks = sorted(Path("notebooks").glob("chapter_*/*.ipynb"))
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
