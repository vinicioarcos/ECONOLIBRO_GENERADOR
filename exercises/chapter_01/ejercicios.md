# Ejercicios - Capitulo 1

## Resultados de aprendizaje asociados

- Explicar que es la economia computacional.
- Formular preguntas economicas observables.
- Documentar fuentes de datos antes de usarlas.
- Usar una estructura reproducible con rutas relativas.
- Interpretar resultados con cautela.

## Ejercicios conceptuales

1. Explique la diferencia entre usar Python para automatizar calculos y usarlo
   para responder una pregunta economica.
2. Reescriba la pregunta "que pasa con el empleo?" como una pregunta economica
   medible. Incluya poblacion, periodo y comparacion.
3. Defina unidad de observacion usando un ejemplo de encuesta de hogares, un
   ejemplo de serie macroeconomica y un ejemplo de datos de empresas.
4. Explique por que una diferencia de ingresos promedio entre dos grupos no
   demuestra, por si sola, un efecto causal.
5. Describa tres riesgos de trabajar con una fuente de datos sin revisar su
   metodologia.

## Ejercicios computacionales

1. Abra el notebook `notebooks/chapter_01/intro_economia_computacional.ipynb` y
   ejecutelo de arriba hacia abajo.
2. Modifique la ficha de fuente de datos del notebook para una fuente economica
   real que quiera usar en el futuro.
3. Verifique que el notebook guarde una tabla en `outputs/tables`.
4. Revise que el codigo use `pathlib` y no tenga rutas absolutas.
5. Agregue una advertencia de interpretacion para la pregunta economica elegida.

## Mini-proyecto

Identifique una fuente de datos economicos real. No descargue datos todavia.
Entregue una ficha con:

- pregunta economica;
- institucion productora;
- enlace de acceso;
- periodo disponible;
- unidad de observacion;
- variables clave;
- producto esperado;
- limites de interpretacion.

## Criterios de entrega

- La pregunta debe ser observable con datos.
- La fuente debe ser real y verificable.
- La ficha debe separar descripcion de interpretacion causal.
- Las rutas del notebook deben ser relativas.
- La salida debe poder regenerarse al ejecutar el notebook.
