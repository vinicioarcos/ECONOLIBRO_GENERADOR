# econolab-computational-books

Sistema multiagente para planificar, escribir, revisar y publicar libros de
economia computacional con Python, notebooks reproducibles, datasets
documentados, ejercicios, rubricas y materiales editoriales.

Este repositorio organiza la **Serie Econolab Computacional** como un sistema
multi-libro. Cada libro puede tener capitulos, notebooks, ejercicios,
entregables PDF y diapositivas propias, reutilizando scripts, plantillas,
prompts y rubricas comunes.

## Primer libro piloto

**Economia Computacional con Python**  
**Datos, modelos y aplicaciones para estudiantes, docentes e investigadores en economia**

El objetivo del piloto es que el lector pueda importar, limpiar, analizar,
visualizar y modelar datos economicos con Python, usando ejemplos aplicados a
mercado laboral, educacion, pobreza, desigualdad, crecimiento y politica publica.

## Principios de trabajo

1. No inventar fuentes, autores, DOI ni resultados empiricos.
2. No afirmar causalidad sin una estrategia de identificacion.
3. No modificar `data/raw`.
4. Guardar datos derivados solo en `data/processed`.
5. Usar rutas relativas y codigo reproducible.
6. Todo capitulo debe tener resultados de aprendizaje.
7. Todo notebook debe ejecutarse de arriba hacia abajo.
8. Toda figura debe tener titulo, fuente e interpretacion.
9. Todo ejercicio debe tener solucion o guia docente.
10. Python debe servir a una pregunta economica, no decorar el texto.

## Estructura principal

- `books/`: libros independientes de la Serie Econolab Computacional.
- `book/`: archivos maestros del libro y configuracion editorial.
- `chapters/`: capitulos en Markdown.
- `notebooks/`: notebooks reproducibles por capitulo.
- `scripts/`: utilidades de descarga, limpieza, validacion y generacion.
- `data/`: datos originales, procesados, externos y diccionarios.
- `outputs/`: tablas, figuras, reportes, logs y versiones finales.
- `exercises/`: ejercicios, soluciones y notebooks docentes/estudiantes.
- `prompts/`: prompts de los 12 agentes.
- `workflows/`: flujos editoriales y computacionales.
- `templates/`: plantillas reutilizables.
- `rubrics/`: criterios de evaluacion.
- `examples/`: ejemplo piloto del primer libro.
- `publishing/`: preparacion Quarto, Jupyter Book, KDP y LMS.
- `docs/`: guias para autor, docente, estudiante, instalacion y publicacion.

## Arranque rapido

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/validate_reproducibility.py
```

## Flujo recomendado

1. Definir ficha editorial e indice maestro.
2. Crear matriz pedagogica y resultados por capitulo.
3. Identificar datos y referencias reales.
4. Escribir capitulo, notebook y ejercicios como un paquete.
5. Ejecutar validacion de reproducibilidad.
6. Revisar teoria, codigo, datos, visualizaciones y publicacion.

## PDF por capitulo con Quarto

Para generar un entregable PDF de un capitulo:

```powershell
python scripts/render_chapter_quarto.py --chapter 01
```

El PDF se guarda en `outputs/final/quarto`. Incluye el capitulo y, cuando
existan, los ejercicios del estudiante y la guia docente.

## Diapositivas por capitulo

Para generar diapositivas con Quarto en HTML, PowerPoint y PDF:

```powershell
python scripts/render_chapter_slides_quarto.py --chapter 01
```

Las presentaciones se guardan en `outputs/final/slides`.

## Estado del primer sprint

Este repositorio queda preparado para iniciar la escritura de la Serie Econolab
Computacional, comenzando por **Economia Computacional con Python**.

## Libros activos

- `books/econometria_financiera_python`: Econometria Financiera con Python,
  con datos financieros descargados desde internet, notebooks reproducibles,
  entregables PDF y diapositivas en HTML/PDF/PPTX.
