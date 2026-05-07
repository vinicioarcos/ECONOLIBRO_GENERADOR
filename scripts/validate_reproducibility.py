from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOOK = "economia_computacional_python"

REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "ROADMAP.md",
    "requirements.txt",
    "environment.yml",
    "pyproject.toml",
    f"books/{DEFAULT_BOOK}/book/index.md",
    "templates/checklist_libro.md",
    "examples/economia_computacional_python.md",
]


def main() -> int:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).exists()]
    raw_files = [
        p
        for p in (ROOT / "books" / DEFAULT_BOOK / "data" / "raw").glob("*")
        if p.name != ".gitkeep" and p.is_file()
    ]
    if missing:
        print("Faltan archivos requeridos:")
        for path in missing:
            print(f"- {path}")
        return 1
    print("Estructura base verificada.")
    print(
        "Archivos originales en "
        f"books/{DEFAULT_BOOK}/data/raw: {len(raw_files)}"
    )
    print(
        "Recordatorio: no modificar data/raw del libro; "
        "escribir derivados en data/processed del mismo libro."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
