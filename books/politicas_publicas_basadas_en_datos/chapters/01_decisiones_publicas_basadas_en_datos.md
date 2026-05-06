# Capítulo 01. Decisiones públicas basadas en datos

## 1. Apertura

### Pregunta motivadora

Que significa tomar una decision publica basada en datos sin reducir la politica
publica a un tablero, una correlacion o un modelo predictivo?

### Caso aplicado

Un gobierno local quiere priorizar barrios para mejorar servicios de cuidado
infantil. Tiene datos administrativos de asistencia, cupos disponibles,
solicitudes no atendidas y distancia a centros. Tambien recibe presion politica
de varios sectores. La tarea tecnica no es reemplazar la decision publica, sino
ordenar evidencia, explicitar criterios y advertir limites.

### Por que importa

Los datos pueden mejorar la asignacion de recursos, detectar brechas y hacer
seguimiento de metas. Pero tambien pueden reforzar sesgos, ocultar poblaciones no
registradas o producir una falsa precision. La politica publica exige combinar
evidencia, teoria, derechos, presupuesto, factibilidad y deliberacion.

## 2. Resultados de aprendizaje

Al finalizar este capitulo, el lector sera capaz de:

1. Definir una politica publica basada en datos con criterios institucionales y
   tecnicos.
2. Diferenciar diagnostico, monitoreo, prediccion y evaluacion causal.
3. Construir una cadena minima entre problema publico, datos, indicador,
   decision y rendicion de cuentas.
4. Identificar riesgos de sesgo, privacidad y sobreinterpretacion.
5. Usar Python para organizar una matriz reproducible de evidencia y decisiones.

## 3. Conceptos clave

- Problema publico.
- Evidencia.
- Indicador.
- Unidad de analisis.
- Poblacion objetivo.
- Teoria del cambio.
- Monitoreo.
- Evaluacion de impacto.
- Prediccion.
- Rendicion de cuentas.

## 4. Intuicion economica

Toda politica publica enfrenta escasez. No hay presupuesto, tiempo, personal ni
capacidad administrativa ilimitada. Por eso las decisiones publicas requieren
criterios para priorizar. Los datos ayudan a observar magnitud, distribucion,
tendencias y posibles brechas, pero no determinan por si solos que valor social
debe maximizarse.

La economia aporta una pregunta central: que asignacion de recursos produce
mejores resultados sociales dadas las restricciones existentes? La respuesta
depende de informacion, incentivos, costos de oportunidad y efectos esperados.
Los datos mejoran esa informacion, pero no eliminan la necesidad de juicio
publico.

## 5. Formalizacion minima

Una decision publica basada en datos puede representarse como una cadena:

```text
Problema -> poblacion objetivo -> indicador -> criterio -> accion -> monitoreo
```

El indicador no es la politica. Es una medicion parcial que debe cumplir al
menos cuatro condiciones:

1. definicion clara;
2. fuente verificable;
3. unidad de analisis explicita;
4. interpretacion compatible con el problema.

## 6. Datos

Este capitulo no usa aun microdatos oficiales. El notebook asociado construye
una matriz didactica de decisiones con datos simulados y declarados como tales.
Su objetivo es practicar trazabilidad: cada fila conecta una pregunta de
politica con un indicador, una fuente potencial, un uso y una advertencia.

Para aplicaciones reales se deben documentar fuente, fecha de descarga,
diccionario, filtros, periodo, cobertura, ponderadores y restricciones de uso.

## 7. Implementacion en Python

El notebook asociado esta en:

```text
books/politicas_publicas_basadas_en_datos/notebooks/chapter_01/pipeline_decision_publica.ipynb
```

El flujo realiza:

1. crea una matriz pedagogica de problemas, indicadores y decisiones;
2. clasifica cada uso como diagnostico, monitoreo, prediccion o evaluacion;
3. exporta una tabla trazable;
4. genera una figura simple sobre tipos de uso de evidencia;
5. registra una nota metodologica para evitar interpretar datos simulados como
   evidencia real.

## 8. Resultados

Al ejecutarse, el notebook genera:

```text
outputs/tables/chapter_01_matriz_decision_publica.csv
outputs/figures/chapter_01_usos_evidencia.png
outputs/reports/chapter_01_nota_metodologica.md
```

Los resultados son pedagogicos. No describen una institucion real.

## 9. Interpretacion economica

Una matriz de evidencia permite ordenar decisiones bajo escasez. Si una politica
prioriza solo magnitud del problema, puede ignorar equidad. Si prioriza solo
factibilidad, puede abandonar a poblaciones con mayores barreras. Si prioriza
solo prediccion, puede optimizar un resultado medible y omitir derechos o
restricciones legales.

La interpretacion economica debe preguntar: que objetivo se persigue, que costo
de oportunidad existe, quien gana, quien pierde, que incertidumbre persiste y
como se rendiran cuentas?

## 10. Errores frecuentes

- Confundir un tablero con una politica publica.
- Usar correlaciones como si fueran efectos causales.
- No declarar la unidad de analisis.
- Medir solo lo facil y omitir lo importante.
- Ignorar poblaciones fuera de registros administrativos.
- Usar modelos predictivos sin revisar sesgos.
- Recomendar acciones sin costos, restricciones ni incertidumbre.

## 11. Ejercicios

Ver:

```text
books/politicas_publicas_basadas_en_datos/exercises/chapter_01/ejercicios.md
```

## 12. Mini-proyecto

Seleccione un problema publico local. Construya una matriz con problema,
poblacion objetivo, indicador, fuente potencial, criterio de decision,
advertencia etica y posible producto de comunicacion. No use resultados
empiricos si no tiene datos reales documentados.

## 13. Lecturas recomendadas

- Documentacion metodologica de la fuente oficial que se vaya a usar.
- Guias institucionales de monitoreo y evaluacion del organismo responsable.
- Textos de evaluacion de impacto y analisis de politica publica que distingan
  diagnostico, monitoreo y causalidad.

No se incluyen DOI ni ediciones no verificadas en este borrador inicial.

## 14. Resumen del capitulo

Una politica publica basada en datos requiere evidencia verificable, teoria del
cambio, criterios normativos y prudencia interpretativa. Los datos ayudan a
decidir mejor, pero no sustituyen la deliberacion publica ni la responsabilidad
institucional.

## 15. Checklist de aprendizaje

- [ ] Puedo diferenciar diagnostico, monitoreo, prediccion y evaluacion causal.
- [ ] Puedo explicar por que un indicador no equivale a una politica.
- [ ] Puedo construir una matriz de evidencia para una decision publica.
- [ ] Puedo identificar riesgos de sesgo, privacidad y sobreinterpretacion.
- [ ] Puedo documentar advertencias antes de recomendar una accion.
