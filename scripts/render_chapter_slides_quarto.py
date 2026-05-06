"""Render chapter slide decks with Quarto.

The generated slides are classroom deliverables in HTML, PowerPoint, and PDF.
They summarize the chapter, learning outcomes, concepts, workflow, common
errors, and activities.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "chapters"
EXERCISES_DIR = ROOT / "exercises"
OUTPUT_DIR = ROOT / "outputs" / "final" / "slides"
BUILD_DIR = ROOT / "_quarto_generated" / "slides"
LOCAL_QUARTO = Path.home() / "AppData" / "Local" / "Programs" / "Quarto" / "bin" / "quarto.cmd"
LOCAL_CHROME = Path("C:/Program Files/Google/Chrome/Application/chrome.exe")


def find_quarto() -> str:
    command = shutil.which("quarto")
    if command:
        return command
    if LOCAL_QUARTO.exists():
        return str(LOCAL_QUARTO)
    raise FileNotFoundError(
        "No se encontro Quarto. Instale Quarto o agregue quarto al PATH."
    )


def find_chrome() -> str:
    for command in ["chrome", "msedge"]:
        found = shutil.which(command)
        if found:
            return found
    if LOCAL_CHROME.exists():
        return str(LOCAL_CHROME)
    raise FileNotFoundError(
        "No se encontro Chrome o Edge para exportar RevealJS a PDF."
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
        book_root / "outputs" / "final" / "slides",
        ROOT / "_quarto_generated" / "slides" / book,
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


def first_heading(markdown: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Capitulo"


def section(markdown: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##\s+\d+\.\s+{re.escape(heading)}\s*$",
        flags=re.MULTILINE | re.IGNORECASE,
    )
    match = pattern.search(markdown)
    if not match:
        return ""
    start = match.end()
    next_match = re.search(r"^##\s+\d+\.\s+", markdown[start:], flags=re.MULTILINE)
    end = start + next_match.start() if next_match else len(markdown)
    return markdown[start:end].strip()


def subheading_text(markdown: str, subheading: str) -> str:
    pattern = re.compile(
        rf"^###\s+{re.escape(subheading)}\s*$",
        flags=re.MULTILINE | re.IGNORECASE,
    )
    match = pattern.search(markdown)
    if not match:
        return ""
    start = match.end()
    next_match = re.search(r"^###\s+", markdown[start:], flags=re.MULTILINE)
    end = start + next_match.start() if next_match else len(markdown)
    return markdown[start:end].strip()


def bullets_from_text(text: str, limit: int = 5) -> list[str]:
    bullets: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            bullets.append(stripped)
        elif re.match(r"^\d+\.\s+", stripped):
            bullets.append(re.sub(r"^\d+\.\s+", "- ", stripped))
        if len(bullets) >= limit:
            break
    return bullets


def prose_bullets(text: str, limit: int = 4) -> list[str]:
    clean = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    clean = re.sub(r"\|.*\|", "", clean)
    parts = re.split(r"(?<=[.!?])\s+", clean.replace("\n", " "))
    bullets: list[str] = []
    for part in parts:
        sentence = part.strip()
        if 35 <= len(sentence) <= 180:
            bullets.append("- " + sentence)
        if len(bullets) >= limit:
            break
    return bullets


def slide(title: str, body: list[str] | str) -> str:
    content = "\n".join(body) if isinstance(body, list) else body
    return f"## {title}\n\n{content.strip()}\n"


def figure_paths(chapter_path: Path) -> list[Path]:
    number = chapter_number(chapter_path)
    book_root = chapter_path.parent.parent if chapter_path.parent.name == "chapters" else ROOT
    figures_dir = book_root / "outputs" / "figures"
    patterns = [
        f"chapter_{number}_*.png",
        f"chapter_{number}_*.jpg",
        f"chapter_{number}_*.jpeg",
        f"chapter_{number}_*.svg",
    ]
    paths: list[Path] = []
    for pattern in patterns:
        paths.extend(sorted(figures_dir.glob(pattern)))
    return paths[:3]


def figure_slide_lines(paths: list[Path], qmd_dir: Path) -> list[str]:
    if not paths:
        return []

    lines = ["## Graficos del capitulo", ""]
    for path in paths:
        relative = os.path.relpath(path, start=qmd_dir).replace("\\", "/")
        caption = path.stem.replace("_", " ").title()
        lines.append(f"![{caption}]({relative}){{fig-align=\"center\" width=\"82%\"}}")
        lines.append("")
    return lines


def bundle_slides(
    chapter_path: Path,
    exercises_dir: Path,
    subtitle: str,
    qmd_dir: Path,
) -> str:
    number = chapter_number(chapter_path)
    exercise_dir = exercises_dir / f"chapter_{number}"
    chapter = read_if_exists(chapter_path)
    exercises = read_if_exists(exercise_dir / "ejercicios.md")

    title = first_heading(chapter)
    apertura = section(chapter, "Apertura")
    pregunta = subheading_text(apertura, "Pregunta motivadora")
    resultados = bullets_from_text(section(chapter, "Resultados de aprendizaje"), 5)
    conceptos = bullets_from_text(section(chapter, "Conceptos clave"), 8)
    intuicion = prose_bullets(section(chapter, "Intuicion economica"), 4)
    datos = prose_bullets(section(chapter, "Datos"), 4)
    python = prose_bullets(section(chapter, "Implementacion en Python"), 4)
    interpretacion = prose_bullets(section(chapter, "Interpretacion economica"), 4)
    errores = bullets_from_text(section(chapter, "Errores frecuentes"), 6)
    resumen = prose_bullets(section(chapter, "Resumen del capitulo"), 3)
    actividad = bullets_from_text(section(exercises, "Mini-proyecto"), 6) or prose_bullets(
        section(chapter, "Mini-proyecto"), 4
    )

    slides = [
        "---",
        f'title: "{title}"',
        f'subtitle: "{subtitle}"',
        'lang: "es"',
        "format:",
        "  revealjs:",
        "    theme: simple",
        "    slide-number: true",
        "    chalkboard: true",
        "    preview-links: auto",
        "    footer: \"Serie Econolab Computacional\"",
        "    transition: fade",
        "execute:",
        "  echo: true",
        "---",
        "",
        slide("Pregunta guia", pregunta or "- Que problema economico vamos a aprender a resolver?"),
        slide("Resultados de aprendizaje", resultados or ["- Resultado pendiente de desarrollar."]),
        slide("Conceptos clave", conceptos or ["- Conceptos pendientes de desarrollar."]),
        slide("Intuicion economica", intuicion or ["- Intuicion pendiente de desarrollar."]),
        slide("Datos y trazabilidad", datos or ["- Fuente, variables y advertencias pendientes."]),
        "\n".join(figure_slide_lines(figure_paths(chapter_path), qmd_dir)),
        slide("Flujo en Python", python or ["- Notebook reproducible pendiente."]),
        slide("Interpretacion", interpretacion or ["- Interpretacion pendiente."]),
        slide("Errores frecuentes", errores or ["- Evitar rutas absolutas.", "- No afirmar causalidad sin identificacion."]),
        slide("Actividad de clase", actividad or ["- Mini-proyecto pendiente."]),
        slide("Cierre", resumen or ["- Resumen pendiente de desarrollar."]),
    ]

    return "\n".join(slides).strip() + "\n"


def render_revealjs(quarto: str, qmd_path: Path, slug: str, output_dir: Path) -> Path:
    output_name = f"{slug}_slides.html"
    expected = output_dir / output_name
    if expected.exists():
        expected.unlink()
    subprocess.run(
        [
            quarto,
            "render",
            str(qmd_path.relative_to(ROOT)),
            "--to",
            "revealjs",
            "--output",
            output_name,
            "--output-dir",
            str(output_dir.relative_to(ROOT)),
        ],
        check=True,
        cwd=ROOT,
    )
    return normalize_quarto_output(qmd_path.parent, output_dir, output_name)


def render_pptx(quarto: str, qmd_path: Path, slug: str, output_dir: Path) -> Path:
    output_name = f"{slug}_slides.pptx"
    expected = output_dir / output_name
    if expected.exists():
        expected.unlink()
    subprocess.run(
        [
            quarto,
            "render",
            str(qmd_path.relative_to(ROOT)),
            "--to",
            "pptx",
            "--output",
            output_name,
            "--output-dir",
            str(output_dir.relative_to(ROOT)),
        ],
        check=True,
        cwd=ROOT,
    )
    return normalize_quarto_output(qmd_path.parent, output_dir, output_name)


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


def render_pdf(chrome: str, html_path: Path, slug: str, output_dir: Path) -> Path:
    pdf_path = output_dir / f"{slug}_slides.pdf"
    html_url = "file:///" + html_path.resolve().as_posix() + "?print-pdf"
    if pdf_path.exists():
        pdf_path.unlink()
    with tempfile.TemporaryDirectory(prefix="econolibro_chrome_") as profile_dir:
        subprocess.run(
            [
                chrome,
                "--headless=new",
                "--disable-gpu",
                "--disable-extensions",
                "--disable-background-networking",
                "--allow-file-access-from-files",
                "--run-all-compositor-stages-before-draw",
                "--virtual-time-budget=10000",
                f"--user-data-dir={profile_dir}",
                f"--print-to-pdf={pdf_path}",
                html_url,
            ],
            check=True,
            cwd=ROOT,
            timeout=90,
        )
    return pdf_path


def render_chapter(
    quarto: str,
    chrome: str,
    chapter_path: Path,
    output_dir: Path,
    build_dir_base: Path,
    exercises_dir: Path,
    subtitle: str,
) -> list[Path]:
    number = chapter_number(chapter_path)
    slug = chapter_path.stem
    build_dir = build_dir_base / f"chapter_{number}"
    build_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    qmd_path = build_dir / f"chapter_{number}_slides.qmd"
    qmd_path.write_text(
        bundle_slides(chapter_path, exercises_dir, subtitle, build_dir),
        encoding="utf-8",
    )

    html = render_revealjs(quarto, qmd_path, slug, output_dir)
    pptx = render_pptx(quarto, qmd_path, slug, output_dir)
    pdf = render_pdf(chrome, html, slug, output_dir)
    return [html, pptx, pdf]


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
        help="Subtitulo que se usara en las diapositivas.",
    )
    args = parser.parse_args()

    quarto = find_quarto()
    chrome = find_chrome()
    chapters_dir, exercises_dir, output_dir, build_dir_base = resolve_scope(args.book)
    outputs: list[Path] = []
    for path in chapter_paths(chapters_dir, args.chapter):
        outputs.extend(
            render_chapter(
                quarto,
                chrome,
                path,
                output_dir,
                build_dir_base,
                exercises_dir,
                args.subtitle,
            )
        )
    for output in outputs:
        print(output.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
