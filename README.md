# Econolab Computational Books

![License](https://img.shields.io/github/license/vinicioarcos/econolab-computational-books)
![Last Commit](https://img.shields.io/github/last-commit/vinicioarcos/econolab-computational-books)
![Repo Size](https://img.shields.io/github/repo-size/vinicioarcos/econolab-computational-books)
![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)
![Quarto](https://img.shields.io/badge/quarto-publishing-blue?logo=quarto&logoColor=white)
![Jupyter](https://img.shields.io/badge/jupyter-notebooks-orange?logo=jupyter&logoColor=white)
![Made with Claude](https://img.shields.io/badge/made%20with-Claude-blueviolet?logo=anthropic&logoColor=white)

Sistema multiagente para planificar, escribir, revisar y publicar libros de
economia computacional con Python. Organiza la **Serie Econolab Computacional**
como un sistema multi-libro: cada libro tiene capitulos, notebooks, ejercicios,
entregables PDF y diapositivas propias, reutilizando scripts, plantillas,
prompts y rubricas comunes.

---

## Serie Econolab Computacional

| Libro | Estado | Descripcion |
|---|---|---|
| [Economia Computacional con Python](chapters/) | En progreso (30 caps.) | Datos, modelos y aplicaciones para estudiantes, docentes e investigadores |
| [Econometria Financiera con Python](books/econometria_financiera_python/) | En progreso (2 caps.) | Precios, retornos, volatilidad, riesgo y portafolios con Python |

---

## Estructura del repositorio

```
econolab-computational-books/
├── books/                        # Libros independientes de la serie
│   └── econometria_financiera_python/
├── book/                         # Archivos maestros y configuracion editorial
├── chapters/                     # 30 capitulos en Markdown
├── notebooks/                    # Notebooks reproducibles por capitulo
├── exercises/                    # Ejercicios, soluciones y notebooks docentes
├── scripts/                      # Descarga, limpieza, validacion y generacion
├── data/
│   ├── raw/                      # Datos originales (no modificar)
│   ├── processed/                # Datos derivados
│   ├── external/                 # Fuentes externas
│   └── dictionary/               # Diccionarios de variables
├── outputs/
│   ├── figures/                  # Graficos generados
│   ├── tables/                   # Tablas generadas
│   ├── reports/                  # Reportes intermedios
│   └── final/                    # PDFs, slides y versiones finales
├── prompts/                      # Prompts de los 12 agentes editoriales
├── workflows/                    # Flujos editoriales y computacionales
├── templates/                    # Plantillas reutilizables
├── rubrics/                      # Criterios de evaluacion
├── publishing/                   # Configuracion Quarto, Jupyter Book, KDP, LMS
├── docs/                         # Guias para autor, docente, estudiante
├── skills/                       # Claude Skills del proyecto
└── examples/                     # Ejemplo piloto
```

---

## Arranque rapido

**Requisitos:** Python 3.10+, [Quarto](https://quarto.org/docs/get-started/)

```bash
# Crear entorno virtual e instalar dependencias
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
.\.venv\Scripts\Activate.ps1     # Windows

pip install -r requirements.txt

# Verificar que el entorno es reproducible
python scripts/validate_reproducibility.py
```

### Dependencias principales

| Categoria | Paquetes |
|---|---|
| Datos y analisis | `pandas`, `numpy`, `scipy`, `statsmodels`, `linearmodels` |
| Machine learning | `scikit-learn` |
| Visualizacion | `matplotlib`, `plotly` |
| Datos financieros | `yfinance`, `pandas-datareader` |
| Notebooks | `jupyter`, `jupyterlab`, `nbformat`, `nbconvert` |
| Publicacion | `quarto` |
| Calidad de codigo | `black`, `ruff`, `pytest` |

---

## Generar entregables

### PDF de un capitulo

```bash
python scripts/render_chapter_quarto.py --chapter 01
# Salida: outputs/final/quarto/
```

### Diapositivas de un capitulo (HTML, PDF, PowerPoint)

```bash
python scripts/render_chapter_slides_quarto.py --chapter 01
# Salida: outputs/final/slides/
```

### PDF de todos los capitulos

```bash
python scripts/generate_chapter_pdfs.py
```

---

## Flujo editorial recomendado

```
1. Ficha editorial + indice maestro
        ↓
2. Matriz pedagogica + resultados de aprendizaje
        ↓
3. Identificar datasets y referencias reales
        ↓
4. Escribir capitulo + notebook + ejercicios (como un paquete)
        ↓
5. Ejecutar validate_reproducibility.py
        ↓
6. Revision tecnica (teoria, codigo, datos, figuras, publicacion)
        ↓
7. Generar PDF + slides + version LMS
```

Los 9 workflows detallados estan en [`workflows/`](workflows/).

---

## Principios de trabajo

1. No inventar fuentes, autores, DOI ni resultados empiricos.
2. No afirmar causalidad sin una estrategia de identificacion.
3. No modificar `data/raw/` — solo leer.
4. Guardar datos derivados solo en `data/processed/`.
5. Usar rutas relativas y codigo reproducible.
6. Todo capitulo debe tener resultados de aprendizaje explícitos.
7. Todo notebook debe ejecutarse de arriba hacia abajo sin errores.
8. Toda figura debe tener titulo, fuente e interpretacion.
9. Todo ejercicio debe tener solucion o guia docente.
10. Python debe servir a una pregunta economica, no decorar el texto.

---

## Agentes del sistema

El repositorio incluye 12 prompts de agentes editoriales especializados
en [`prompts/`](prompts/):

| # | Agente | Rol |
|---|---|---|
| 01 | Arquitecto editorial | Estructura, indice y coherencia del libro |
| 02 | Disenador pedagogico | Resultados de aprendizaje y matriz pedagogica |
| 03 | Investigador bibliografico | Fuentes, referencias y estado del arte |
| 04 | Economista teorico aplicado | Marco teorico y rigor conceptual |
| 05 | Datos economicos | Identificacion y documentacion de datasets |
| 06 | Programador Python | Codigo limpio, reproducible y bien documentado |
| 07 | Econometrista computacional | Modelos econometricos y validacion |
| 08 | Cientifico de datos | ML aplicado a economia |
| 09 | Visualizador y storyteller | Figuras, tablas e interpretacion narrativa |
| 10 | Ejercicios y evaluaciones | Ejercicios, soluciones y rubricas |
| 11 | Revisor tecnico academico | Control de calidad integral |
| 12 | Editor y publicador | Formatos finales y distribucion |

---

## Roadmap

Ver [`ROADMAP.md`](ROADMAP.md) para el detalle completo.

| Fase | Descripcion | Estado |
|---|---|---|
| 1 | Diseno editorial | Completado |
| 2 | Diseno pedagogico | Completado |
| 3 | Infraestructura computacional | Completado |
| 4 | Datos | En progreso |
| 5 | Escritura de capitulos | En progreso |
| 6 | Revision tecnica | Pendiente |
| 7 | Publicacion | Pendiente |
| 8 | Escalamiento de la serie | Pendiente |

---

## Licencia

[MIT](LICENSE)
