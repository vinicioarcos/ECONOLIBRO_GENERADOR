# Capítulo 02. Diagnóstico de problemas públicos y priorización

## 1. Apertura

### Pregunta motivadora

Como se transforma una preocupacion social amplia en un diagnostico verificable
que permita priorizar acciones publicas?

### Caso aplicado

Un ministerio necesita decidir donde iniciar un programa de apoyo a empleo
juvenil. Varias zonas presentan desempleo, informalidad y abandono educativo. La
pregunta tecnica es como priorizar sin inventar precision: que indicadores
usar, como ponderarlos, que datos faltan y que decisiones no se pueden justificar
sin informacion adicional.

### Por que importa

Un mal diagnostico puede llevar recursos al lugar equivocado, excluir poblaciones
vulnerables o prometer impactos que no se pueden evaluar. La priorizacion no debe
ser una formula opaca; debe ser una decision transparente con criterios
explícitos.

## 2. Resultados de aprendizaje

Al finalizar este capitulo, el lector sera capaz de:

1. Formular un problema publico como brecha observable.
2. Definir poblacion objetivo, territorio, periodo y unidad de analisis.
3. Construir una matriz de priorizacion con criterios de necesidad,
   factibilidad y equidad.
4. Interpretar rankings como herramientas de decision, no como verdades
   absolutas.
5. Implementar un ejercicio reproducible de priorizacion en Python.

## 3. Conceptos clave

- Diagnostico.
- Brecha.
- Linea base.
- Poblacion objetivo.
- Priorizacion.
- Necesidad.
- Factibilidad.
- Equidad.
- Normalizacion.
- Sensibilidad.

## 4. Intuicion economica

La priorizacion aparece porque los recursos publicos son limitados. Si todas las
zonas tienen necesidades, el analista debe explicitar criterios para ordenar
intervenciones. Un criterio de necesidad atiende magnitud del problema; uno de
factibilidad observa capacidad de implementacion; uno de equidad corrige
desventajas acumuladas.

El peso de cada criterio es una decision normativa e institucional. Python ayuda
a hacerla transparente, reproducible y sensible a cambios de supuestos.

## 5. Formalizacion minima

Una forma simple de construir un puntaje de prioridad es:

```text
prioridad_i = w_n * necesidad_i + w_f * factibilidad_i + w_e * equidad_i
```

donde los pesos cumplen:

```text
w_n + w_f + w_e = 1
```

Este puntaje no identifica efectos causales. Solo ordena unidades segun criterios
observados o definidos.

## 6. Datos

El notebook del capitulo usa datos simulados de territorios ficticios. Cada
variable esta creada para ensenar el procedimiento, no para describir una
realidad empirica.

Para una aplicacion real se recomienda:

- usar una fuente oficial o registro administrativo autorizado;
- documentar cobertura y periodo;
- revisar missing values;
- aplicar ponderadores cuando corresponda;
- validar definiciones con el organismo productor.

## 7. Implementacion en Python

El notebook asociado esta en:

```text
books/politicas_publicas_basadas_en_datos/notebooks/chapter_02/priorizacion_diagnostico.ipynb
```

El flujo realiza:

1. crea un conjunto simulado de territorios;
2. normaliza criterios de necesidad, factibilidad y equidad;
3. calcula un puntaje de prioridad;
4. exporta una tabla de ranking;
5. genera una figura de priorizacion;
6. registra limitaciones metodologicas.

## 8. Resultados

Al ejecutarse, el notebook genera:

```text
outputs/tables/chapter_02_ranking_priorizacion.csv
outputs/figures/chapter_02_priorizacion.png
outputs/reports/chapter_02_nota_metodologica.md
```

Los rankings son demostrativos y no deben usarse para decisiones reales.

## 9. Interpretacion economica

Un ranking puede cambiar cuando cambian los pesos, la escala o la fuente de
datos. Por eso no basta presentar el primer lugar. La interpretacion debe
explicar que criterio domina, que unidades quedan cerca del umbral y que
informacion faltaria antes de asignar presupuesto.

En politica publica, la transparencia del criterio es parte de la calidad de la
decision. Una priorizacion reproducible permite discutir desacuerdos sin ocultar
supuestos.

## 10. Errores frecuentes

- Presentar un ranking como medicion objetiva definitiva.
- Mezclar indicadores con escalas distintas sin normalizar.
- Asignar pesos sin justificacion.
- Ignorar sensibilidad a cambios de ponderacion.
- Usar datos simulados como si fueran reales.
- Confundir priorizacion descriptiva con impacto causal.
- No documentar la poblacion objetivo.

## 11. Ejercicios

Ver:

```text
books/politicas_publicas_basadas_en_datos/exercises/chapter_02/ejercicios.md
```

## 12. Mini-proyecto

Disene una matriz de priorizacion para un problema publico real, pero complete
los valores solo si tiene datos verificables. Si no tiene datos, entregue la
estructura, la fuente potencial y el plan de validacion.

## 13. Lecturas recomendadas

- Manuales de monitoreo y evaluacion de programas publicos.
- Documentacion metodologica de encuestas y registros administrativos.
- Textos introductorios de evaluacion de impacto para distinguir priorizacion y
  estimacion causal.

No se incluyen referencias no verificadas en esta version inicial.

## 14. Resumen del capitulo

El diagnostico convierte una preocupacion publica en una brecha observable. La
priorizacion ordena unidades bajo criterios explicitos de necesidad,
factibilidad y equidad. Ninguna formula reemplaza la decision publica, pero una
formula transparente mejora la deliberacion.

## 15. Checklist de aprendizaje

- [ ] Puedo formular un problema publico como brecha medible.
- [ ] Puedo declarar poblacion objetivo, periodo y unidad de analisis.
- [ ] Puedo construir un puntaje de prioridad con pesos explicitos.
- [ ] Puedo explicar por que un ranking no prueba impacto causal.
- [ ] Puedo documentar limitaciones antes de recomendar una accion.
