from pathlib import Path


def main() -> None:
    Path("outputs/tables").mkdir(parents=True, exist_ok=True)
    print("Generacion de tablas pendiente: incluir notas, fuente e interpretacion.")


if __name__ == "__main__":
    main()
