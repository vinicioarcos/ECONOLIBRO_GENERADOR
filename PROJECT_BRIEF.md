# ECONOLIBRO-CODEX

## Sistema Multiagente para Escritura de Libros de Economía Computacional con Python

---

## 1. Nombre del proyecto

**ECONOLIBRO-CODEX**

## 2. Subtítulo

Sistema multiagente para planificar, escribir, revisar y publicar libros de economía computacional con Python, notebooks reproducibles, datasets reales, ejercicios, rúbricas y preparación editorial.

## 3. Nombre sugerido del repositorio

```text
ECONOLIBRO_CODEX
```

Alternativas:

```text
econolibro-codex
econolab-computational-books
computational-economics-book-agents
econopy-book-system
serie-econolab-computacional
```

---

# 4. Descripción general

ECONOLIBRO-CODEX es una arquitectura multiagente diseñada para apoyar la creación de libros académicos y aplicados de economía con énfasis computacional, especialmente usando Python.

El sistema organiza la producción editorial en agentes especializados capaces de diseñar el índice del libro, estructurar capítulos, formular resultados de aprendizaje, preparar notebooks reproducibles, trabajar con datos económicos reales, generar ejercicios, revisar código, revisar teoría económica, validar modelos econométricos y preparar el libro para publicación en formatos como Markdown, Quarto, Jupyter Book, LaTeX, PDF, EPUB, HTML, LMS o Amazon KDP.

Este proyecto toma como inspiración la lógica de arquitecturas multiagente para investigación académica como AURA, pero cambia el objetivo central: en lugar de producir papers académicos, produce libros completos, cursos-libro y materiales editoriales computacionales.

---

# 5. Problema que resuelve

La escritura de libros académicos aplicados suele tener varios problemas:

- índices desordenados;
- capítulos sin progresión pedagógica;
- teoría económica desconectada del código;
- notebooks que no se ejecutan;
- ejemplos artificiales;
- datasets sin documentación;
- ejercicios sin solución;
- ausencia de rúbricas;
- gráficos sin interpretación;
- referencias incompletas;
- dificultad para publicar en varios formatos;
- falta de trazabilidad entre teoría, datos, código, resultados y ejercicios.

ECONOLIBRO-CODEX busca resolver estos problemas mediante una arquitectura de trabajo clara, reproducible y multiagente.

---

# 6. Objetivo general

Diseñar e implementar un sistema multiagente para producir libros de economía computacional con Python, integrando teoría económica, datos reales, programación reproducible, notebooks, ejercicios, visualizaciones, revisión técnica, diseño pedagógico y preparación editorial.

---

# 7. Objetivos específicos

1. Crear una estructura de repositorio para libros computacionales de economía.
2. Diseñar agentes especializados para cada fase de producción editorial.
3. Crear prompts estructurados para Claude Code, Codex, Copilot y otros agentes.
4. Diseñar plantillas para capítulos, notebooks, ejercicios, datasets, figuras y publicación.
5. Crear rúbricas para evaluar capítulos, código, ejercicios, visualizaciones y reproducibilidad.
6. Preparar el proyecto para escribir libros con Python, datos económicos y notebooks ejecutables.
7. Integrar bases de datos oficiales de Ecuador, América Latina y organismos internacionales.
8. Preparar la publicación en Quarto, Jupyter Book, PDF, EPUB, HTML, LMS y Amazon KDP.
9. Diseñar una colección editorial llamada Serie Econolab Computacional.
10. Preparar el proyecto para futura automatización con Claude Skills, LangGraph, MCP, GitHub Actions y LMS.

---

# 8. Principios obligatorios

El proyecto debe obedecer estos principios:

1. No inventar fuentes.
2. No inventar autores.
3. No inventar DOI.
4. No inventar resultados empíricos.
5. No afirmar causalidad sin estrategia de identificación.
6. No modificar archivos en `data/raw`.
7. Guardar datos procesados únicamente en `data/processed`.
8. Usar rutas relativas.
9. Evitar código que dependa del computador del autor.
10. Todo capítulo debe tener resultados de aprendizaje.
11. Todo código debe tener propósito económico.
12. Todo notebook debe ejecutarse de arriba hacia abajo.
13. Toda figura debe tener título, fuente e interpretación.
14. Toda tabla debe tener notas claras.
15. Todo ejercicio debe tener solución o guía docente.
16. Separar teoría, datos, código, resultados, ejercicios y publicación.
17. No usar machine learning como reemplazo de teoría económica.
18. No usar Python como decoración tecnológica.
19. No incluir citas decorativas.
20. Priorizar reproducibilidad, claridad y utilidad docente.

---

# 9. Serie Econolab Computacional

La colección editorial del proyecto será:

## Línea 1. Fundamentos computacionales para economía

1. Economía Computacional con Python.
2. Estadística para Economía con Python.
3. Ciencia de Datos para Economía.
4. Visualización y Storytelling de Datos Económicos con Python.

## Línea 2. Econometría aplicada con Python

5. Econometría Aplicada con Python.
6. Microeconometría Aplicada con Python.
7. Evaluación de Impacto con Python.
8. Series de Tiempo Macroeconómicas con Python.
9. Econometría Financiera con Python.
10. Econometría Espacial con Python.

## Línea 3. Economía, política pública y contexto

11. Mercado Laboral y ENEMDU con Python.
12. Educación, Capital Humano e Ingresos con Python.
13. Pobreza, Desigualdad y Movilidad Social con Python.
14. Políticas Públicas Basadas en Datos.
15. Análisis del Contexto Nacional y Global con IA.

## Línea 4. Inteligencia artificial, productividad e investigación

16. Inteligencia Artificial para Economistas.
17. IA Generativa Aplicada a la Investigación Académica.
18. IA Agéntica Aplicada a la Productividad, Investigación y Transformación Organizacional.
19. Automatización de Procesos Académicos y Empresariales con IA.
20. Sistemas Multiagente para Investigación, Docencia y Consultoría.

---

# 10. Trilogía fundacional recomendada

El proyecto debe iniciar con tres libros estratégicos:

1. **Economía Computacional con Python**  
   Público: estudiantes, docentes, tesistas e investigadores iniciales.

2. **Econometría Aplicada con Python**  
   Público: economistas, maestrantes, investigadores y analistas.

3. **IA Agéntica Aplicada a la Productividad, Investigación y Transformación Organizacional**  
   Público: universidades, empresas, sector público, docentes, investigadores y profesionales.

---

# 11. Arquitectura multiagente

El sistema debe incluir 12 agentes:

```text
1. Agente arquitecto editorial
2. Agente diseñador pedagógico
3. Agente investigador bibliográfico
4. Agente economista teórico-aplicado
5. Agente de datos económicos
6. Agente programador Python
7. Agente econometrista computacional
8. Agente científico de datos
9. Agente visualizador y storyteller de datos
10. Agente generador de ejercicios y evaluaciones
11. Agente revisor técnico-académico
12. Agente editor final y publicador
```

---

# 12. Función de cada agente

## 12.1. Agente arquitecto editorial

Convierte una idea general en un proyecto de libro.

Responsabilidades:

- definir título;
- definir subtítulo;
- definir público objetivo;
- definir nivel académico;
- definir promesa de aprendizaje;
- definir índice maestro;
- definir estructura por partes;
- definir extensión aproximada;
- definir formato editorial;
- definir productos complementarios.

Entregables:

- ficha editorial del libro;
- índice maestro;
- mapa de capítulos;
- propuesta de valor;
- estructura narrativa;
- plan de escritura;
- cronograma editorial.

---

## 12.2. Agente diseñador pedagógico

Diseña la experiencia de aprendizaje del libro.

Responsabilidades:

- definir resultados de aprendizaje;
- definir competencias;
- definir prerrequisitos;
- diseñar actividades;
- diseñar ejercicios;
- diseñar mini-proyectos;
- diseñar rúbricas;
- crear guía docente;
- crear guía del estudiante.

Entregables:

- matriz pedagógica;
- resultados de aprendizaje por capítulo;
- actividades prácticas;
- rúbricas;
- banco de preguntas;
- guía docente;
- guía del estudiante.

---

## 12.3. Agente investigador bibliográfico

Sustenta el libro con literatura de calidad.

Responsabilidades:

- identificar libros seminales;
- identificar artículos relevantes;
- identificar documentación técnica;
- identificar fuentes de datos;
- crear referencias por capítulo;
- revisar consistencia bibliográfica;
- evitar fuentes inventadas.

Entregables:

- matriz bibliográfica;
- fichas de libros;
- fichas de artículos;
- lecturas obligatorias;
- lecturas complementarias;
- referencias APA 7 o BibTeX.

---

## 12.4. Agente economista teórico-aplicado

Conecta el contenido computacional con teoría económica.

Responsabilidades:

- explicar intuición económica;
- conectar teoría con datos;
- proponer casos aplicados;
- contextualizar con Ecuador y América Latina;
- formular mecanismos económicos;
- advertir límites de interpretación.

Entregables:

- explicación económica por capítulo;
- mecanismos teóricos;
- casos aplicados;
- implicaciones de política pública;
- advertencias de interpretación.

---

## 12.5. Agente de datos económicos

Identifica, descarga, documenta, limpia y valida bases de datos.

Fuentes sugeridas:

- INEC;
- ENEMDU;
- ECV;
- ENDI;
- ENSANUT;
- Censo;
- Banco Central del Ecuador;
- SRI, si aplica;
- Banco Mundial;
- CEPALSTAT;
- ILOSTAT;
- Our World in Data;
- IMF Data;
- Penn World Table;
- FRED;
- OECD Data.

Responsabilidades:

- crear inventario de datos;
- crear diccionario de variables;
- descargar datos;
- revisar metadatos;
- limpiar datos;
- validar llaves;
- revisar missing values;
- documentar filtros;
- mantener intacto `data/raw`.

Entregables:

- inventario de datasets;
- diccionario de variables;
- script de descarga;
- script de limpieza;
- reporte de calidad de datos;
- cleaning log;
- datos procesados en `data/processed`.

---

## 12.6. Agente programador Python

Implementa el código reproducible del libro.

Responsabilidades:

- crear notebooks;
- crear scripts;
- cargar datos;
- limpiar datos;
- transformar variables;
- estimar modelos;
- generar tablas;
- generar gráficos;
- exportar outputs;
- documentar dependencias.

Librerías sugeridas:

- pathlib;
- pandas;
- numpy;
- scipy;
- statsmodels;
- linearmodels;
- scikit-learn;
- matplotlib;
- plotly;
- pyreadstat;
- openpyxl;
- jupyter;
- quarto.

Entregables:

- notebooks por capítulo;
- scripts `.py`;
- funciones reutilizables;
- tablas exportables;
- figuras exportables;
- requirements.txt;
- environment.yml;
- guía de instalación.

---

## 12.7. Agente econometrista computacional

Diseña, explica e implementa modelos econométricos en Python.

Temas posibles:

- regresión lineal;
- regresión múltiple;
- variables dummy;
- interacciones;
- heterocedasticidad;
- errores robustos;
- logit;
- probit;
- modelos de conteo;
- datos de panel;
- diferencias en diferencias;
- regresión discontinua;
- variables instrumentales;
- propensity score matching;
- series de tiempo;
- ARIMA;
- VAR;
- cointegración;
- modelos con ponderadores de encuesta.

Entregables:

- especificación matemática;
- explicación intuitiva;
- implementación en Python;
- interpretación de coeficientes;
- ejercicios aplicados;
- advertencias causales;
- pruebas de robustez.

---

## 12.8. Agente científico de datos

Desarrolla análisis exploratorio, modelamiento predictivo e interpretabilidad.

Responsabilidades:

- análisis exploratorio;
- tratamiento de missing values;
- detección de outliers;
- feature engineering;
- clustering;
- clasificación;
- predicción;
- validación cruzada;
- métricas de desempeño;
- interpretabilidad;
- SHAP, si aplica;
- comparación entre enfoque predictivo y econométrico.

Entregables:

- notebooks de ciencia de datos;
- EDA reports;
- modelos predictivos;
- visualizaciones;
- interpretación económica;
- advertencias metodológicas.

---

## 12.9. Agente visualizador y storyteller de datos

Convierte resultados en gráficos, tablas y narrativa visual.

Responsabilidades:

- crear figuras;
- crear tablas;
- crear diagramas;
- crear mapas conceptuales;
- mejorar captions;
- revisar legibilidad;
- exportar gráficos en PNG, SVG y PDF;
- asegurar interpretación económica.

Entregables:

- figuras por capítulo;
- tablas limpias;
- captions;
- notas de figuras;
- storytelling visual;
- lineamientos gráficos.

---

## 12.10. Agente generador de ejercicios y evaluaciones

Crea actividades para estudiantes y docentes.

Responsabilidades:

- preguntas conceptuales;
- ejercicios de código;
- ejercicios con datos;
- mini-proyectos;
- evaluaciones;
- rúbricas;
- soluciones docentes;
- notebooks incompletos para estudiantes;
- notebooks solucionados para docentes.

Entregables:

- banco de ejercicios;
- soluciones;
- rúbricas;
- proyectos aplicados;
- preguntas tipo examen;
- actividades para LMS;
- actividades para GitHub Classroom.

---

## 12.11. Agente revisor técnico-académico

Evalúa rigor, coherencia y reproducibilidad.

Responsabilidades:

- revisar teoría económica;
- revisar código;
- revisar notebooks;
- revisar modelos;
- revisar visualizaciones;
- revisar datos;
- revisar ejercicios;
- revisar reproducibilidad;
- revisar coherencia editorial.

Entregables:

- dictamen técnico;
- errores mayores;
- errores menores;
- recomendaciones;
- checklist prepublicación;
- informe de reproducibilidad.

---

## 12.12. Agente editor final y publicador

Prepara el libro para publicación.

Formatos objetivo:

- Markdown;
- Quarto;
- Jupyter Book;
- LaTeX;
- PDF;
- EPUB;
- HTML;
- Amazon KDP;
- LMS;
- GitHub Pages.

Entregables:

- manuscrito final;
- portada textual;
- contraportada;
- biografía del autor;
- índice final;
- metadatos;
- archivos de publicación;
- versión para estudiantes;
- versión para docentes.

---

# 13. Flujo general de trabajo

```text
Idea del libro
        ↓
Agente arquitecto editorial
        ↓
Ficha editorial e índice maestro
        ↓
Agente diseñador pedagógico
        ↓
Resultados de aprendizaje y estructura didáctica
        ↓
Agente investigador bibliográfico
        ↓
Bibliografía por capítulo
        ↓
Agente economista teórico-aplicado
        ↓
Marco conceptual y casos económicos
        ↓
Agente de datos económicos
        ↓
Datasets, diccionarios y limpieza
        ↓
Agente programador Python
        ↓
Notebooks y scripts reproducibles
        ↓
Agente econometrista computacional
        ↓
Modelos, interpretación y supuestos
        ↓
Agente científico de datos
        ↓
EDA, predicción y análisis aplicado
        ↓
Agente visualizador
        ↓
Figuras, tablas y storytelling
        ↓
Agente de ejercicios
        ↓
Actividades, soluciones y rúbricas
        ↓
Agente revisor técnico
        ↓
Correcciones académicas y computacionales
        ↓
Agente editor final
        ↓
Libro publicable
```

---

# 14. Estructura de carpetas recomendada

```text
ECONOLIBRO_CODEX/
│
├── README.md
├── AGENTS.md
├── PROJECT_BRIEF.md
├── ROADMAP.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── environment.yml
├── pyproject.toml
│
├── book/
│   ├── index.md
│   ├── preface.md
│   ├── introduction.md
│   ├── references.bib
│   ├── glossary.md
│   ├── author_bio.md
│   ├── acknowledgements.md
│   └── _toc.yml
│
├── chapters/
│   ├── 00_prefacio.md
│   ├── 01_introduccion_economia_computacional.md
│   ├── 02_python_para_economistas.md
│   ├── 03_datos_economicos_con_pandas.md
│   ├── 04_visualizacion_economica.md
│   ├── 05_estadistica_aplicada.md
│   ├── 06_regresion_lineal.md
│   ├── 07_modelos_logit_probit.md
│   ├── 08_series_de_tiempo.md
│   ├── 09_evaluacion_impacto.md
│   ├── 10_machine_learning_economia.md
│   ├── 11_proyecto_final.md
│   └── 12_conclusiones.md
│
├── notebooks/
│   ├── chapter_01/
│   ├── chapter_02/
│   ├── chapter_03/
│   ├── chapter_04/
│   ├── chapter_05/
│   ├── chapter_06/
│   ├── chapter_07/
│   ├── chapter_08/
│   ├── chapter_09/
│   ├── chapter_10/
│   └── chapter_11/
│
├── scripts/
│   ├── download_data.py
│   ├── inspect_data.py
│   ├── clean_data.py
│   ├── build_features.py
│   ├── generate_tables.py
│   ├── generate_figures.py
│   ├── run_all_notebooks.py
│   └── validate_reproducibility.py
│
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   ├── processed/
│   │   └── .gitkeep
│   ├── external/
│   │   └── .gitkeep
│   ├── dictionary/
│   │   └── .gitkeep
│   └── README.md
│
├── outputs/
│   ├── tables/
│   │   └── .gitkeep
│   ├── figures/
│   │   └── .gitkeep
│   ├── reports/
│   │   └── .gitkeep
│   ├── logs/
│   │   └── .gitkeep
│   └── final/
│       └── .gitkeep
│
├── exercises/
│   ├── chapter_01/
│   │   ├── ejercicios.md
│   │   ├── soluciones_docente.md
│   │   ├── notebook_estudiante.ipynb
│   │   └── notebook_solucion.ipynb
│   ├── chapter_02/
│   ├── chapter_03/
│   ├── chapter_04/
│   ├── chapter_05/
│   ├── chapter_06/
│   ├── chapter_07/
│   ├── chapter_08/
│   ├── chapter_09/
│   ├── chapter_10/
│   └── chapter_11/
│
├── prompts/
│   ├── 01_agente_arquitecto_editorial.md
│   ├── 02_agente_disenador_pedagogico.md
│   ├── 03_agente_investigador_bibliografico.md
│   ├── 04_agente_economista_teorico_aplicado.md
│   ├── 05_agente_datos_economicos.md
│   ├── 06_agente_programador_python.md
│   ├── 07_agente_econometrista_computacional.md
│   ├── 08_agente_cientifico_datos.md
│   ├── 09_agente_visualizador_storytelling.md
│   ├── 10_agente_ejercicios_evaluaciones.md
│   ├── 11_agente_revisor_tecnico_academico.md
│   └── 12_agente_editor_final_publicador.md
│
├── skills/
│   ├── book-editorial-architect/
│   │   ├── SKILL.md
│   │   ├── resources/
│   │   └── templates/
│   ├── book-pedagogy/
│   │   ├── SKILL.md
│   │   ├── resources/
│   │   └── templates/
│   ├── book-literature/
│   │   ├── SKILL.md
│   │   ├── resources/
│   │   └── templates/
│   ├── book-economics/
│   │   ├── SKILL.md
│   │   └── resources/
│   ├── book-data-agent/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── book-python/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── book-econometrics/
│   │   ├── SKILL.md
│   │   └── resources/
│   ├── book-data-science/
│   │   ├── SKILL.md
│   │   └── resources/
│   ├── book-visualization/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── book-exercises/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── book-reviewer/
│   │   ├── SKILL.md
│   │   └── templates/
│   └── book-publishing/
│       ├── SKILL.md
│       └── templates/
│
├── workflows/
│   ├── 01_workflow_diseno_libro.md
│   ├── 02_workflow_capitulo.md
│   ├── 03_workflow_notebook_python.md
│   ├── 04_workflow_datos.md
│   ├── 05_workflow_econometria.md
│   ├── 06_workflow_ciencia_datos.md
│   ├── 07_workflow_ejercicios.md
│   ├── 08_workflow_revision_tecnica.md
│   └── 09_workflow_publicacion.md
│
├── templates/
│   ├── ficha_editorial_libro.md
│   ├── indice_maestro.md
│   ├── plantilla_capitulo.md
│   ├── plantilla_notebook.md
│   ├── plantilla_ejercicios.md
│   ├── plantilla_soluciones_docente.md
│   ├── matriz_pedagogica.md
│   ├── matriz_bibliografica.md
│   ├── data_dictionary.md
│   ├── cleaning_log.md
│   ├── figure_caption.md
│   ├── tabla_resultados.md
│   ├── checklist_capitulo.md
│   ├── checklist_libro.md
│   ├── portada_kdp.md
│   └── contraportada.md
│
├── rubrics/
│   ├── rubrica_capitulo.md
│   ├── rubrica_codigo_python.md
│   ├── rubrica_notebook.md
│   ├── rubrica_ejercicios.md
│   ├── rubrica_datos.md
│   ├── rubrica_visualizacion.md
│   ├── rubrica_econometria.md
│   ├── rubrica_ciencia_datos.md
│   ├── rubrica_estilo_editorial.md
│   └── rubrica_publicacion.md
│
├── examples/
│   ├── economia_computacional_python/
│   │   ├── project_config.md
│   │   ├── chapters/
│   │   ├── notebooks/
│   │   ├── data/
│   │   ├── exercises/
│   │   └── outputs/
│   │
│   ├── econometria_con_python/
│   │   ├── project_config.md
│   │   ├── chapters/
│   │   ├── notebooks/
│   │   ├── data/
│   │   ├── exercises/
│   │   └── outputs/
│   │
│   └── politica_publica_computacional/
│       ├── project_config.md
│       ├── chapters/
│       ├── notebooks/
│       ├── data/
│       ├── exercises/
│       └── outputs/
│
├── publishing/
│   ├── quarto/
│   │   ├── _quarto.yml
│   │   └── styles.scss
│   ├── jupyterbook/
│   │   ├── _config.yml
│   │   └── _toc.yml
│   ├── latex/
│   │   ├── main.tex
│   │   └── preamble.tex
│   ├── kdp/
│   │   ├── metadata.md
│   │   ├── portada.md
│   │   └── contraportada.md
│   └── lms/
│       ├── estructura_curso.md
│       └── carga_moodle.md
│
└── docs/
    ├── guia_autor.md
    ├── guia_docente.md
    ├── guia_estudiante.md
    ├── guia_instalacion.md
    └── guia_publicacion.md
```

---

# 15. Estructura obligatoria de cada capítulo

Cada capítulo debe seguir esta plantilla:

```markdown
# Capítulo X. Título del capítulo

## 1. Apertura

### Pregunta motivadora

¿Qué problema económico queremos entender?

### Caso aplicado

Ejemplo contextualizado, preferentemente Ecuador o América Latina.

### Por qué importa

Relevancia económica, social, empresarial o de política pública.

## 2. Resultados de aprendizaje

Al finalizar este capítulo, el lector será capaz de:

1. Explicar...
2. Implementar...
3. Interpretar...
4. Aplicar...

## 3. Conceptos clave

- Concepto 1
- Concepto 2
- Concepto 3

## 4. Intuición económica

Explicación conceptual sin código.

## 5. Formalización mínima

Modelo, ecuación o estructura analítica necesaria.

## 6. Datos

Fuente, variables, muestra, período y advertencias.

## 7. Implementación en Python

Código explicado paso a paso.

## 8. Resultados

Tablas, gráficos y salidas principales.

## 9. Interpretación económica

Qué significan los resultados.

## 10. Errores frecuentes

Errores conceptuales, técnicos y de interpretación.

## 11. Ejercicios

Ejercicios conceptuales y computacionales.

## 12. Mini-proyecto

Actividad aplicada de cierre.

## 13. Lecturas recomendadas

Bibliografía básica y complementaria.

## 14. Resumen del capítulo

Ideas centrales.

## 15. Checklist de aprendizaje

- [ ] Puedo explicar...
- [ ] Puedo implementar...
- [ ] Puedo interpretar...
```

---

# 16. Primer libro piloto

## Título

**Economía Computacional con Python**

## Subtítulo

**Datos, modelos y aplicaciones para estudiantes, docentes e investigadores en economía**

## Público objetivo

- Estudiantes de economía.
- Estudiantes de administración.
- Docentes universitarios.
- Investigadores aplicados.
- Tesistas.
- Profesionales del sector público.
- Analistas de datos económicos.

## Nivel

Inicial-intermedio.

## Promesa del libro

Al finalizar el libro, el lector podrá importar, limpiar, analizar, visualizar y modelar datos económicos con Python, usando ejemplos aplicados a problemas reales de economía, mercado laboral, educación, pobreza, desigualdad, crecimiento y política pública.

---

# 17. Índice tentativo del primer libro

```text
Parte I. Fundamentos

Capítulo 1. ¿Qué es la economía computacional?
Capítulo 2. Instalación, Google Colab y entorno de trabajo
Capítulo 3. Python básico para economistas
Capítulo 4. Pensamiento computacional aplicado a problemas económicos

Parte II. Datos económicos

Capítulo 5. Fuentes de datos económicos
Capítulo 6. Limpieza de datos con Pandas
Capítulo 7. Transformación y construcción de variables
Capítulo 8. Tablas estadísticas para análisis económico

Parte III. Visualización y estadística aplicada

Capítulo 9. Visualización de datos económicos
Capítulo 10. Estadística descriptiva computacional
Capítulo 11. Distribuciones, muestreo e inferencia básica

Parte IV. Econometría con Python

Capítulo 12. Regresión lineal simple
Capítulo 13. Regresión múltiple
Capítulo 14. Variables dummy e interacciones
Capítulo 15. Heterocedasticidad y errores robustos
Capítulo 16. Modelos logit y probit
Capítulo 17. Introducción a datos de panel
Capítulo 18. Introducción a series de tiempo

Parte V. Ciencia de datos para economía

Capítulo 19. Análisis exploratorio avanzado
Capítulo 20. Introducción a machine learning para economía
Capítulo 21. Clasificación y predicción económica
Capítulo 22. Clustering y segmentación económica
Capítulo 23. Interpretabilidad de modelos

Parte VI. Aplicaciones

Capítulo 24. Mercado laboral con ENEMDU
Capítulo 25. Educación e ingresos
Capítulo 26. Pobreza y desigualdad
Capítulo 27. Inflación y series macroeconómicas
Capítulo 28. Política pública basada en datos

Parte VII. Proyecto final

Capítulo 29. Cómo construir un proyecto reproducible
Capítulo 30. Proyecto final aplicado
```

---

# 18. Segundo libro piloto

## Título

**Econometría Aplicada con Python**

## Subtítulo

**Modelos, inferencia y aplicaciones empíricas para economía y políticas públicas**

## Temas principales

- MCO.
- Regresión múltiple.
- Variables dummy.
- Interacciones.
- Heterocedasticidad.
- Errores robustos.
- Logit y probit.
- Modelos de conteo.
- Datos de panel.
- Diferencias en diferencias.
- Regresión discontinua.
- Variables instrumentales.
- Propensity Score Matching.
- Series de tiempo.
- Modelos con ponderadores de encuesta.

## Casos aplicados

- Ingresos laborales.
- Educación e ingresos.
- Informalidad.
- Pobreza.
- Mercado laboral.
- Evaluación de programas públicos.
- ENEMDU.
- BCE.
- Banco Mundial.

---

# 19. Tercer libro piloto

## Título

**IA Agéntica Aplicada a la Productividad, Investigación y Transformación Organizacional**

## Subtítulo

**Diseño de agentes, automatización inteligente y sistemas multiagente para universidades, empresas y sector público**

## Temas principales

- Fundamentos de IA agéntica.
- Diferencia entre chatbot, workflow y agente.
- Agentes para investigación académica.
- Agentes para análisis de datos.
- Agentes para revisión documental.
- Agentes para productividad personal.
- Agentes para gestión universitaria.
- Agentes para empresas.
- Agentes para sector público.
- Automatización con n8n, Make o Zapier.
- LangGraph.
- Claude Projects.
- Claude Skills.
- OpenAI Agents.
- MCP.
- RAG.
- Evaluación y trazabilidad.
- Riesgos éticos y organizacionales.

## Casos aplicados

- Agente investigador académico.
- Agente econometrista.
- Agente para revisar papers.
- Agente para generar informes institucionales.
- Agente para atención estudiantil.
- Agente para gestión documental.
- Agente para análisis de productividad.
- Agente para procesos de acreditación.
- Agente para inteligencia competitiva.

---

# 20. Archivos iniciales que deben crearse

El primer sprint debe producir:

```text
- README.md
- AGENTS.md
- PROJECT_BRIEF.md
- ROADMAP.md
- LICENSE
- .gitignore
- requirements.txt
- environment.yml
- pyproject.toml
- estructura completa de carpetas
- 12 prompts de agentes
- 9 workflows
- 16 templates
- 10 rubrics
- índice tentativo del primer libro
- plantilla de capítulo
- plantilla de notebook
- plantilla de ejercicios
- ejemplo piloto: Economía Computacional con Python
```

---

# 21. Contenido base de AGENTS.md

Crear un archivo `AGENTS.md` con el siguiente contenido inicial:

```markdown
# AGENTS.md

## Proyecto

ECONOLIBRO-CODEX: Sistema Multiagente para Escritura de Libros de Economía Computacional con Python.

## Descripción

Este proyecto implementa una arquitectura multiagente para planificar, escribir, revisar y publicar libros académicos y aplicados de economía con énfasis computacional.

El sistema produce capítulos, notebooks, scripts, ejercicios, datasets documentados, figuras, tablas, rúbricas y materiales complementarios para docencia, investigación y publicación.

## Regla general

Cada agente debe producir entregables verificables. No se aceptan respuestas genéricas, texto de relleno ni código decorativo.

## Agentes

### 1. Agente arquitecto editorial

Convierte una idea de libro en una propuesta editorial. Define título, subtítulo, público objetivo, nivel, índice maestro, estructura por partes, estilo y formato de publicación.

### 2. Agente diseñador pedagógico

Define resultados de aprendizaje, competencias, actividades, ejercicios, rúbricas y estructura didáctica por capítulo.

### 3. Agente investigador bibliográfico

Busca y organiza literatura académica, libros, artículos, documentación técnica y fuentes de datos para sustentar cada capítulo.

### 4. Agente economista teórico-aplicado

Conecta los capítulos con teoría económica, mecanismos, intuición, contexto institucional y aplicaciones reales.

### 5. Agente de datos económicos

Identifica, descarga, documenta, limpia y valida bases económicas. Mantiene intacta data/raw y guarda transformaciones en data/processed.

### 6. Agente programador Python

Implementa notebooks, scripts, funciones, tablas y gráficos reproducibles. Todo código debe ser claro, didáctico y ejecutable.

### 7. Agente econometrista computacional

Diseña y explica modelos econométricos implementados en Python, sus supuestos, interpretación y límites.

### 8. Agente científico de datos

Desarrolla análisis exploratorio, modelos predictivos, validación, segmentación e interpretabilidad aplicada a problemas económicos.

### 9. Agente visualizador y storyteller de datos

Produce gráficos, tablas, diagramas y narrativas visuales claras para enseñar y comunicar resultados económicos.

### 10. Agente generador de ejercicios y evaluaciones

Crea ejercicios conceptuales, computacionales, mini-proyectos, soluciones docentes, rúbricas y bancos de preguntas.

### 11. Agente revisor técnico-académico

Evalúa rigor económico, claridad pedagógica, calidad del código, reproducibilidad, consistencia de datos y coherencia editorial.

### 12. Agente editor final y publicador

Prepara el libro para publicación en Markdown, Quarto, Jupyter Book, LaTeX, PDF, EPUB, HTML, Amazon KDP, LMS o GitHub Pages.

## Reglas obligatorias

1. No inventar fuentes.
2. No inventar autores.
3. No inventar DOI.
4. No inventar resultados.
5. No afirmar causalidad sin identificación.
6. No modificar data/raw.
7. No usar rutas absolutas.
8. No entregar código que dependa del computador del autor.
9. No incluir gráficos sin interpretación.
10. No crear ejercicios sin solución o guía.
11. No usar machine learning como reemplazo de teoría económica.
12. No mezclar datos originales con datos procesados.
13. No usar citas decorativas.
14. No entregar capítulos sin resultados de aprendizaje.
15. No entregar notebooks que no puedan ejecutarse de arriba hacia abajo.

## Formato de respuesta obligatorio para cada agente

Cada agente debe responder con:

1. Diagnóstico.
2. Producto generado.
3. Justificación.
4. Riesgos o limitaciones.
5. Próximo paso.
```

---

# 22. Roadmap inicial

Crear un archivo `ROADMAP.md` con el siguiente contenido:

```markdown
# ROADMAP.md

## Fase 1. Diseño editorial

- Definir título del libro.
- Definir público objetivo.
- Definir nivel.
- Definir índice maestro.
- Definir estilo editorial.
- Definir formato de publicación.

## Fase 2. Diseño pedagógico

- Crear resultados de aprendizaje.
- Crear matriz pedagógica.
- Definir ejercicios por capítulo.
- Definir rúbricas.
- Definir guía docente y guía del estudiante.

## Fase 3. Infraestructura computacional

- Crear entorno Python.
- Crear requirements.txt.
- Crear notebooks base.
- Crear scripts de datos.
- Crear estructura reproducible.
- Crear guía de instalación.

## Fase 4. Datos

- Identificar datasets.
- Descargar datos.
- Crear data dictionary.
- Crear cleaning log.
- Crear bases procesadas.
- Validar calidad.

## Fase 5. Escritura de capítulos

- Redactar capítulos en Markdown.
- Integrar teoría.
- Integrar ejemplos Python.
- Integrar figuras.
- Integrar ejercicios.
- Integrar referencias.

## Fase 6. Revisión técnica

- Revisar teoría.
- Revisar código.
- Revisar notebooks.
- Revisar datos.
- Revisar ejercicios.
- Revisar reproducibilidad.

## Fase 7. Publicación

- Preparar versión Quarto.
- Preparar versión Jupyter Book.
- Preparar versión PDF.
- Preparar versión EPUB.
- Preparar versión LMS.
- Preparar versión KDP, si aplica.

## Fase 8. Escalamiento

- Crear más libros.
- Crear biblioteca Econolab.
- Crear cursos asociados.
- Integrar con LMS.
- Crear Claude Skills.
- Automatizar con LangGraph.
```

---

# 23. .gitignore sugerido

Crear `.gitignore` con este contenido:

```gitignore
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

# VS Code
.vscode/

# Secrets
*.key
*.pem
secrets.*
.env.local

# Large files
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
```

---

# 24. requirements.txt sugerido

Crear `requirements.txt` con este contenido inicial:

```txt
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
quarto
black
ruff
pytest
```

---

# 25. environment.yml sugerido

Crear `environment.yml` con este contenido:

```yaml
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
```

---

# 26. pyproject.toml sugerido

Crear `pyproject.toml` con este contenido:

```toml
[project]
name = "econolibro-codex"
version = "0.1.0"
description = "Sistema multiagente para escritura de libros de economía computacional con Python."
authors = [
    { name = "Econolab" }
]
requires-python = ">=3.11"

[tool.black]
line-length = 88
target-version = ["py311"]

[tool.ruff]
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "I", "B"]
ignore = []
```

---

# 27. Checklist de calidad del libro

Crear `templates/checklist_libro.md` con este contenido:

```markdown
# Checklist de calidad antes de publicar

## Identidad editorial

- [ ] El título es claro.
- [ ] El subtítulo comunica valor.
- [ ] El público objetivo está definido.
- [ ] El nivel académico está claro.
- [ ] El índice tiene progresión lógica.

## Pedagogía

- [ ] Cada capítulo tiene resultados de aprendizaje.
- [ ] Cada capítulo tiene conceptos clave.
- [ ] Cada capítulo tiene ejercicios.
- [ ] Cada capítulo tiene resumen.
- [ ] Cada capítulo tiene checklist de aprendizaje.
- [ ] Hay guía docente.
- [ ] Hay guía del estudiante.

## Economía

- [ ] Los conceptos económicos están bien explicados.
- [ ] Hay conexión con teoría económica.
- [ ] Hay aplicaciones reales.
- [ ] Hay ejemplos de Ecuador o América Latina cuando corresponde.
- [ ] No se usa código sin interpretación económica.

## Python

- [ ] Los notebooks se ejecutan de arriba abajo.
- [ ] Las rutas son relativas.
- [ ] El código está comentado.
- [ ] Las librerías están documentadas.
- [ ] requirements.txt está actualizado.
- [ ] No hay errores visibles.
- [ ] Los outputs se generan automáticamente.

## Datos

- [ ] data/raw está intacta.
- [ ] data/processed contiene datos derivados.
- [ ] Hay diccionario de variables.
- [ ] Hay cleaning log.
- [ ] Hay fuente de datos.
- [ ] Hay advertencias sobre filtros y muestra.

## Figuras y tablas

- [ ] Todas las figuras tienen título.
- [ ] Todas las figuras tienen fuente.
- [ ] Todas las figuras tienen interpretación.
- [ ] Las tablas son legibles.
- [ ] Las tablas tienen notas.
- [ ] Los resultados no se sobreinterpretan.

## Ejercicios

- [ ] Hay ejercicios conceptuales.
- [ ] Hay ejercicios computacionales.
- [ ] Hay mini-proyectos.
- [ ] Hay soluciones docentes.
- [ ] Hay rúbricas.
- [ ] Los ejercicios están alineados con los objetivos.

## Reproducibilidad

- [ ] El libro puede reconstruirse desde cero.
- [ ] Los notebooks funcionan.
- [ ] Los scripts funcionan.
- [ ] Las dependencias están claras.
- [ ] Los datos están documentados.
- [ ] Los outputs pueden regenerarse.

## Publicación

- [ ] Hay versión Markdown.
- [ ] Hay versión Quarto o Jupyter Book.
- [ ] Hay versión PDF.
- [ ] Hay referencias completas.
- [ ] Hay portada y contraportada.
- [ ] Hay metadatos.
```

---

# 28. Instrucción principal para Claude Code o Codex

Usar esta instrucción como prompt principal:

```text
Construye el repositorio ECONOLIBRO_CODEX siguiendo exactamente este brief.

Prioriza estructura, claridad, reproducibilidad, utilidad pedagógica y calidad editorial.

No crees una aplicación web todavía.

No generes archivos vacíos. Cada archivo Markdown debe tener contenido inicial útil.

No inventes fuentes, autores, DOI ni resultados.

Asegura que el proyecto quede listo para producir libros de economía computacional con Python, notebooks reproducibles, ejercicios, datasets documentados y futura publicación en Quarto, Jupyter Book, PDF, EPUB, LMS o Amazon KDP.

El primer libro piloto será:

Economía Computacional con Python:
Datos, modelos y aplicaciones para estudiantes, docentes e investigadores en economía.

Crea toda la estructura de carpetas y archivos iniciales del proyecto.
```

---

# 29. Instrucción de trabajo para Codex en VS Code

Después de crear la carpeta local del proyecto, ejecutar:

```powershell
cd C:\Users\vinic\OneDrive\Escritorio\PROYECTOS
mkdir ECONOLIBRO_CODEX
cd ECONOLIBRO_CODEX
code .
```

Luego en Codex o Claude Code:

```text
Lee PROJECT_BRIEF.md y construye toda la estructura inicial del proyecto ECONOLIBRO_CODEX.

No crees archivos vacíos.

Crea README.md, AGENTS.md, ROADMAP.md, requirements.txt, environment.yml, pyproject.toml, .gitignore, carpetas principales, prompts, workflows, templates, rubrics, examples, publishing y docs.

Cada archivo Markdown debe tener contenido útil inicial.

Respeta la regla de no modificar data/raw y de usar data/processed para datos derivados.
```

---

# 30. Resultado esperado del primer sprint

Al finalizar el primer sprint, el repositorio debe contener:

```text
ECONOLIBRO_CODEX/
├── README.md
├── AGENTS.md
├── PROJECT_BRIEF.md
├── ROADMAP.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── environment.yml
├── pyproject.toml
├── book/
├── chapters/
├── notebooks/
├── scripts/
├── data/
├── outputs/
├── exercises/
├── prompts/
├── skills/
├── workflows/
├── templates/
├── rubrics/
├── examples/
├── publishing/
└── docs/
```

El proyecto debe quedar listo para empezar la escritura del primer libro:

```text
Economía Computacional con Python
```

y preparado para escalar hacia la colección completa:

```text
Serie Econolab Computacional
```
