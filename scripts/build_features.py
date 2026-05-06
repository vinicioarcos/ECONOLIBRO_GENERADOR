from pathlib import Path


def main() -> None:
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    print("Feature engineering pendiente: documentar cada variable construida.")


if __name__ == "__main__":
    main()
