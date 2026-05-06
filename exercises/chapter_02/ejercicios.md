# Ejercicios - Capitulo 2

## Resultados de aprendizaje asociados

- Preparar un entorno de trabajo reproducible.
- Verificar version de Python y kernel de Jupyter.
- Usar rutas relativas.
- Generar un reporte tecnico en `outputs/reports`.
- Explicar diferencias entre entorno local y Google Colab.

## Ejercicios conceptuales

1. Explique por que una ruta absoluta dificulta la reproducibilidad.
2. Compare entorno local, entorno virtual, Conda y Google Colab. Indique una
   ventaja y una limitacion de cada opcion.
3. Explique por que `requirements.txt` y `environment.yml` no son archivos
   decorativos.
4. Describa que puede salir mal si Jupyter usa un kernel distinto al Python
   donde se instalaron los paquetes.
5. Explique por que `data/raw` no debe recibir archivos transformados.

## Ejercicios computacionales

1. Ejecute `notebooks/chapter_02/verificacion_entorno.ipynb` de arriba hacia
   abajo.
2. Verifique que se cree `outputs/reports/chapter_02_entorno_python.txt`.
3. Verifique que se cree `outputs/tables/chapter_02_checklist_entorno.csv`.
4. Abra el reporte y confirme que muestre version de Python, plataforma y raiz
   del proyecto.
5. Reinicie el kernel y ejecute todo nuevamente para confirmar que las salidas se
   regeneran.

## Mini-proyecto

Prepare una ficha de entorno personal con:

- sistema operativo;
- version de Python;
- forma de trabajo elegida: local, Conda, Google Colab o mixta;
- ruta relativa usada para outputs;
- problemas encontrados;
- solucion aplicada o duda pendiente.

## Criterios de entrega

- El notebook debe ejecutarse completo.
- Las salidas deben generarse en `outputs`.
- No debe modificarse `data/raw`.
- La ficha debe distinguir instalacion, kernel y dependencias.
- La explicacion debe estar escrita para que otro estudiante pueda repetir el
  proceso.
