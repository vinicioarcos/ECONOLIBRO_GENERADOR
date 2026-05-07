# Capítulo 01. Del relato macroeconómico al modelo computacional

## 1. Apertura

### Pregunta motivadora

¿Cómo pasamos de una intuición macroeconómica, por ejemplo "un aumento del gasto
público eleva la producción en el corto plazo", a un modelo computacional que
explicite supuestos, parámetros, resultados y límites?

### Caso aplicado

Un equipo docente quiere explicar el multiplicador de la demanda agregada sin
presentarlo como una verdad mecanica. Para hacerlo, construye una economia
simulada con consumo, impuestos, importaciones, inversion, gasto publico y
exportaciones netas. Luego compara escenarios y pregunta: que cambia cuando la
propension a consumir es mayor, cuando las importaciones responden mas al ingreso
o cuando el ajuste de la produccion es gradual?

### Por que importa

La macroeconomia trabaja con objetos agregados: producto, consumo, inversion,
precios, empleo, sector externo y politica economica. Esos objetos no se ven de
forma directa; se miden, se modelan y se interpretan. Python permite volver
auditable ese proceso: cada ecuacion queda escrita, cada parametro queda
documentado y cada grafico puede reproducirse.

## 2. Resultados de aprendizaje

Al finalizar este capitulo, el lector sera capaz de:

1. Distinguir relato economico, modelo teorico, simulacion y evidencia empirica.
2. Representar un modelo simple de demanda agregada en Python.
3. Simular escenarios macroeconomicos con parametros documentados.
4. Exportar datos simulados, tablas y figuras usando rutas relativas.
5. Interpretar multiplicadores como resultados condicionados a supuestos.
6. Evitar afirmaciones causales cuando solo se presenta una simulacion.

## 3. Conceptos clave

- Variable endogena.
- Variable exogena.
- Parametro.
- Escenario base.
- Shock.
- Multiplicador.
- Ingreso disponible.
- Propension marginal a consumir.
- Propension marginal a importar.
- Simulacion.
- Sensibilidad de parametros.
- Trazabilidad.

## 4. Intuicion economica

Un relato macroeconomico organiza una intuicion: si aumenta la demanda agregada,
las empresas pueden producir mas mientras exista capacidad ociosa. Un modelo
convierte esa intuicion en una estructura: define que variables se determinan
dentro del sistema, que variables se tratan como externas y que parametros
resumen comportamientos.

La simulacion no prueba que una politica funcione en el mundo real. Sirve para
preguntar que se seguiria logicamente de un conjunto de supuestos. Por eso su
valor pedagogico esta en la transparencia: si cambia la propension a consumir,
el multiplicador cambia; si aumentan las importaciones inducidas, parte del
impulso de demanda se filtra hacia el exterior; si el ajuste de la produccion es
lento, el efecto aparece gradualmente.

## 5. Formalizacion minima

Usaremos una economia cerrada parcialmente al comercio, con impuestos
proporcionales e importaciones inducidas:

```text
Y = C + I + G + XN
C = C0 + c * (1 - t) * Y
XN = X0 - m * Y
```

Al sustituir, el producto de equilibrio es:

```text
Y* = (C0 + I + G + X0) / (1 - c * (1 - t) + m)
```

El multiplicador del gasto publico, dentro de este modelo estatico, es:

```text
dY*/dG = 1 / (1 - c * (1 - t) + m)
```

Esta expresion no es una estimacion empirica. Es una consecuencia algebraica de
las ecuaciones elegidas.

## 6. Datos

El capitulo usa datos simulados generados por el notebook:

```text
books/macroeconomia_computacional_python/notebooks/chapter_01/modelo_demanda_agregada_simulado.ipynb
```

No se modifica `data/raw`. Los datos derivados se guardan en:

```text
books/macroeconomia_computacional_python/data/processed/chapter_01_escenarios_demanda_agregada.csv
```

Cada fila representa un periodo simulado y un escenario. Las variables incluyen
producto observado en la simulacion, producto de equilibrio, consumo, inversion,
gasto publico, exportaciones netas, impuestos netos e importaciones inducidas.

## 7. Implementacion en Python

El flujo computacional del notebook es:

1. declarar parametros pedagogicos del modelo;
2. calcular el equilibrio estatico del escenario base;
3. construir escenarios con distinto gasto publico y distinta apertura externa;
4. simular ajuste dinamico gradual hacia el equilibrio;
5. exportar una tabla de multiplicadores;
6. exportar una figura comparativa de trayectorias del producto;
7. registrar metadatos para que el lector sepa que los datos son simulados.

La idea didactica no es "hacer macroeconomia con muchas lineas de codigo", sino
convertir cada supuesto en una decision visible.

## 8. Resultados

El notebook genera:

```text
books/macroeconomia_computacional_python/data/processed/chapter_01_escenarios_demanda_agregada.csv
books/macroeconomia_computacional_python/outputs/tables/chapter_01_multiplicadores.csv
books/macroeconomia_computacional_python/outputs/figures/chapter_01_trayectorias_producto.svg
books/macroeconomia_computacional_python/outputs/reports/chapter_01_metadata_simulacion.md
```

La tabla permite comparar el producto de equilibrio antes y después del shock.
La figura muestra que el escenario con mayor apertura externa tiene un
multiplicador menor, porque una parte mayor del aumento de ingreso se transforma
en importaciones. El shock fiscal sin cambio de apertura alcanza un producto de
equilibrio más alto que el escenario base, pero esa conclusión solo vale dentro
del modelo simulado.

## 9. Interpretacion economica

El multiplicador no es una constante universal. Depende de la propension
marginal a consumir, la tasa impositiva, la propension marginal a importar, la
capacidad de respuesta de la oferta y las expectativas. En este capitulo
mantuvimos muchos elementos fuera del modelo para que la estructura inicial sea
comprensible.

Tampoco podemos afirmar que una política fiscal concreta tendrá el mismo efecto
en una economía real. Para eso se requieren datos observados, estrategia
empírica, contexto institucional y evaluación de supuestos.

## 10. Errores frecuentes

- Tratar una simulacion como si fuera evidencia empirica.
- Llamar causal a un resultado que solo proviene de ecuaciones supuestas.
- Cambiar parametros sin documentar el motivo.
- Mezclar datos simulados con datos observados en el mismo archivo.
- Guardar datos procesados en `data/raw`.
- Interpretar el multiplicador sin mencionar impuestos, importaciones y
  capacidad ociosa.
- Usar rutas absolutas del computador del autor.

## 11. Ejercicios

Ver:

```text
books/macroeconomia_computacional_python/exercises/chapter_01/ejercicios.md
```

## 12. Mini-proyecto

Construya tres escenarios fiscales alternativos. En cada uno cambie un solo
parametro central: gasto publico, propension a consumir o propension a importar.
Exporte una tabla y una figura. Escriba una interpretacion de maximo una pagina
que explique que cambia, por que cambia y que no puede concluirse.

## 13. Lecturas recomendadas

- Sargent y Stachurski, QuantEcon: *A First Course in Quantitative Economics
  with Python*.
- Sargent y Stachurski, QuantEcon: capitulo sobre ciclos economicos.
- Federal Reserve Bank of St. Louis: FRED Economic Data, como fuente para
  futuras practicas con series observadas.
- Banco Mundial: World Development Indicators, como fuente para comparaciones
  internacionales.

Estas lecturas se recomiendan como orientacion verificable. Este capitulo no
usa datos descargados desde esas fuentes.

## 14. Resumen del capitulo

La macroeconomía computacional empieza al convertir una pregunta agregada en un
objeto reproducible. Un modelo simple de demanda agregada permite ver como los
supuestos determinan los resultados. Python ayuda a documentar, simular,
comparar y comunicar, pero no elimina la responsabilidad económica de
interpretar con cautela.

## 15. Checklist de aprendizaje

- [ ] Puedo explicar la diferencia entre relato, modelo, simulacion y evidencia.
- [ ] Puedo identificar variables endogenas, exogenas y parametros.
- [ ] Puedo implementar el equilibrio de demanda agregada en Python.
- [ ] Puedo exportar datos simulados a `data/processed`.
- [ ] Puedo crear una tabla y una figura reproducibles.
- [ ] Puedo interpretar multiplicadores sin afirmar causalidad empirica.
