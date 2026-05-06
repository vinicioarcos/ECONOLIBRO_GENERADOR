from pathlib import Path


def main() -> None:
    Path("outputs/figures").mkdir(parents=True, exist_ok=True)
    print("Generacion de figuras pendiente: incluir titulo, fuente e interpretacion.")


if __name__ == "__main__":
    main()
