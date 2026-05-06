"""Render chapter deliverables with Quarto.

Each deliverable bundles the chapter Markdown plus student exercises and the
teacher guide when they exist. Quarto renders the bundle to PDF through Typst,
so LaTeX/TinyTeX is not required.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "chapters"
EXERCISES_DIR = ROOT / "exercises"
OUTPUT_DIR = ROOT / "outputs" / "final" / "quarto"
BUILD_DIR = ROOT / "_quarto_generated" / "pdf"
LOCAL_QUARTO = Path.home() / "AppData" / "Local" / "Programs" / "Quarto" / "bin" / "quarto.cmd"


def find_quarto() -> str:
    command = shutil.which("quarto")
    if command:
        return command
    if LOCAL_QUARTO.exists():
        return str(LOCAL_QUARTO)
    raise FileNotFoundError(
        "No se encontro Quarto. Instale Quarto o agregue quarto al PATH."
    )


def chapter_number(path: Path) -> str:
    return path.name.split("_", 1)[0]


def resolve_scope(book: str | None) -> tuple[Path, Path, Path, Path]:
    if not book:
        return CHAPTERS_DIR, EXERCISES_DIR, OUTPUT_DIR, BUILD_DIR

    book_root = ROOT / "books" / book
    return (
        book_root / "chapters",
        book_root / "exercises",
        book_root / "outputs" / "final" / "quarto",
        ROOT / "_quarto_generated" / "pdf" / book,
    )


def chapter_paths(chapters_dir: Path, selected: str | None) -> list[Path]:
    if selected:
        number = selected.zfill(2)
        matches = sorted(chapters_dir.glob(f"{number}_*.md"))
        if not matches:
            raise FileNotFoundError(f"No se encontro el capitulo {number}")
        return matches
    return sorted(chapters_dir.glob("[0-9][0-9]_*.md"))


def read_if_exists(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def bundle_markdown(chapter_path: Path, exercises_dir: Path, subtitle: str) -> str:
    number = chapter_number(chapter_path)
    exercise_dir = exercises_dir / f"chapter_{number}"
    chapter = read_if_exists(chapter_path)
    exercises = read_if_exists(exercise_dir / "ejercicios.md")
    teacher_guide = read_if_exists(exercise_dir / "soluciones_docente.md")

    parts = [
        "---",
        f'title: "Entregable Capitulo {number}"',
        f'subtitle: "{subtitle}"',
        'lang: "es"',
        "format:",
        "  typst:",
        "    toc: true",
        "    number-sections: false",
        "    papersize: a4",
        "    margin:",
        "      x: 2.2cm",
        "      y: 2.4cm",
        "execute:",
        "  echo: true",
        "---",
        "",
        chapter,
    ]

    if exercises:
        parts.extend(["", "{{< pagebreak >}}", "", "# Anexo A. Ejercicios del estudiante", "", exercises])

    if teacher_guide:
        parts.extend(["", "{{< pagebreak >}}", "", "# Anexo B. Guia docente", "", teacher_guide])

    return "\n".join(parts).strip() + "\n"


def render_chapter(
    quarto: str,
    chapter_path: Path,
    exercises_dir: Path,
    output_dir: Path,
    build_dir_base: Path,
    subtitle: str,
) -> Path:
    number = chapter_number(chapter_path)
    slug = chapter_path.stem
    build_dir = build_dir_base / f"chapter_{number}"
    build_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    qmd_path = build_dir / f"chapter_{number}_entregable.qmd"
    qmd_path.write_text(
        bundle_markdown(chapter_path, exercises_dir, subtitle),
        encoding="utf-8",
    )

    output_name = f"{slug}_entregable.pdf"
    expected = output_dir / output_name
    if expected.exists():
        expected.unlink()
    subprocess.run(
        [
            quarto,
            "render",
            str(qmd_path.relative_to(ROOT)),
            "--to",
            "typst",
            "--output",
            output_name,
            "--output-dir",
            str(output_dir.relative_to(ROOT)),
        ],
        check=True,
        cwd=ROOT,
    )
    return normalize_quarto_output(build_dir, output_dir, output_name)


def normalize_quarto_output(build_dir: Path, output_dir: Path, output_name: str) -> Path:
    expected = output_dir / output_name
    if expected.exists():
        return expected

    candidates = [
        build_dir / output_name,
        build_dir / output_dir.relative_to(ROOT) / output_name,
        build_dir / "books" / output_name,
    ]
    candidates.extend(build_dir.rglob(output_name))
    for candidate in candidates:
        if candidate.exists():
            expected.parent.mkdir(parents=True, exist_ok=True)
            if expected.exists():
                expected.unlink()
            shutil.move(str(candidate), str(expected))
            return expected

    raise FileNotFoundError(f"No se encontro la salida esperada: {output_name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--chapter",
        help="Numero de capitulo, por ejemplo 01 o 2. Omitir para renderizar todos.",
    )
    parser.add_argument(
        "--book",
        help="Slug del libro dentro de books/, por ejemplo econometria_financiera_python.",
    )
    parser.add_argument(
        "--subtitle",
        default="Economia Computacional con Python",
        help="Subtitulo que se usara en el PDF.",
    )
    args = parser.parse_args()

    quarto = find_quarto()
    chapters_dir, exercises_dir, output_dir, build_dir_base = resolve_scope(args.book)
    outputs = [
        render_chapter(
            quarto,
            path,
            exercises_dir,
            output_dir,
            build_dir_base,
            args.subtitle,
        )
        for path in chapter_paths(chapters_dir, args.chapter)
    ]
    for output in outputs:
        print(output.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
