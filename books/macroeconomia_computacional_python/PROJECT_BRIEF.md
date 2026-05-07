# PROJECT_BRIEF - Macroeconomía Computacional con Python

## Nombre del libro

**Macroeconomía Computacional con Python**

## Subtitulo

**Modelos, simulación, datos y política macroeconómica reproducible**

## Publico objetivo

- Estudiantes de economía con Python básico.
- Docentes de macroeconomía, econometría aplicada y métodos cuantitativos.
- Tesistas que necesitan pasar de modelos teoricos a evidencia reproducible.
- Analistas de bancos centrales, ministerios, centros de investigacion y
  consultoras.

## Nivel

Intermedio inicial. Requiere álgebra básica, lectura de gráficos, nociones de
macroeconomía y capacidad para ejecutar notebooks de Python.

## Promesa de aprendizaje

Al finalizar el libro, el lector podrá convertir preguntas macroeconómicas en
modelos computacionales trazables, simular escenarios, trabajar con series
macroeconómicas, construir indicadores, estimar modelos descriptivos y comunicar
resultados sin confundir simulación, correlación, predicción y causalidad.

## Tesis editorial

La macroeconomía computacional no reemplaza la teoría macroeconómica: la vuelve
ejecutable. Programar un modelo obliga a declarar supuestos, parámetros,
unidades, mecanismos y límites de interpretación.

## Fuentes de datos sugeridas

- Banco Central del Ecuador para cuentas nacionales, precios, sector externo y
  estadisticas monetarias locales.
- FRED del Federal Reserve Bank of St. Louis para series macroeconomicas
  internacionales.
- World Development Indicators del Banco Mundial para comparaciones de largo
  plazo.
- CEPALSTAT para indicadores regionales de America Latina.
- INEC Ecuador para mercado laboral, precios y condiciones sociales.

## Indice maestro preliminar

### Parte I. Fundamentos computacionales de macroeconomia

1. Del relato macroeconomico al modelo computacional.
2. Series macroeconomicas, frecuencia y transformaciones.
3. Cuentas nacionales y medicion del PIB.
4. Inflacion, indices de precios y poder adquisitivo.

### Parte II. Ciclos, demanda agregada y politica fiscal

5. Brechas del producto y componentes ciclicos.
6. Multiplicador keynesiano y escenarios fiscales.
7. Consumo, ingreso disponible y estabilizadores automaticos.
8. Inversion, expectativas y sensibilidad al ciclo.

### Parte III. Dinamica monetaria y sector externo

9. Dinero, tasas de interes e inflacion.
10. Reglas de politica monetaria y simulacion de shocks.
11. Tipo de cambio, balanza de pagos y apertura.
12. Terminos de intercambio y vulnerabilidad externa.

### Parte IV. Crecimiento, productividad y distribucion

13. Contabilidad del crecimiento.
14. Modelo de Solow computacional.
15. Capital humano, productividad y convergencia.
16. Macroeconomia y desigualdad agregada.

### Parte V. Modelos empiricos y comunicacion

17. VAR descriptivos y funciones impulso-respuesta.
18. Pronosticos macroeconomicos con cautela.
19. Escenarios de politica y analisis de sensibilidad.
20. Proyecto final reproducible.

## Productos complementarios

- Notebooks ejecutables por capitulo.
- Datos simulados o procesados con metadatos.
- Tablas y figuras interpretadas.
- Ejercicios conceptuales y computacionales con solucion docente.
- Diapositivas academicas en HTML, PDF y PowerPoint.
- Entregables PDF generados con Quarto.

## Reglas obligatorias del libro

1. Separar simulacion, descripcion empirica, prediccion y causalidad.
2. No inventar fuentes, autores, DOI ni resultados.
3. Mantener `data/raw` intacta.
4. Guardar transformaciones en `data/processed`.
5. Documentar parametros, periodo, unidades y supuestos.
6. No afirmar efectos de politica sin identificacion o sin declarar que se trata
   de un escenario simulado.
7. Toda figura debe incluir interpretacion y advertencias.

## Proximo sprint sugerido

Desarrollar el capitulo 2 sobre series macroeconomicas, frecuencia temporal,
deflactacion, tasas de crecimiento y filtros descriptivos.
