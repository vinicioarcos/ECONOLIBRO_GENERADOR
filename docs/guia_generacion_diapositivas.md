# Guia de generacion de diapositivas por capitulo

Cada capitulo puede producir una presentacion con Quarto en tres formatos:

- HTML navegable con RevealJS;
- PowerPoint editable (`.pptx`);
- PDF de diapositivas.

La presentacion resume:

- pregunta guia;
- resultados de aprendizaje;
- conceptos clave;
- intuicion economica;
- datos y trazabilidad;
- flujo en Python;
- interpretacion;
- errores frecuentes;
- actividad de clase;
- cierre.

## Generar diapositivas de un capitulo

```powershell
python scripts/render_chapter_slides_quarto.py --chapter 01
```

Para un libro dentro de `books/`:

```powershell
python scripts/render_chapter_slides_quarto.py --book econometria_financiera_python --subtitle "Econometria Financiera con Python" --chapter 01
```

Las salidas quedan en:

```text
books/economia_computacional_python/outputs/final/slides/
```

Ejemplo de archivos generados:

```text
01_introduccion_economia_computacional_slides.html
01_introduccion_economia_computacional_slides.pptx
01_introduccion_economia_computacional_slides.pdf
```

## Generar diapositivas de todos los capitulos

```powershell
python scripts/render_chapter_slides_quarto.py
```

## Uso docente

Estas diapositivas son materiales de clase. No reemplazan el capitulo escrito:
lo resumen para exposicion, discusion y actividades guiadas.
