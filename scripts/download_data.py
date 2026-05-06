from pathlib import Path


RAW_DIR = Path("data/raw")


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print("Descarga pendiente: registrar fuente real antes de descargar datos.")
    print("Regla: este script puede guardar originales en data/raw sin transformarlos.")


if __name__ == "__main__":
    main()
