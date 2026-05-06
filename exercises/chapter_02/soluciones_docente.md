# Soluciones docentes - Capitulo 2

## Criterios de revision

- El estudiante identifica correctamente la raiz del proyecto.
- El notebook se ejecuta de arriba hacia abajo.
- Las salidas se guardan en `outputs/reports` y `outputs/tables`.
- No se usan rutas absolutas.
- No se modifica `data/raw`.
- La respuesta distingue entorno local, entorno virtual, Conda y Colab.
- El estudiante entiende la diferencia entre instalar un paquete y usarlo desde
  el kernel correcto.

## Guia orientativa por ejercicio

### Ejercicio conceptual 1

Una ruta absoluta depende de la estructura de carpetas de una computadora
particular. Una ruta relativa permite que el proyecto se mueva o comparta sin
reescribir el codigo.

### Ejercicio conceptual 2

Respuestas esperadas:

- Local: da control sobre archivos y dependencias, pero requiere instalacion.
- Entorno virtual: aisla dependencias, pero debe activarse correctamente.
- Conda: facilita dependencias cientificas, pero agrega una herramienta mas.
- Colab: reduce barreras de instalacion, pero depende de sesion remota y manejo
  cuidadoso de archivos.

### Ejercicio conceptual 3

`requirements.txt` y `environment.yml` documentan el entorno. Permiten recrear
dependencias y reducen ambiguedad entre computadoras.

### Ejercicio conceptual 4

Puede ocurrir que el paquete este instalado en un Python, pero el notebook use
otro kernel. El resultado tipico es `ModuleNotFoundError` aunque el estudiante
crea que ya instalo la libreria.

### Ejercicio conceptual 5

`data/raw` debe preservar los archivos originales. Las transformaciones deben
quedar en `data/processed` para mantener trazabilidad y poder reconstruir el
flujo.

## Rubrica breve

| Criterio | Excelente | A mejorar |
|---|---|---|
| Ejecucion | Notebook corre completo y regenera salidas | Requiere pasos manuales no documentados |
| Rutas | Usa rutas relativas | Usa rutas personales |
| Entorno | Distingue Python, kernel y dependencias | Mezcla conceptos |
| Reproducibilidad | Reporte y checklist verificables | Salidas ausentes o fuera de carpeta |
| Datos | Respeta `data/raw` | Escribe derivados en lugar incorrecto |
