# Plantilla de notebook reproducible

## 1. Pregunta economica

Formular una pregunta observable y explicar por que importa.

## 2. Preparacion

```python
from pathlib import Path

DATA_RAW = Path("../../data/raw")
DATA_PROCESSED = Path("../../data/processed")
OUTPUTS = Path("../../outputs")
```

## 3. Datos

- Fuente:
- Periodo:
- Unidad de observacion:
- Variables clave:
- Advertencias:

## 4. Carga y validacion

Verificar existencia de archivos, dimensiones, nombres de variables, duplicados
y valores faltantes.

## 5. Limpieza

Leer desde `data/raw` y escribir derivados en `data/processed`. Documentar cada
filtro o transformacion.

## 6. Analisis

Construir tablas, estadisticas, graficos o modelos que respondan la pregunta.

## 7. Interpretacion

Explicar los resultados en lenguaje economico y declarar limitaciones.

## 8. Exportacion

Guardar tablas en `outputs/tables` y figuras en `outputs/figures`.

## Checklist

- [ ] El notebook corre de arriba hacia abajo.
- [ ] No usa rutas absolutas.
- [ ] No modifica `data/raw`.
- [ ] Cada resultado tiene interpretacion economica.
- [ ] No afirma causalidad sin identificacion.
