"""Generate chapter deliverable PDFs without external dependencies.

The output is intentionally simple: readable text PDFs that bundle the chapter,
student exercises, and teacher guide when those files exist.
"""

from __future__ import annotations

import argparse
import re
import textwrap
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOOK = "economia_computacional_python"

PAGE_WIDTH = 595
PAGE_HEIGHT = 842
LEFT_MARGIN = 54
TOP_MARGIN = 56
LINE_HEIGHT = 13
BODY_FONT_SIZE = 10
TITLE_FONT_SIZE = 15
MAX_BODY_CHARS = 92


@dataclass
class Line:
    text: str
    font: str = "F1"
    size: int = BODY_FONT_SIZE
    leading: int = LINE_HEIGHT


def normalize_text(text: str) -> str:
    replacements = {
        "\u201c": '"',
        "\u201d": '"',
        "\u2018": "'",
        "\u2019": "'",
        "\u2013": "-",
        "\u2014": "-",
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def strip_markdown(line: str) -> tuple[str, str, int]:
    raw = line.rstrip()
    if not raw:
        return "", "F1", BODY_FONT_SIZE

    heading = re.match(r"^(#{1,6})\s+(.*)$", raw)
    if heading:
        level = len(heading.group(1))
        text = heading.group(2).strip()
        size = max(11, TITLE_FONT_SIZE - level + 1)
        return text, "F2", size

    raw = re.sub(r"^\s*[-*]\s+", "- ", raw)
    raw = re.sub(r"^\s*(\d+)\.\s+", r"\1. ", raw)
    raw = raw.replace("**", "").replace("__", "").replace("`", "")
    raw = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", raw)
    return raw, "F1", BODY_FONT_SIZE


def markdown_to_lines(markdown: str) -> list[Line]:
    lines: list[Line] = []
    in_code = False

    for original in normalize_text(markdown).splitlines():
        if original.strip().startswith("```"):
            in_code = not in_code
            lines.append(Line(""))
            continue

        if in_code:
            wrapped = textwrap.wrap(
                original,
                width=MAX_BODY_CHARS,
                replace_whitespace=False,
                drop_whitespace=False,
            ) or [""]
            lines.extend(Line(part, "F3", 9, 12) for part in wrapped)
            continue

        text, font, size = strip_markdown(original)
        if not text:
            lines.append(Line(""))
            continue

        width = 74 if font == "F2" and size >= 13 else MAX_BODY_CHARS
        wrapped = textwrap.wrap(text, width=width) or [""]
        lines.extend(Line(part, font, size) for part in wrapped)

    return lines


def read_if_exists(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def chapter_number(path: Path) -> str:
    match = re.match(r"^(\d{2})_", path.name)
    if not match:
        raise ValueError(f"No chapter number found in {path.name}")
    return match.group(1)


def build_deliverable_markdown(chapter_path: Path, exercises_dir: Path) -> str:
    number = chapter_number(chapter_path)
    exercise_dir = exercises_dir / f"chapter_{number}"
    parts = [read_if_exists(chapter_path)]

    exercises = read_if_exists(exercise_dir / "ejercicios.md")
    if exercises:
        parts.append("\\newpage\n# Anexo A. Ejercicios del estudiante\n" + exercises)

    teacher_guide = read_if_exists(exercise_dir / "soluciones_docente.md")
    if teacher_guide:
        parts.append("\\newpage\n# Anexo B. Guia docente\n" + teacher_guide)

    return "\n\n".join(parts)


def escape_pdf_text(text: str) -> str:
    encoded = text.encode("latin-1", errors="replace").decode("latin-1")
    return encoded.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def paginate(lines: list[Line]) -> list[list[Line]]:
    pages: list[list[Line]] = [[]]
    y = TOP_MARGIN

    for line in lines:
        if line.text == "\\newpage":
            pages.append([])
            y = TOP_MARGIN
            continue

        if y + line.leading > PAGE_HEIGHT - TOP_MARGIN:
            pages.append([])
            y = TOP_MARGIN

        pages[-1].append(line)
        y += line.leading

    return pages


def page_stream(lines: list[Line], page_number: int) -> bytes:
    commands = ["BT"]
    y = PAGE_HEIGHT - TOP_MARGIN

    for line in lines:
        if not line.text:
            y -= line.leading
            continue
        commands.append(f"/{line.font} {line.size} Tf")
        commands.append(f"{LEFT_MARGIN} {y} Td")
        commands.append(f"({escape_pdf_text(line.text)}) Tj")
        commands.append(f"{-LEFT_MARGIN} {-line.leading} Td")
        y -= line.leading

    commands.append("/F1 8 Tf")
    commands.append(f"{PAGE_WIDTH - 92} 28 Td")
    commands.append(f"(Pagina {page_number}) Tj")
    commands.append("ET")
    return ("\n".join(commands) + "\n").encode("latin-1", errors="replace")


def write_pdf(lines: list[Line], output_path: Path) -> None:
    pages = paginate(lines)
    objects: list[bytes] = []

    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    kids = " ".join(f"{3 + index * 2} 0 R" for index in range(len(pages)))
    objects.append(f"<< /Type /Pages /Kids [{kids}] /Count {len(pages)} >>".encode())

    font_object_numbers = {
        "F1": 3 + len(pages) * 2,
        "F2": 4 + len(pages) * 2,
        "F3": 5 + len(pages) * 2,
    }

    for index, page_lines in enumerate(pages):
        page_obj = 3 + index * 2
        content_obj = page_obj + 1
        resources = (
            "<< /Font << "
            f"/F1 {font_object_numbers['F1']} 0 R "
            f"/F2 {font_object_numbers['F2']} 0 R "
            f"/F3 {font_object_numbers['F3']} 0 R "
            ">> >>"
        )
        page = (
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PAGE_WIDTH} {PAGE_HEIGHT}] "
            f"/Resources {resources} /Contents {content_obj} 0 R >>"
        )
        objects.append(page.encode())

        stream = page_stream(page_lines, index + 1)
        content = b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n"
        content += stream + b"endstream"
        objects.append(content)

    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier >>")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("wb") as file:
        file.write(b"%PDF-1.4\n")
        offsets = [0]
        for object_number, obj in enumerate(objects, start=1):
            offsets.append(file.tell())
            file.write(f"{object_number} 0 obj\n".encode())
            file.write(obj)
            file.write(b"\nendobj\n")
        xref_start = file.tell()
        file.write(f"xref\n0 {len(objects) + 1}\n".encode())
        file.write(b"0000000000 65535 f \n")
        for offset in offsets[1:]:
            file.write(f"{offset:010d} 00000 n \n".encode())
        trailer = f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
        file.write(trailer.encode())
        file.write(f"startxref\n{xref_start}\n%%EOF\n".encode())


def chapter_paths(chapters_dir: Path, selected: str | None) -> list[Path]:
    if selected:
        normalized = selected.zfill(2)
        matches = sorted(chapters_dir.glob(f"{normalized}_*.md"))
        if not matches:
            raise FileNotFoundError(f"No se encontro capitulo {normalized}")
        return matches
    return sorted(chapters_dir.glob("[0-9][0-9]_*.md"))


def generate(selected: str | None, book: str) -> list[Path]:
    book_root = ROOT / "books" / book
    chapters_dir = book_root / "chapters"
    exercises_dir = book_root / "exercises"
    output_dir = book_root / "outputs" / "final"
    outputs: list[Path] = []
    for chapter_path in chapter_paths(chapters_dir, selected):
        number = chapter_number(chapter_path)
        markdown = build_deliverable_markdown(chapter_path, exercises_dir)
        lines = markdown_to_lines(markdown.replace("\\newpage", "\n\\newpage\n"))
        output_path = output_dir / f"chapter_{number}_entregable.pdf"
        write_pdf(lines, output_path)
        outputs.append(output_path)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--chapter",
        help="Chapter number to generate, for example 01 or 2. Omit to generate all.",
    )
    parser.add_argument(
        "--book",
        default=DEFAULT_BOOK,
        help="Slug del libro dentro de books/.",
    )
    args = parser.parse_args()

    outputs = generate(args.chapter, args.book)
    for path in outputs:
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
