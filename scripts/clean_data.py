from pathlib import Path


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    print("Limpieza pendiente: leer desde data/raw y escribir derivados en data/processed.")
    print("No sobrescribir archivos originales.")


if __name__ == "__main__":
    main()
