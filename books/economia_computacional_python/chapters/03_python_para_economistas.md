# Capítulo 03. Python básico para economistas

## 1. Apertura

### Pregunta motivadora

¿Cómo puede un economista usar Python para convertir observaciones económicas
simples en variables, indicadores, tablas, gráficos y argumentos reproducibles?

### Caso aplicado

Un estudiante recibe una pequeña base didáctica con hogares simulados: ingreso
mensual, número de miembros y horas trabajadas. Antes de descargar una encuesta
real, necesita aprender a representar esos datos en Python, calcular indicadores
básicos, detectar errores y guardar resultados en las carpetas correctas del
proyecto.

El objetivo no es estimar pobreza real ni describir un país. El objetivo es
aprender las estructuras mínimas de Python que luego permitirán trabajar con
fuentes verificadas.

### Por qué importa

Python no es valioso para economía porque permita escribir código largo. Es
valioso porque permite repetir cálculos, documentar supuestos, separar datos
originales de productos derivados y revisar cada paso entre una pregunta
económica y una conclusión.

Si un estudiante entiende variables, listas, diccionarios, funciones y rutas
relativas, puede leer notebooks más avanzados con menos ansiedad y más criterio.

## 2. Resultados de aprendizaje

Al finalizar este capítulo, el lector será capaz de:

1. Crear variables, listas y diccionarios para representar información
   económica simple.
2. Diferenciar tipos de datos comunes en Python: números, cadenas, booleanos y
   colecciones.
3. Escribir funciones pequeñas para calcular indicadores económicos.
4. Usar condicionales y bucles para clasificar observaciones.
5. Exportar tablas, figuras y reportes usando rutas relativas.
6. Interpretar resultados didácticos sin presentarlos como evidencia empírica.

## 3. Conceptos clave

- Variable.
- Tipo de dato.
- Lista.
- Diccionario.
- Función.
- Bucle.
- Condicional.
- Ingreso per cápita.
- Clasificación.
- Reproducibilidad.

## 4. Intuición económica

Muchos problemas económicos comienzan con una operación sencilla: dividir,
comparar, agrupar o clasificar. Por ejemplo, el ingreso total de un hogar no se
interpreta igual si vive una persona que si viven cinco. Una transformación
simple como el ingreso per cápita cambia la escala de análisis y permite una
comparación más razonable.

Python ayuda a expresar esas operaciones de forma explícita. En lugar de
calcular manualmente cada fila, escribimos una regla general y la aplicamos a
todas las observaciones. Esa regla queda visible para revisión docente,
replicación y corrección.

La idea central del capítulo es que programar no significa decorar el análisis
con tecnología. Programar significa transformar una pregunta económica en pasos
lógicos que otra persona puede leer, ejecutar y discutir.

## 5. Formalización mínima

Para un hogar \(i\), el ingreso per cápita mensual se define como:

```text
ingreso_per_capita_i = ingreso_total_i / miembros_i
```

Una clasificación didáctica puede escribirse como:

```text
vulnerable_i = ingreso_per_capita_i < umbral
```

Esta clasificación no mide pobreza oficial. Para medir pobreza real se necesita
una metodología institucional, una fuente de datos oficial, ponderadores y una
línea de pobreza documentada.

## 6. Datos

El notebook del capítulo usa una base simulada de hogares. La base contiene
identificador del hogar, ingreso mensual, miembros del hogar, horas trabajadas y
zona ficticia. Estas variables permiten practicar cálculo de indicadores sin
afirmar resultados sobre una población real.

| Variable | Descripción |
|---|---|
| `hogar_id` | Identificador ficticio del hogar |
| `ingreso_mensual` | Ingreso mensual simulado |
| `miembros` | Número simulado de miembros del hogar |
| `horas_trabajadas` | Horas mensuales simuladas |
| `zona` | Zona ficticia urbana o rural |

Los datos son creados dentro del notebook. La base derivada didáctica se guarda
en `data/processed` para mantener intacta la carpeta `data/raw`:

```text
data/processed/chapter_03_hogares_simulados.csv
```

No se modifica `data/raw`.

## 7. Implementación en Python

El notebook asociado está en:

```text
notebooks/chapter_03/python_basico_economistas.ipynb
```

El flujo realiza:

1. define variables y tipos de datos;
2. crea una lista de diccionarios con hogares simulados;
3. implementa funciones para calcular ingreso per cápita e ingreso por hora;
4. clasifica hogares con una regla condicional didáctica;
5. exporta una tabla CSV, una figura SVG y un reporte metodológico;
6. explica por qué los resultados no son evidencia real.

## 8. Resultados

Al ejecutar el notebook se generan:

```text
data/processed/chapter_03_hogares_simulados.csv
outputs/tables/chapter_03_resumen_hogares.csv
outputs/figures/chapter_03_ingreso_per_capita.svg
outputs/reports/chapter_03_nota_metodologica.md
```

La figura compara ingresos per cápita simulados por hogar. Su única función es
mostrar el flujo de código a salida reproducible.

## 9. Interpretación económica

El ingreso per cápita permite aproximar la capacidad económica individual dentro
de un hogar, pero no resume por completo bienestar, pobreza ni vulnerabilidad.
También importan precios locales, acceso a servicios, composición del hogar,
activos, deudas, transferencias y condiciones territoriales.

En este capítulo la interpretación correcta es técnica y pedagógica: aprendimos
a representar datos, construir variables y guardar resultados. No aprendimos una
verdad empírica sobre hogares reales.

## 10. Errores frecuentes

- Creer que una variable en Python es igual a una variable económica bien
  definida.
- Usar nombres poco claros como `x`, `y` o `dato1`.
- Dividir por cero al calcular indicadores por persona u hora.
- Escribir la misma operación muchas veces en vez de crear una función.
- Mezclar datos simulados con datos oficiales.
- Guardar derivados en `data/raw`.
- Interpretar un ejemplo didáctico como si fuera evidencia real.

## 11. Ejercicios

Los ejercicios están en:

```text
exercises/chapter_03/ejercicios.md
```

La guía docente está en:

```text
exercises/chapter_03/soluciones_docente.md
```

## 12. Mini-proyecto

Cree una base simulada de diez hogares o estudiantes. Defina al menos tres
variables, construya un indicador derivado, clasifique observaciones con una
regla explícita y exporte una tabla. Incluya una nota metodológica que declare
que los datos son simulados.

## 13. Lecturas recomendadas

Para esta unidad se recomienda consultar documentación oficial y material
técnico verificable:

- Documentación oficial de Python sobre tipos de datos incorporados.
- Documentación oficial de Python sobre funciones.
- Documentación oficial de `pathlib`.
- Guía oficial de Jupyter Notebook para ejecución ordenada de celdas.

No se incluyen DOI ni referencias bibliográficas no verificadas en esta versión
del capítulo.

## 14. Resumen del capítulo

Este capítulo introdujo Python como lenguaje para representar información
económica básica y convertir reglas de cálculo en resultados reproducibles.
Trabajamos con variables, listas, diccionarios, funciones, bucles y
condicionales.

La lección principal es metodológica: antes de usar bases grandes, modelos o
visualizaciones complejas, el economista debe poder explicar cada transformación
que aplica a los datos.

## 15. Checklist de aprendizaje

- [ ] Puedo crear variables económicas simples en Python.
- [ ] Puedo usar listas y diccionarios para representar observaciones.
- [ ] Puedo escribir una función pequeña y reutilizable.
- [ ] Puedo usar condicionales para clasificar observaciones.
- [ ] Puedo exportar resultados sin modificar `data/raw`.
- [ ] Puedo explicar por qué un dato simulado no es evidencia empírica.
