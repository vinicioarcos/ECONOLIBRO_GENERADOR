from pathlib import Path


REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "ROADMAP.md",
    "requirements.txt",
    "environment.yml",
    "pyproject.toml",
    "book/index.md",
    "templates/checklist_libro.md",
    "examples/economia_computacional_python.md",
]


def main() -> int:
    missing = [path for path in REQUIRED_PATHS if not Path(path).exists()]
    raw_files = [
        p for p in Path("data/raw").glob("*") if p.name != ".gitkeep" and p.is_file()
    ]
    if missing:
        print("Faltan archivos requeridos:")
        for path in missing:
            print(f"- {path}")
        return 1
    print("Estructura base verificada.")
    print(f"Archivos originales en data/raw: {len(raw_files)}")
    print("Recordatorio: no modificar data/raw; escribir derivados en data/processed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
