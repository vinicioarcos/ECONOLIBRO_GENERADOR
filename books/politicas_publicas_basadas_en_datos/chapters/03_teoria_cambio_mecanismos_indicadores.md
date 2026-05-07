# Capítulo 03. Teoría del cambio, mecanismos e indicadores

## 1. Apertura

### Pregunta motivadora

¿Cómo se conecta un problema público con una intervención, un mecanismo esperado y un conjunto de indicadores que permitan aprender sin prometer causalidad no identificada?

### Caso aplicado

Una entidad local quiere reducir el abandono escolar en educación media. El
diagnóstico muestra ausentismo, dificultades de transporte, presión económica
en los hogares y baja conexión entre la escuela y las expectativas laborales de
los estudiantes. El equipo propone tutorías, apoyo de transporte y seguimiento
temprano de asistencia. La pregunta técnica no es solo qué indicador observar,
sino por qué se espera que esas acciones cambien el comportamiento de
estudiantes, hogares y escuelas.

### Por qué importa

Una política pública sin teoría del cambio puede terminar midiendo actividades
sin saber si se acercan al resultado esperado. Una teoría del cambio no prueba
impacto por sí misma, pero obliga a declarar supuestos, mecanismos, riesgos y
condiciones de implementación. Esa disciplina evita que el análisis de datos se
reduzca a listas de indicadores desconectados.

## 2. Resultados de aprendizaje

Al finalizar este capítulo, el lector será capaz de:

1. Diferenciar insumos, actividades, productos, resultados intermedios y
   resultados finales.
2. Formular mecanismos de cambio compatibles con teoría económica e
   institucional.
3. Diseñar indicadores trazables para cada eslabón de una teoría del cambio.
4. Distinguir indicadores de monitoreo, diagnóstico y evaluación causal.
5. Implementar en Python una matriz reproducible de teoría del cambio e
   indicadores.

## 3. Conceptos clave

- Teoría del cambio.
- Cadena de resultados.
- Mecanismo.
- Supuesto.
- Indicador.
- Línea base.
- Meta.
- Medio de verificación.
- Riesgo de implementación.
- Resultado intermedio.
- Resultado final.

## 4. Intuición económica

Una política pública intenta modificar restricciones, incentivos, información o
capacidades. Si el problema es abandono escolar, una transferencia puede cambiar
el costo de asistir a clases; una tutoría puede cambiar el rendimiento esperado;
un sistema de alertas puede cambiar la velocidad de respuesta institucional.
Cada intervención opera por un mecanismo distinto.

La teoría del cambio explicita esa lógica. En economía aplicada, la pregunta no
es únicamente si un indicador sube o baja, sino qué comportamiento debería
cambiar, para quién, bajo qué restricciones y con qué costos de oportunidad. Si
el mecanismo no es plausible, el indicador puede mejorar por razones ajenas a la
política o no cambiar aunque la implementación haya sido intensa.

## 5. Formalización mínima

Una cadena simple puede representarse así:

```text
insumos -> actividades -> productos -> resultados intermedios -> resultado final
```

Para cada eslabón se define al menos:

```text
indicador = variable observable + unidad de análisis + periodo + fuente
```

La teoría del cambio debe declarar supuestos:

```text
Si actividad A se implementa con cobertura C,
y la población objetivo enfrenta restricción R,
entonces el mecanismo M debería producir el resultado intermedio Y.
```

Esta afirmación es una hipótesis de política. No equivale a una estimación de
impacto causal.

## 6. Datos

El cuaderno del capítulo usa datos simulados sobre un programa ficticio de
retención escolar. Los datos se crean únicamente para enseñar el flujo:

- matriz de teoría del cambio;
- catálogo de indicadores;
- metas por indicador;
- semáforo de monitoreo;
- figura de avance por eslabón.

No se usan datos reales de estudiantes, hogares ni instituciones. Para una
aplicación real se requiere autorización, diccionario de variables, revisión de
confidencialidad, reglas de acceso y validación con la entidad responsable.

## 7. Implementación en Python

El cuaderno asociado está en:

```text
books/politicas_publicas_basadas_en_datos/notebooks/chapter_03/teoria_cambio_indicadores.ipynb
```

El flujo realiza:

1. crea una matriz de teoría del cambio para un programa ficticio;
2. define indicadores por eslabón, fuente potencial y frecuencia;
3. calcula brechas entre valor observado y meta;
4. clasifica el estado de cada indicador;
5. exporta tablas trazables;
6. genera una figura de avance;
7. registra una nota metodológica.

## 8. Resultados

Al ejecutarse, el cuaderno genera:

```text
outputs/tables/chapter_03_matriz_teoria_cambio.csv
outputs/tables/chapter_03_indicadores_monitoreo.csv
outputs/figures/chapter_03_avance_indicadores.png
outputs/reports/chapter_03_nota_metodologica.md
```

Los resultados son pedagógicos. No describen una política real ni estiman
impacto causal.

## 9. Interpretación económica

La matriz permite revisar si cada indicador responde a una pregunta de política.
Un indicador de producto, como número de tutorías realizadas, informa esfuerzo
operativo. Un indicador de resultado intermedio, como asistencia mensual,
aproxima un comportamiento que la intervención espera modificar. Un resultado
final, como permanencia escolar, requiere más tiempo, mejor diseño de medición y
posiblemente una estrategia de evaluación.

La interpretación debe evitar dos extremos. El primero es creer que ejecutar
actividades garantiza resultados. El segundo es exigir evidencia causal antes de
tener una implementación mínima monitoreable. La teoría del cambio ayuda a
ordenar el aprendizaje institucional entre esos dos extremos.

## 10. Errores frecuentes

- Confundir productos con resultados finales.
- Formular indicadores sin unidad de análisis ni periodo.
- Medir solo actividades porque son más fáciles de contar.
- Declarar metas sin línea base o sin fuente verificable.
- Usar la teoría del cambio como decoración narrativa.
- No declarar supuestos críticos de implementación.
- Presentar monitoreo descriptivo como impacto causal.
- Ignorar costos, capacidad operativa y restricciones legales.

## 11. Ejercicios

Ver:

```text
books/politicas_publicas_basadas_en_datos/exercises/chapter_03/ejercicios.md
```

## 12. Mini-proyecto

Seleccione un problema público y construya una teoría del cambio de una página.
Incluya población objetivo, mecanismo, cadena de resultados, tres indicadores,
fuente potencial, frecuencia de medición y una advertencia causal. No invente
valores empíricos.

## 13. Lecturas recomendadas

- Manuales institucionales de planificación, monitoreo y evaluación del sector
  público.
- Guías metodológicas de organismos productores de datos oficiales.
- Textos introductorios de evaluación de programas que distingan teoría del
  cambio, monitoreo e identificación causal.

No se incluyen DOI ni referencias específicas no verificadas en este borrador.

## 14. Resumen del capítulo

Una teoría del cambio conecta problema, intervención, mecanismo e indicadores.
Su valor no está en adornar un informe, sino en hacer verificables los supuestos
que sostienen una decisión pública. Los indicadores permiten monitorear la
cadena, pero no prueban impacto causal sin un diseño de evaluación apropiado.

## 15. Checklist de aprendizaje

- [ ] Puedo diferenciar insumos, actividades, productos y resultados.
- [ ] Puedo formular un mecanismo plausible de cambio.
- [ ] Puedo diseñar indicadores con unidad, periodo, fuente y frecuencia.
- [ ] Puedo explicar por qué monitoreo no equivale a evaluación de impacto.
- [ ] Puedo documentar supuestos y riesgos antes de recomendar una acción.
