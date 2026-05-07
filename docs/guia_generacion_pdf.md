# Guia de generacion de PDF por capitulo con Quarto

Cada capitulo puede producirse como un entregable PDF independiente. El PDF
incluye:

- texto del capitulo en `chapters`;
- ejercicios del estudiante, si existen;
- guia docente, si existe.

La ruta recomendada usa Quarto con el motor Typst, por lo que no requiere
TinyTeX ni LaTeX.

## Generar un capitulo

```powershell
python scripts/render_chapter_quarto.py --chapter 01
```

El archivo queda en:

```text
books/economia_computacional_python/outputs/final/quarto/
```

## Generar todos los capitulos

```powershell
python scripts/render_chapter_quarto.py
```

## Criterio editorial

Estos PDFs son entregables de trabajo. Sirven para revisar, compartir o imprimir
capitulos mientras el libro completo sigue creciendo. Para publicacion final se
mantiene la ruta Quarto/Jupyter Book definida en `publishing`.

## Respaldo sin Quarto

Existe `scripts/generate_chapter_pdfs.py` como respaldo tecnico sin
dependencias externas. Su salida es simple y no reemplaza la version editorial
generada con Quarto.
