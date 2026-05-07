# Ejercicios - Capítulo 3

## Resultados de aprendizaje asociados

- Representar información económica simple con variables, listas y
  diccionarios.
- Crear funciones para indicadores básicos.
- Usar condicionales y bucles.
- Exportar salidas reproducibles.
- Diferenciar ejemplo didáctico y evidencia empírica.

## Ejercicios conceptuales

1. Explique la diferencia entre una variable de Python y una variable económica
   bien definida.
2. ¿Por qué el ingreso total del hogar puede ser menos comparable que el ingreso
   per cápita?
3. Explique por qué una función reduce errores cuando se repite un cálculo.
4. ¿Qué riesgo aparece si se mezclan datos simulados con datos oficiales?
5. ¿Por qué una clasificación con un umbral didáctico no equivale a una medición
   oficial de pobreza?

## Ejercicios computacionales

1. Ejecute `notebooks/chapter_03/python_basico_economistas.ipynb` de arriba
   hacia abajo.
2. Verifique que se cree `data/processed/chapter_03_hogares_simulados.csv`.
3. Verifique que se cree `outputs/tables/chapter_03_resumen_hogares.csv`.
4. Verifique que se cree `outputs/figures/chapter_03_ingreso_per_capita.svg`.
5. Agregue dos hogares simulados al notebook y vuelva a ejecutar todo.
6. Cambie el umbral didáctico de vulnerabilidad y explique cómo cambia la
   clasificación.

## Mini-proyecto

Cree una base simulada con diez observaciones sobre un tema económico sencillo:
hogares, estudiantes, trabajadores o pequeñas empresas. Debe incluir:

- al menos tres variables originales;
- un indicador derivado calculado con una función;
- una clasificación usando condicionales;
- una tabla exportada a `outputs/tables`;
- una nota metodológica que declare que los datos son simulados.

## Criterios de entrega

- El notebook debe ejecutarse completo.
- Las rutas deben ser relativas.
- `data/raw` no debe modificarse.
- Los nombres de variables deben ser claros.
- La interpretación debe indicar que los datos son simulados.
- La solución debe incluir tabla o reporte exportado.
