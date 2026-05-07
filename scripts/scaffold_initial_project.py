"""Create the initial ECONOLIBRO-CODEX project scaffold.

This script is intentionally conservative: it writes starter files with useful
content and does not touch PROJECT_BRIEF.md or any files under data/raw.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BOOK_ROOT = "books/economia_computacional_python"
BOOK_SPECIFIC_PREFIXES = (
    "book/",
    "chapters/",
    "notebooks/",
    "exercises/",
    "data/",
    "outputs/",
)


def scoped_path(path: str) -> str:
    normalized = path.replace("\\", "/")
    if normalized.startswith(BOOK_SPECIFIC_PREFIXES):
        return f"{DEFAULT_BOOK_ROOT}/{normalized}"
    return path


def write(path: str, content: str) -> None:
    target = ROOT / scoped_path(path)
    if "data/raw" in target.as_posix():
        raise ValueError("Refusing to write inside data/raw")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.strip() + "\n", encoding="utf-8")


def touch(path: str) -> None:
    target = ROOT / scoped_path(path)
    if "data/raw" in target.as_posix() and target.name != ".gitkeep":
        raise ValueError("Refusing to write inside data/raw")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.touch(exist_ok=True)


README = """
# ECONOLIBRO-CODEX

Sistema multiagente para planificar, escribir, revisar y publicar libros de
economia computacional con Python, notebooks reproducibles, datasets
documentados, ejercicios, rubricas y materiales editoriales.

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
.\\.venv\\Scripts\\Activate.ps1
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

## Estado del primer sprint

Este repositorio queda preparado para iniciar la escritura de la Serie Econolab
Computacional, comenzando por **Economia Computacional con Python**.
"""


AGENTS = """
# AGENTS.md

## Proyecto

ECONOLIBRO-CODEX: Sistema Multiagente para Escritura de Libros de Economia
Computacional con Python.

## Descripcion

Este proyecto implementa una arquitectura multiagente para planificar, escribir,
revisar y publicar libros academicos y aplicados de economia con enfasis
computacional.

El sistema produce capitulos, notebooks, scripts, ejercicios, datasets
documentados, figuras, tablas, rubricas y materiales complementarios para
docencia, investigacion y publicacion.

## Regla general

Cada agente debe producir entregables verificables. No se aceptan respuestas
genericas, texto de relleno ni codigo decorativo.

## Agentes

### 1. Agente arquitecto editorial

Convierte una idea de libro en una propuesta editorial. Define titulo,
subtitulo, publico objetivo, nivel, indice maestro, estructura por partes, estilo
y formato de publicacion.

### 2. Agente disenador pedagogico

Define resultados de aprendizaje, competencias, actividades, ejercicios,
rubricas y estructura didactica por capitulo.

### 3. Agente investigador bibliografico

Busca y organiza literatura academica, libros, articulos, documentacion tecnica
y fuentes de datos para sustentar cada capitulo.

### 4. Agente economista teorico-aplicado

Conecta los capitulos con teoria economica, mecanismos, intuicion, contexto
institucional y aplicaciones reales.

### 5. Agente de datos economicos

Identifica, descarga, documenta, limpia y valida bases economicas. Mantiene
intacta `data/raw` y guarda transformaciones en `data/processed`.

### 6. Agente programador Python

Implementa notebooks, scripts, funciones, tablas y graficos reproducibles. Todo
codigo debe ser claro, didactico y ejecutable.

### 7. Agente econometrista computacional

Disena y explica modelos econometricos implementados en Python, sus supuestos,
interpretacion y limites.

### 8. Agente cientifico de datos

Desarrolla analisis exploratorio, modelos predictivos, validacion,
segmentacion e interpretabilidad aplicada a problemas economicos.

### 9. Agente visualizador y storyteller de datos

Produce graficos, tablas, diagramas y narrativas visuales claras para ensenar y
comunicar resultados economicos.

### 10. Agente generador de ejercicios y evaluaciones

Crea ejercicios conceptuales, computacionales, mini-proyectos, soluciones
docentes, rubricas y bancos de preguntas.

### 11. Agente revisor tecnico-academico

Evalua rigor economico, claridad pedagogica, calidad del codigo,
reproducibilidad, consistencia de datos y coherencia editorial.

### 12. Agente editor final y publicador

Prepara el libro para publicacion en Markdown, Quarto, Jupyter Book, LaTeX, PDF,
EPUB, HTML, Amazon KDP, LMS o GitHub Pages.

## Reglas obligatorias

1. No inventar fuentes.
2. No inventar autores.
3. No inventar DOI.
4. No inventar resultados.
5. No afirmar causalidad sin identificacion.
6. No modificar `data/raw`.
7. No usar rutas absolutas.
8. No entregar codigo que dependa del computador del autor.
9. No incluir graficos sin interpretacion.
10. No crear ejercicios sin solucion o guia.
11. No usar machine learning como reemplazo de teoria economica.
12. No mezclar datos originales con datos procesados.
13. No usar citas decorativas.
14. No entregar capitulos sin resultados de aprendizaje.
15. No entregar notebooks que no puedan ejecutarse de arriba hacia abajo.

## Formato de respuesta obligatorio para cada agente

Cada agente debe responder con:

1. Diagnostico.
2. Producto generado.
3. Justificacion.
4. Riesgos o limitaciones.
5. Proximo paso.
"""


ROADMAP = """
# ROADMAP.md

## Fase 1. Diseno editorial

- Definir titulo del libro.
- Definir publico objetivo.
- Definir nivel.
- Definir indice maestro.
- Definir estilo editorial.
- Definir formato de publicacion.

## Fase 2. Diseno pedagogico

- Crear resultados de aprendizaje.
- Crear matriz pedagogica.
- Definir ejercicios por capitulo.
- Definir rubricas.
- Definir guia docente y guia del estudiante.

## Fase 3. Infraestructura computacional

- Crear entorno Python.
- Crear `requirements.txt`.
- Crear notebooks base.
- Crear scripts de datos.
- Crear estructura reproducible.
- Crear guia de instalacion.

## Fase 4. Datos

- Identificar datasets.
- Descargar datos.
- Crear diccionario de datos.
- Crear cleaning log.
- Crear bases procesadas.
- Validar calidad.

## Fase 5. Escritura de capitulos

- Redactar capitulos en Markdown.
- Integrar teoria.
- Integrar ejemplos Python.
- Integrar figuras.
- Integrar ejercicios.
- Integrar referencias.

## Fase 6. Revision tecnica

- Revisar teoria.
- Revisar codigo.
- Revisar notebooks.
- Revisar datos.
- Revisar ejercicios.
- Revisar reproducibilidad.

## Fase 7. Publicacion

- Preparar version Quarto.
- Preparar version Jupyter Book.
- Preparar version PDF.
- Preparar version EPUB.
- Preparar version LMS.
- Preparar version KDP, si aplica.

## Fase 8. Escalamiento

- Crear mas libros.
- Crear biblioteca Econolab.
- Crear cursos asociados.
- Integrar con LMS.
- Crear Claude Skills.
- Automatizar con LangGraph.
"""


ROOT_FILES = {
    "README.md": README,
    "AGENTS.md": AGENTS,
    "ROADMAP.md": ROADMAP,
    "LICENSE": """
MIT License

Copyright (c) 2026 Econolab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",
    ".gitignore": """
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
.env
.venv
venv/
env/

# Jupyter
.ipynb_checkpoints/

# Quarto / Jupyter Book builds
_book/
_site/
.quarto/
_build/

# Data
/data/raw/*
/data/processed/*
/data/external/*
!/data/raw/.gitkeep
!/data/processed/.gitkeep
!/data/external/.gitkeep

# Outputs
/outputs/tables/*
/outputs/figures/*
/outputs/reports/*
/outputs/logs/*
/outputs/final/*
!/outputs/tables/.gitkeep
!/outputs/figures/.gitkeep
!/outputs/reports/.gitkeep
!/outputs/logs/.gitkeep
!/outputs/final/.gitkeep

# OS
.DS_Store
Thumbs.db

# Editors
.vscode/

# Secrets
*.key
*.pem
secrets.*
.env.local

# Large local files
*.zip
*.rar
*.7z
*.tar
*.gz
*.parquet
*.dta
*.sav
*.xlsx
*.csv
""",
    "requirements.txt": """
pandas
numpy
scipy
statsmodels
linearmodels
scikit-learn
matplotlib
plotly
pyreadstat
openpyxl
jupyter
jupyterlab
nbformat
nbconvert
black
ruff
pytest
""",
    "environment.yml": """
name: econolibro-codex
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - pandas
  - numpy
  - scipy
  - statsmodels
  - linearmodels
  - scikit-learn
  - matplotlib
  - plotly
  - openpyxl
  - jupyterlab
  - nbconvert
  - pip
  - pip:
      - pyreadstat
      - black
      - ruff
      - pytest
""",
    "pyproject.toml": """
[project]
name = "econolibro-codex"
version = "0.1.0"
description = "Sistema multiagente para escritura de libros de economia computacional con Python."
authors = [
    { name = "Econolab" }
]
requires-python = ">=3.11"
dependencies = []

[tool.black]
line-length = 88
target-version = ["py311"]

[tool.ruff]
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "I", "B"]
ignore = []
""",
}


BOOK_FILES = {
    "book/index.md": """
# Economia Computacional con Python

Datos, modelos y aplicaciones para estudiantes, docentes e investigadores en
economia.

## Proposito

Este libro ensena a trabajar preguntas economicas con Python de manera
reproducible. La prioridad es unir teoria economica, datos reales, codigo claro,
visualizaciones interpretables y ejercicios con solucion docente.

## Publico objetivo

- Estudiantes de economia y administracion.
- Docentes universitarios.
- Tesistas e investigadores iniciales.
- Analistas de datos economicos.
- Profesionales del sector publico.

## Estructura

El libro avanza desde fundamentos de Python y datos economicos hasta
visualizacion, estadistica, econometria introductoria, ciencia de datos y
aplicaciones de politica publica.
""",
    "book/preface.md": """
# Prefacio

Este libro nace para reducir la distancia entre aprender economia y practicar
economia con datos. Cada capitulo debe responder una pregunta economica,
mostrar un flujo computacional reproducible y cerrar con ejercicios que ayuden a
transferir lo aprendido.

La regla editorial es simple: no hay codigo sin proposito economico, no hay
resultados sin interpretacion y no hay datos sin trazabilidad.
""",
    "book/introduction.md": """
# Introduccion

La economia computacional combina intuicion economica, datos, modelos y
programacion. Python permite construir flujos reproducibles para importar,
limpiar, analizar, visualizar y modelar informacion economica.

Este libro usa una progresion inicial-intermedia: primero entorno y Python,
luego datos, visualizacion y estadistica, despues econometria y ciencia de
datos, y finalmente aplicaciones sobre problemas reales.
""",
    "book/glossary.md": """
# Glosario inicial

- **Dato crudo**: archivo original sin transformaciones del proyecto.
- **Dato procesado**: dato derivado por scripts documentados.
- **Notebook reproducible**: notebook que se ejecuta completo de arriba abajo.
- **Inferencia causal**: afirmacion causal respaldada por una estrategia de
  identificacion explicita.
- **Variable**: caracteristica observada o construida para una unidad de
  analisis.
""",
    "book/author_bio.md": """
# Biografia del autor

Pendiente de completar por el equipo editorial. Debe incluir filiacion,
experiencia docente, lineas de investigacion y una declaracion breve sobre el
proposito pedagogico de la Serie Econolab Computacional.
""",
    "book/acknowledgements.md": """
# Agradecimientos

Pendiente de completar. Registrar aqui instituciones, equipos docentes,
estudiantes, revisores y comunidades de software libre que contribuyan al libro.
No incluir nombres sin autorizacion.
""",
    "book/references.bib": """
% Archivo BibTeX del libro.
% Regla: no agregar referencias sin verificar autores, titulo, ano, editorial o DOI.
""",
    "book/_toc.yml": """
format: jb-book
root: index
parts:
  - caption: Fundamentos
    chapters:
      - file: ../chapters/01_introduccion_economia_computacional
      - file: ../chapters/02_instalacion_entorno
      - file: ../chapters/03_python_para_economistas
  - caption: Datos economicos
    chapters:
      - file: ../chapters/05_fuentes_datos_economicos
      - file: ../chapters/06_limpieza_pandas
  - caption: Proyecto final
    chapters:
      - file: ../chapters/29_proyecto_reproducible
      - file: ../chapters/30_proyecto_final
""",
}


CHAPTER_TEMPLATE = """
# Capitulo {number}. {title}

## 1. Apertura

### Pregunta motivadora

Que problema economico queremos entender en este capitulo?

### Caso aplicado

Caso pendiente de seleccionar con datos reales de Ecuador, America Latina o una
fuente internacional verificada.

### Por que importa

El capitulo debe explicar la relevancia economica, social, empresarial o de
politica publica del tema.

## 2. Resultados de aprendizaje

Al finalizar este capitulo, el lector sera capaz de:

1. Explicar el problema economico central.
2. Identificar los datos necesarios para analizarlo.
3. Implementar un flujo basico en Python.
4. Interpretar resultados sin sobreafirmar causalidad.

## 3. Conceptos clave

- Concepto economico principal.
- Variable o medida clave.
- Metodo computacional usado.

## 4. Intuicion economica

Desarrollar aqui la explicacion conceptual sin codigo.

## 5. Formalizacion minima

Incluir ecuacion, identidad, modelo o estructura analitica solo si ayuda al
aprendizaje.

## 6. Datos

Registrar fuente, variables, muestra, periodo y advertencias. No inventar datos
ni referencias.

## 7. Implementacion en Python

El notebook asociado debe vivir en `notebooks/chapter_{number}/` y ejecutarse de
arriba hacia abajo.

## 8. Resultados

Agregar tablas, figuras y salidas principales generadas por scripts o notebooks.

## 9. Interpretacion economica

Explicar que significan los resultados y que no se puede concluir.

## 10. Errores frecuentes

- Confundir correlacion con causalidad.
- Usar rutas absolutas.
- Presentar una figura sin fuente e interpretacion.

## 11. Ejercicios

Ver carpeta `exercises/chapter_{number}/`.

## 12. Mini-proyecto

Proponer una actividad aplicada con datos documentados.

## 13. Lecturas recomendadas

Agregar solo lecturas verificadas.

## 14. Resumen del capitulo

Sintetizar las ideas centrales cuando el capitulo sea desarrollado.

## 15. Checklist de aprendizaje

- [ ] Puedo explicar la pregunta economica.
- [ ] Puedo ejecutar el notebook del capitulo.
- [ ] Puedo interpretar los resultados con cautela.
"""


CHAPTERS = [
    ("00_prefacio.md", "00", "Prefacio"),
    ("01_introduccion_economia_computacional.md", "01", "Que es la economia computacional?"),
    ("02_instalacion_entorno.md", "02", "Instalacion, Google Colab y entorno de trabajo"),
    ("03_python_para_economistas.md", "03", "Python basico para economistas"),
    ("04_pensamiento_computacional.md", "04", "Pensamiento computacional aplicado a problemas economicos"),
    ("05_fuentes_datos_economicos.md", "05", "Fuentes de datos economicos"),
    ("06_limpieza_pandas.md", "06", "Limpieza de datos con Pandas"),
    ("07_transformacion_variables.md", "07", "Transformacion y construccion de variables"),
    ("08_tablas_estadisticas.md", "08", "Tablas estadisticas para analisis economico"),
    ("09_visualizacion_economica.md", "09", "Visualizacion de datos economicos"),
    ("10_estadistica_descriptiva.md", "10", "Estadistica descriptiva computacional"),
    ("11_inferencia_basica.md", "11", "Distribuciones, muestreo e inferencia basica"),
    ("12_regresion_lineal_simple.md", "12", "Regresion lineal simple"),
    ("13_regresion_multiple.md", "13", "Regresion multiple"),
    ("14_dummy_interacciones.md", "14", "Variables dummy e interacciones"),
    ("15_heterocedasticidad_errores_robustos.md", "15", "Heterocedasticidad y errores robustos"),
    ("16_logit_probit.md", "16", "Modelos logit y probit"),
    ("17_datos_panel.md", "17", "Introduccion a datos de panel"),
    ("18_series_tiempo.md", "18", "Introduccion a series de tiempo"),
    ("19_eda_avanzado.md", "19", "Analisis exploratorio avanzado"),
    ("20_machine_learning_economia.md", "20", "Introduccion a machine learning para economia"),
    ("21_clasificacion_prediccion.md", "21", "Clasificacion y prediccion economica"),
    ("22_clustering_segmentacion.md", "22", "Clustering y segmentacion economica"),
    ("23_interpretabilidad_modelos.md", "23", "Interpretabilidad de modelos"),
    ("24_mercado_laboral_enemdu.md", "24", "Mercado laboral con ENEMDU"),
    ("25_educacion_ingresos.md", "25", "Educacion e ingresos"),
    ("26_pobreza_desigualdad.md", "26", "Pobreza y desigualdad"),
    ("27_inflacion_series_macro.md", "27", "Inflacion y series macroeconomicas"),
    ("28_politica_publica_datos.md", "28", "Politica publica basada en datos"),
    ("29_proyecto_reproducible.md", "29", "Como construir un proyecto reproducible"),
    ("30_proyecto_final.md", "30", "Proyecto final aplicado"),
]


PROMPTS = {
    "01_arquitecto_editorial.md": "Agente arquitecto editorial",
    "02_disenador_pedagogico.md": "Agente disenador pedagogico",
    "03_investigador_bibliografico.md": "Agente investigador bibliografico",
    "04_economista_teorico_aplicado.md": "Agente economista teorico-aplicado",
    "05_datos_economicos.md": "Agente de datos economicos",
    "06_programador_python.md": "Agente programador Python",
    "07_econometrista_computacional.md": "Agente econometrista computacional",
    "08_cientifico_datos.md": "Agente cientifico de datos",
    "09_visualizador_storyteller.md": "Agente visualizador y storyteller de datos",
    "10_ejercicios_evaluaciones.md": "Agente generador de ejercicios y evaluaciones",
    "11_revisor_tecnico_academico.md": "Agente revisor tecnico-academico",
    "12_editor_publicador.md": "Agente editor final y publicador",
}


def prompt_content(agent: str) -> str:
    return f"""
# {agent}

## Rol

Actuas como {agent.lower()} del proyecto ECONOLIBRO-CODEX.

## Mision

Producir entregables verificables para libros de economia computacional con
Python, respetando rigor academico, reproducibilidad y utilidad docente.

## Entradas minimas

- Nombre del libro o capitulo.
- Publico objetivo.
- Nivel esperado.
- Pregunta economica o producto requerido.
- Restricciones de datos, codigo y publicacion.

## Reglas

1. No inventar fuentes, autores, DOI ni resultados.
2. No afirmar causalidad sin identificacion.
3. Usar rutas relativas cuando haya codigo.
4. Separar teoria, datos, codigo, resultados y ejercicios.
5. Declarar limitaciones y proximo paso.

## Formato de salida

1. Diagnostico.
2. Producto generado.
3. Justificacion.
4. Riesgos o limitaciones.
5. Proximo paso.
"""


WORKFLOWS = {
    "01_idea_a_indice.md": "Convertir una idea de libro en ficha editorial, promesa de aprendizaje e indice maestro.",
    "02_capitulo_completo.md": "Crear un capitulo con teoria, datos, codigo, resultados, ejercicios y checklist.",
    "03_dataset_a_notebook.md": "Transformar un dataset documentado en notebook reproducible sin tocar data/raw.",
    "04_revision_reproducibilidad.md": "Ejecutar controles de rutas, notebooks, outputs y dependencias.",
    "05_revision_bibliografica.md": "Verificar que referencias, fuentes y DOI existan antes de incluirlos.",
    "06_figuras_tablas.md": "Generar figuras y tablas con titulo, fuente, notas e interpretacion.",
    "07_ejercicios_soluciones.md": "Crear ejercicios alineados con resultados de aprendizaje y solucion docente.",
    "08_publicacion_multiformato.md": "Preparar salida Markdown, Quarto, Jupyter Book, PDF, EPUB, LMS y KDP.",
    "09_escalamiento_serie.md": "Escalar desde el libro piloto hacia la Serie Econolab Computacional.",
}


TEMPLATES = {
    "plantilla_capitulo.md": "Estructura obligatoria para cada capitulo con apertura, resultados, datos, codigo, interpretacion, ejercicios y checklist.",
    "plantilla_notebook.md": "Guion de notebook reproducible: objetivo economico, imports, datos, limpieza, analisis, visualizacion, interpretacion y cierre.",
    "plantilla_ejercicios.md": "Formato para ejercicios conceptuales, computacionales, mini-proyecto y solucion docente.",
    "plantilla_dataset.md": "Ficha de dataset con fuente, enlace, periodo, unidad, variables, licencia y advertencias.",
    "plantilla_diccionario_variables.md": "Diccionario de variables con nombre, etiqueta, tipo, unidad, valores y transformaciones.",
    "plantilla_cleaning_log.md": "Registro de decisiones de limpieza, filtros, imputaciones y validaciones.",
    "plantilla_figura.md": "Ficha de figura con pregunta, datos, titulo, fuente, interpretacion y archivo generado.",
    "plantilla_tabla.md": "Ficha de tabla con poblacion, variables, notas, fuente e interpretacion.",
    "plantilla_ficha_editorial.md": "Ficha de libro: titulo, subtitulo, publico, nivel, promesa, estructura y formatos.",
    "plantilla_matriz_pedagogica.md": "Matriz por capitulo: resultados, conceptos, actividades, evaluacion y evidencia.",
    "plantilla_bibliografia.md": "Ficha bibliografica para referencias verificadas sin citas decorativas.",
    "plantilla_modelo_econometrico.md": "Ficha de modelo con especificacion, supuestos, interpretacion y limites causales.",
    "plantilla_revision_tecnica.md": "Informe de revision tecnica con hallazgos, severidad, evidencia y correccion sugerida.",
    "plantilla_publicacion.md": "Checklist editorial para Quarto, Jupyter Book, PDF, EPUB, LMS y KDP.",
    "plantilla_guia_docente.md": "Guia docente por capitulo con objetivos, tiempos, actividades y solucion orientativa.",
    "checklist_libro.md": "Checklist integral antes de publicar el libro.",
}


RUBRICS = {
    "rubrica_capitulo.md": "Evalua estructura, aprendizaje, rigor economico, claridad y cierre pedagogico.",
    "rubrica_notebook.md": "Evalua ejecucion completa, rutas relativas, limpieza, analisis e interpretacion.",
    "rubrica_codigo_python.md": "Evalua legibilidad, modularidad, dependencias, errores y proposito economico.",
    "rubrica_dataset.md": "Evalua trazabilidad, metadatos, diccionario, calidad y separacion raw/processed.",
    "rubrica_figuras.md": "Evalua titulo, fuente, legibilidad, eleccion visual e interpretacion.",
    "rubrica_tablas.md": "Evalua notas, formato, precision, comparabilidad e interpretacion.",
    "rubrica_ejercicios.md": "Evalua alineacion, dificultad, solucion, retroalimentacion y mini-proyecto.",
    "rubrica_bibliografia.md": "Evalua verificacion, pertinencia, actualidad y ausencia de referencias inventadas.",
    "rubrica_econometria.md": "Evalua especificacion, supuestos, inferencia, robustez y cautela causal.",
    "rubrica_publicacion.md": "Evalua consistencia editorial, metadatos, formatos y preparacion multicanal.",
}


DOCS = {
    "docs/guia_autor.md": "Guia para autores: escribir desde preguntas economicas, documentar datos, explicar codigo y cerrar con ejercicios verificables.",
    "docs/guia_docente.md": "Guia docente: usar capitulos como unidades de clase, asignar notebooks, revisar mini-proyectos y aplicar rubricas.",
    "docs/guia_estudiante.md": "Guia del estudiante: preparar entorno, ejecutar notebooks, registrar dudas, entregar ejercicios y evitar copiar resultados sin interpretacion.",
    "docs/guia_instalacion.md": "Guia de instalacion: crear entorno, instalar dependencias, ejecutar validacion y trabajar con rutas relativas.",
    "docs/guia_publicacion.md": "Guia de publicacion: revisar manuscrito, referencias, figuras, tablas, notebooks y salidas Quarto/Jupyter Book antes de publicar.",
}


SCRIPT_FILES = {
    "scripts/download_data.py": """
from pathlib import Path


RAW_DIR = Path("data/raw")


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print("Descarga pendiente: registrar fuente real antes de descargar datos.")
    print("Regla: este script puede guardar originales en data/raw sin transformarlos.")


if __name__ == "__main__":
    main()
""",
    "scripts/inspect_data.py": """
from pathlib import Path


def main() -> None:
    for folder in [Path("data/raw"), Path("data/processed"), Path("data/external")]:
        files = [p.name for p in folder.glob("*") if p.name != ".gitkeep"]
        print(f"{folder}: {len(files)} archivo(s)")


if __name__ == "__main__":
    main()
""",
    "scripts/clean_data.py": """
from pathlib import Path


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    print("Limpieza pendiente: leer desde data/raw y escribir derivados en data/processed.")
    print("No sobrescribir archivos originales.")


if __name__ == "__main__":
    main()
""",
    "scripts/build_features.py": """
from pathlib import Path


def main() -> None:
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    print("Feature engineering pendiente: documentar cada variable construida.")


if __name__ == "__main__":
    main()
""",
    "scripts/generate_tables.py": """
from pathlib import Path


def main() -> None:
    Path("outputs/tables").mkdir(parents=True, exist_ok=True)
    print("Generacion de tablas pendiente: incluir notas, fuente e interpretacion.")


if __name__ == "__main__":
    main()
""",
    "scripts/generate_figures.py": """
from pathlib import Path


def main() -> None:
    Path("outputs/figures").mkdir(parents=True, exist_ok=True)
    print("Generacion de figuras pendiente: incluir titulo, fuente e interpretacion.")


if __name__ == "__main__":
    main()
""",
    "scripts/run_all_notebooks.py": """
from pathlib import Path
import subprocess
import sys


def main() -> int:
    notebooks = sorted(Path("notebooks").glob("chapter_*/*.ipynb"))
    if not notebooks:
        print("No hay notebooks para ejecutar.")
        return 0
    for notebook in notebooks:
        print(f"Ejecutando {notebook}")
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                "--inplace",
                str(notebook),
            ],
            check=False,
        )
        if result.returncode != 0:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
""",
    "scripts/validate_reproducibility.py": """
from pathlib import Path


REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "ROADMAP.md",
    "requirements.txt",
    "environment.yml",
    "pyproject.toml",
    "book/index.md",
    "templates/checklist_libro.md",
    "examples/economia_computacional_python.md",
]


def main() -> int:
    missing = [path for path in REQUIRED_PATHS if not Path(path).exists()]
    raw_files = [
        p for p in Path("data/raw").glob("*") if p.name != ".gitkeep" and p.is_file()
    ]
    if missing:
        print("Faltan archivos requeridos:")
        for path in missing:
            print(f"- {path}")
        return 1
    print("Estructura base verificada.")
    print(f"Archivos originales en data/raw: {len(raw_files)}")
    print("Recordatorio: no modificar data/raw; escribir derivados en data/processed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
""",
}


def notebook(title: str) -> str:
    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# {title}\n",
                "\n",
                "Notebook inicial del proyecto ECONOLIBRO-CODEX.\n",
                "\n",
                "Objetivo: conectar una pregunta economica con un flujo reproducible en Python.\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "from pathlib import Path\n",
                "\n",
                "DATA_RAW = Path('../../data/raw')\n",
                "DATA_PROCESSED = Path('../../data/processed')\n",
                "OUTPUTS = Path('../../outputs')\n",
                "DATA_PROCESSED.mkdir(parents=True, exist_ok=True)\n",
                "OUTPUTS.mkdir(parents=True, exist_ok=True)\n",
                "print('Entorno listo')\n",
            ],
        },
    ]
    return json.dumps(
        {
            "cells": cells,
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3",
                },
                "language_info": {"name": "python", "pygments_lexer": "ipython3"},
            },
            "nbformat": 4,
            "nbformat_minor": 5,
        },
        indent=2,
    )


def generic_markdown(title: str, purpose: str) -> str:
    return f"""
# {title}

## Proposito

{purpose}

## Entradas

- Pregunta economica o editorial.
- Datos, referencias o capitulos ya verificados.
- Restricciones de reproducibilidad y publicacion.

## Salidas esperadas

- Producto documentado.
- Riesgos y limitaciones.
- Proximo paso verificable.

## Checklist

- [ ] Usa rutas relativas si hay codigo.
- [ ] No inventa fuentes, autores, DOI ni resultados.
- [ ] Declara supuestos y limitaciones.
- [ ] Incluye interpretacion economica cuando hay resultados.
"""


def main() -> None:
    for path, content in ROOT_FILES.items():
        write(path, content)
    for path, content in BOOK_FILES.items():
        write(path, content)
    for file_name, number, title in CHAPTERS:
        write(f"chapters/{file_name}", CHAPTER_TEMPLATE.format(number=number, title=title))
    for file_name, agent in PROMPTS.items():
        write(f"prompts/{file_name}", prompt_content(agent))
    for file_name, purpose in WORKFLOWS.items():
        write(f"workflows/{file_name}", generic_markdown(file_name[:-3].replace("_", " ").title(), purpose))
    for file_name, purpose in TEMPLATES.items():
        write(f"templates/{file_name}", generic_markdown(file_name[:-3].replace("_", " ").title(), purpose))
    for file_name, purpose in RUBRICS.items():
        write(f"rubrics/{file_name}", generic_markdown(file_name[:-3].replace("_", " ").title(), purpose))
    for path, purpose in DOCS.items():
        write(path, generic_markdown(Path(path).stem.replace("_", " ").title(), purpose))
    for path, content in SCRIPT_FILES.items():
        write(path, content)

    write(
        "data/README.md",
        """
# Datos

## Reglas

- `data/raw`: datos originales, sin modificar.
- `data/processed`: datos derivados por scripts documentados.
- `data/external`: datos auxiliares descargados de terceros.
- `data/dictionary`: diccionarios de variables y metadatos.

Todo dataset debe tener fuente, fecha de acceso, unidad de observacion, periodo,
variables clave, licencia o condiciones de uso y advertencias de calidad.
""",
    )
    write(
        "data/dictionary/diccionario_inicial.md",
        """
# Diccionario inicial de variables

Este archivo se completara cuando se incorpore el primer dataset real.

| variable | etiqueta | tipo | unidad | fuente | transformacion |
|---|---|---|---|---|---|
| pendiente | Pendiente de definir | pendiente | pendiente | pendiente | pendiente |
""",
    )
    write(
        "outputs/README.md",
        """
# Outputs

Los outputs se regeneran desde scripts o notebooks. No editar manualmente tablas,
figuras o reportes finales sin documentar el cambio.
""",
    )
    write(
        "examples/economia_computacional_python.md",
        """
# Ejemplo piloto: Economia Computacional con Python

## Ficha editorial

- Titulo: Economia Computacional con Python.
- Subtitulo: Datos, modelos y aplicaciones para estudiantes, docentes e
  investigadores en economia.
- Nivel: inicial-intermedio.
- Publico: estudiantes, docentes, tesistas, investigadores iniciales y analistas.

## Promesa de aprendizaje

Al finalizar el libro, el lector podra importar, limpiar, analizar, visualizar y
modelar datos economicos con Python usando flujos reproducibles.

## Primer capitulo sugerido

El capitulo 1 debe presentar la economia computacional como una forma de unir
preguntas economicas, datos, modelos y codigo. Debe cerrar con un mini-proyecto:
identificar una fuente de datos economicos real y documentar sus variables.
""",
    )
    write(
        "exercises/chapter_01/ejercicios.md",
        """
# Ejercicios - Capitulo 1

## Conceptuales

1. Explique la diferencia entre usar Python para automatizar calculos y usarlo
   para responder una pregunta economica.
2. Proponga una pregunta economica que requiera datos y explique que variable
   seria necesaria para responderla.

## Computacional

1. Cree una carpeta de proyecto con subcarpetas `data`, `notebooks` y `outputs`.
2. Escriba una celda de notebook que defina rutas relativas con `pathlib`.

## Mini-proyecto

Identifique una fuente de datos economicos real. No descargue datos todavia:
registre institucion, enlace, periodo, unidad de observacion y variables clave.
""",
    )
    write(
        "exercises/chapter_01/soluciones_docente.md",
        """
# Soluciones docentes - Capitulo 1

## Criterios de revision

- La respuesta diferencia herramienta computacional y argumento economico.
- La pregunta economica es observable con datos.
- La estructura de carpetas separa datos, notebooks y outputs.
- Las rutas usan `pathlib` y no dependen del computador del estudiante.

## Guia orientativa

Una buena respuesta debe conectar teoria, medicion y reproducibilidad. Si el
estudiante propone causalidad, debe indicar que falta una estrategia de
identificacion.
""",
    )
    write("notebooks/chapter_01/intro_economia_computacional.ipynb", notebook("Capitulo 1 - Economia computacional"))
    write("exercises/chapter_01/notebook_estudiante.ipynb", notebook("Notebook estudiante - Capitulo 1"))
    write("exercises/chapter_01/notebook_solucion.ipynb", notebook("Notebook solucion - Capitulo 1"))

    write(
        "publishing/quarto/_quarto.yml",
        """
project:
  type: book

book:
  title: "Economia Computacional con Python"
  subtitle: "Datos, modelos y aplicaciones para estudiantes, docentes e investigadores en economia"
  chapters:
    - ../../book/index.md
    - ../../chapters/01_introduccion_economia_computacional.md

format:
  html:
    toc: true
  pdf:
    documentclass: scrreprt
""",
    )
    write(
        "publishing/jupyterbook/_config.yml",
        """
title: Economia Computacional con Python
author: Econolab
execute:
  execute_notebooks: cache
bibtex_bibfiles:
  - ../../book/references.bib
""",
    )
    write(
        "publishing/kdp/portada.md",
        """
# Portada textual

## Titulo

Economia Computacional con Python

## Subtitulo

Datos, modelos y aplicaciones para estudiantes, docentes e investigadores en
economia

## Serie

Serie Econolab Computacional
""",
    )
    write(
        "publishing/kdp/contraportada.md",
        """
# Contraportada

Este libro ensena a trabajar preguntas economicas con Python mediante datos,
modelos, visualizaciones, notebooks reproducibles y ejercicios aplicados. Esta
version es un borrador editorial inicial y debe completarse con capitulos,
referencias verificadas y revision tecnica antes de publicarse.
""",
    )
    write(
        "publishing/lms/estructura_curso.md",
        """
# Estructura LMS

Cada modulo del curso corresponde a un capitulo del libro e incluye:

- Lectura principal.
- Notebook reproducible.
- Ejercicios.
- Solucion o guia docente.
- Rubrica.
- Mini-proyecto cuando aplique.
""",
    )
    write(
        "publishing/lms/carga_moodle.md",
        """
# Carga Moodle

Preparar cada capitulo como seccion del curso. Subir lectura en PDF/HTML,
notebook descargable, actividad evaluable y rubrica. Mantener nombres de
archivos consistentes con el numero de capitulo.
""",
    )
    write(
        "skills/README.md",
        """
# Skills futuras

Esta carpeta documenta posibles skills para automatizar flujos de
ECONOLIBRO-CODEX. Las skills deben operar sobre entregables verificables y
respetar las reglas del proyecto.
""",
    )
    write(
        "skills/econolibro_skill_spec.md",
        """
# Especificacion inicial de skill

## Nombre

econolibro-capitulo

## Objetivo

Ayudar a crear un paquete de capitulo con Markdown, notebook, ejercicios,
solucion docente, referencias verificadas y checklist de reproducibilidad.

## Restricciones

- No inventar fuentes.
- No modificar `data/raw`.
- No afirmar causalidad sin identificacion.
- No entregar notebooks que no puedan ejecutarse de arriba hacia abajo.
""",
    )

    for folder in [
        "data/raw",
        "data/processed",
        "data/external",
        "data/dictionary",
        "outputs/tables",
        "outputs/figures",
        "outputs/reports",
        "outputs/logs",
        "outputs/final",
    ]:
        touch(f"{folder}/.gitkeep")


if __name__ == "__main__":
    main()
