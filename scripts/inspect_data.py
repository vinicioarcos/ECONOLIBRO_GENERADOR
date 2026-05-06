from pathlib import Path


def main() -> None:
    for folder in [Path("data/raw"), Path("data/processed"), Path("data/external")]:
        files = [p.name for p in folder.glob("*") if p.name != ".gitkeep"]
        print(f"{folder}: {len(files)} archivo(s)")


if __name__ == "__main__":
    main()
