# Soluciones docentes - Capitulo 1

## Criterios de revision

- La respuesta diferencia herramienta computacional y argumento economico.
- La pregunta economica incluye poblacion, periodo, variable o comparacion.
- La unidad de observacion esta claramente definida.
- La fuente de datos es real y puede verificarse.
- La estructura de carpetas separa datos, notebooks y outputs.
- Las rutas usan `pathlib` y no dependen del computador del estudiante.
- La interpretacion evita afirmar causalidad sin identificacion.

## Guia orientativa por ejercicio

### Ejercicio conceptual 1

Una buena respuesta debe decir que Python puede automatizar tareas, pero la
economia computacional exige conectar codigo con teoria, medicion e
interpretacion. El codigo es un medio, no el argumento.

### Ejercicio conceptual 2

Respuesta esperada:

```text
Como cambio la tasa de empleo de jovenes de 18 a 29 anos entre dos periodos
usando una encuesta laboral oficial?
```

La pregunta es mejor porque define poblacion, variable, periodo y fuente
potencial.

### Ejercicio conceptual 3

Ejemplos aceptables:

- Encuesta de hogares: una persona o un hogar.
- Serie macroeconomica: un pais en un mes, trimestre o ano.
- Datos de empresas: una empresa en un periodo contable.

### Ejercicio conceptual 4

La diferencia promedio puede reflejar composicion, seleccion, experiencia,
region, edad u otros factores. Para hablar de efecto causal se necesita una
estrategia de identificacion y supuestos defendibles.

### Ejercicio conceptual 5

Riesgos esperados:

- usar variables con definiciones equivocadas;
- mezclar periodos con cambios metodologicos;
- ignorar factores de expansion o diseno muestral;
- perder observaciones por filtros no documentados;
- interpretar como poblacional algo que no representa a la poblacion.

## Guia del mini-proyecto

La entrega no se evalua por descargar datos ni por producir resultados. Se
evalua por calidad de formulacion, trazabilidad de la fuente y prudencia
interpretativa.

## Rubrica breve

| Criterio | Excelente | A mejorar |
|---|---|---|
| Pregunta | Observable, acotada y economicamente relevante | Amplia o ambigua |
| Fuente | Real, verificable y pertinente | No verificable o poco relacionada |
| Variables | Conectadas con la pregunta | Listadas sin justificacion |
| Reproducibilidad | Usa rutas relativas y salida regenerable | Depende de rutas personales |
| Interpretacion | Declara limites | Sobreinterpreta resultados |
