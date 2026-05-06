# Capitulo 01. Datos financieros con Python

## 1. Apertura

### Pregunta motivadora

Como podemos descargar precios financieros desde internet y convertirlos en una
base reproducible para analizar retornos, riesgo y volatilidad?

### Caso aplicado

Un analista quiere comparar el comportamiento reciente de un ETF de mercado, una
accion tecnologica y Bitcoin. Los precios estan disponibles en internet, pero
antes de modelar necesita decidir que fuente usar, que campo de precio tomar,
como calcular retornos y que advertencias declarar.

### Por que importa

En finanzas, pequenas decisiones tecnicas cambian la interpretacion: precio de
cierre o precio ajustado, frecuencia diaria o mensual, retornos simples o
logaritmicos, muestra corta o larga, activos con horarios distintos. Este
capitulo establece un flujo reproducible para no confundir descarga de datos con
evidencia financiera.

## 2. Resultados de aprendizaje

Al finalizar este capitulo, el lector sera capaz de:

1. Descargar precios financieros desde internet usando `yfinance`.
2. Documentar fuente, tickers, periodo y fecha de descarga.
3. Diferenciar precios de cierre y precios ajustados.
4. Calcular retornos simples y logaritmicos.
5. Exportar datos procesados, tablas y figuras a carpetas del proyecto.
6. Interpretar retornos sin afirmar prediccion ni causalidad.

## 3. Conceptos clave

- Ticker.
- Precio de cierre.
- Precio ajustado.
- Retorno simple.
- Retorno logaritmico.
- Rendimiento acumulado.
- Volatilidad.
- Frecuencia de datos.
- Fuente de mercado.
- Trazabilidad.

## 4. Intuicion economica

Un precio financiero resume informacion de mercado en un momento dado. Pero los
modelos financieros rara vez trabajan directamente con precios, porque los
precios suelen ser no estacionarios y dependen de escalas diferentes. Por eso se
transforman en retornos.

El retorno permite comparar activos de distinto precio inicial. Un movimiento de
1 dolar no significa lo mismo en una accion de 10 dolares que en una accion de
500 dolares. El retorno expresa el cambio relativo.

## 5. Formalizacion minima

El retorno simple entre dos fechas es:

```text
R_t = (P_t - P_{t-1}) / P_{t-1}
```

El retorno logaritmico es:

```text
r_t = log(P_t) - log(P_{t-1})
```

En muestras diarias, los retornos logaritmicos suelen ser utiles porque se
agregan por suma aproximada en el tiempo. Aun asi, la eleccion debe explicarse.

## 6. Datos

Este capitulo usa `yfinance` para descargar precios desde Yahoo Finance. Es una
fuente practica para docencia y prototipos, pero debe documentarse con cautela.

El notebook inicial usa estos tickers:

| Ticker | Descripcion docente |
|---|---|
| SPY | ETF amplio del mercado estadounidense |
| AAPL | Accion individual de alta liquidez |
| BTC-USD | Bitcoin en dolares |

La fuente, fecha de descarga, periodo y variables se registran en outputs del
capitulo. Los datos derivados se guardan en `data/processed`.

## 7. Implementacion en Python

El notebook asociado esta en:

```text
books/econometria_financiera_python/notebooks/chapter_01/descarga_retornos_yfinance.ipynb
```

El flujo realiza:

1. descarga de precios;
2. seleccion de precio ajustado cuando esta disponible;
3. calculo de retornos logaritmicos;
4. tabla descriptiva de retornos;
5. figura de rendimiento acumulado;
6. exportacion de datos, tablas y figura.

## 8. Resultados

El notebook genera:

```text
data/processed/chapter_01_precios_y_retornos.csv
outputs/tables/chapter_01_estadisticas_retornos.csv
outputs/figures/chapter_01_rendimiento_acumulado.png
outputs/reports/chapter_01_metadata_descarga.md
```

Los resultados dependen de la fecha de descarga. Por eso el reporte de metadata
es parte del entregable.

## 9. Interpretacion economica

Una mayor volatilidad diaria no implica que un activo sea "mejor" o "peor". Un
retorno acumulado alto en la muestra tampoco prueba habilidad predictiva. En
este capitulo solo se describe el comportamiento observado de activos concretos
en un periodo descargado.

Las afirmaciones sobre eficiencia de mercado, primas de riesgo o prediccion
requieren capitulos posteriores y pruebas especificas.

## 10. Errores frecuentes

- Confundir precio con retorno.
- Comparar precios de activos con escalas distintas.
- Usar cierre no ajustado sin revisar dividendos o splits.
- Mezclar frecuencias sin documentarlo.
- Omitir fecha de descarga.
- Tratar `yfinance` como fuente oficial para publicacion formal.
- Interpretar desempeno pasado como prediccion.

## 11. Ejercicios

Ver:

```text
books/econometria_financiera_python/exercises/chapter_01/ejercicios.md
```

## 12. Mini-proyecto

Seleccione tres activos financieros, descargue precios, calcule retornos
logaritmicos, compare estadisticas descriptivas y escriba una interpretacion con
al menos tres advertencias metodologicas.

## 13. Lecturas recomendadas

Agregar referencias verificadas sobre econometria financiera, series de tiempo
financieras y documentacion tecnica de las fuentes usadas. No incluir DOI ni
ediciones sin verificar.

## 14. Resumen del capitulo

El primer paso de la econometria financiera es construir datos confiables. Este
capitulo mostro como pasar de precios descargados desde internet a retornos
analizables, manteniendo trazabilidad, salidas reproducibles y prudencia
interpretativa.

## 15. Checklist de aprendizaje

- [ ] Puedo descargar precios con `yfinance`.
- [ ] Puedo registrar tickers, fuente, periodo y fecha de descarga.
- [ ] Puedo calcular retornos simples y logaritmicos.
- [ ] Puedo guardar datos derivados en `data/processed`.
- [ ] Puedo exportar tablas y figuras.
- [ ] Puedo interpretar retornos sin prometer prediccion.
