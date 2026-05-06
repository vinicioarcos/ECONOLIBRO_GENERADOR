# Soluciones docentes - Capítulo 3

## Criterios de revisión

- El estudiante representa observaciones con estructuras de datos claras.
- Las funciones tienen nombres interpretables y controlan divisiones inválidas.
- El notebook corre de arriba hacia abajo.
- Las salidas se guardan en `data/processed` u `outputs`.
- No se modifica `data/raw`.
- La interpretación no presenta datos simulados como evidencia real.

## Guía orientativa por ejercicio

### Ejercicio conceptual 1

Una variable de Python es un nombre que apunta a un objeto en memoria. Una
variable económica requiere definición conceptual, unidad de medida, fuente,
periodo, población y advertencias. `ingreso = 500` no basta para saber si es
mensual, anual, individual, del hogar, nominal o real.

### Ejercicio conceptual 2

El ingreso total del hogar no considera el tamaño del hogar. Dos hogares con el
mismo ingreso total pueden tener condiciones distintas si uno tiene una persona
y otro tiene seis. El ingreso per cápita mejora la comparabilidad, aunque sigue
siendo una medida parcial.

### Ejercicio conceptual 3

Una función concentra la regla de cálculo en un solo lugar. Si hay que corregir
la regla, se corrige una vez. También permite reutilizar el cálculo y revisar
supuestos con más claridad.

### Ejercicio conceptual 4

Mezclar datos simulados con datos oficiales puede producir conclusiones falsas,
confundir al lector y romper la trazabilidad del análisis. Los datos simulados
deben estar declarados y separados.

### Ejercicio conceptual 5

Una medición oficial de pobreza requiere metodología institucional, línea de
pobreza documentada, fuente oficial, ponderadores y tratamiento de la muestra.
Un umbral didáctico solo enseña lógica computacional.

## Guía computacional

Una solución aceptable debe generar:

```text
data/processed/chapter_03_hogares_simulados.csv
outputs/tables/chapter_03_resumen_hogares.csv
outputs/figures/chapter_03_ingreso_per_capita.svg
outputs/reports/chapter_03_nota_metodologica.md
```

Al agregar hogares o cambiar el umbral, el estudiante debe explicar que cambian
los resultados del ejemplo, no una realidad económica externa.

## Rúbrica breve

| Criterio | Excelente | A mejorar |
|---|---|---|
| Estructuras | Usa listas y diccionarios claros | Usa nombres ambiguos o datos sueltos |
| Funciones | Calcula indicadores con validación mínima | Repite código o ignora errores |
| Reproducibilidad | Exporta salidas en carpetas correctas | Usa rutas absolutas o no exporta |
| Interpretación | Declara límites del ejemplo simulado | Sobreinterpreta resultados |
| Datos | Mantiene `data/raw` intacta | Mezcla originales y derivados |
