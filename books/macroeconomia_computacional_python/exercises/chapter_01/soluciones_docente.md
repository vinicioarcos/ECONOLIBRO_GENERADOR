# Soluciones docentes - Capítulo 1

## Criterios de revision

- El estudiante separa claramente simulación y evidencia empírica.
- El notebook se ejecuta completo de arriba hacia abajo.
- Los parámetros modificados quedan documentados.
- Los datos simulados se guardan en `data/processed`.
- La tabla y la figura se exportan a `outputs`.
- La interpretación menciona límites y evita causalidad no identificada.

## Guia orientativa

En el modelo del capítulo, `Y` es endógena porque se determina dentro del
sistema. `G`, `I` y `X0` se tratan como exógenas en la simulación. `c`, `t` y
`m` son parámetros. El multiplicador disminuye cuando aumenta `m` porque parte
del ingreso adicional se filtra hacia importaciones.

Un buen reporte debe decir que los resultados son mecanicos: salen de las
ecuaciones y parámetros elegidos. Para evaluar una política real se necesitarían
datos observados, contexto institucional, estrategia empírica y discusión de
supuestos.

## Rubrica breve

| Criterio | Excelente | A mejorar |
|---|---|---|
| Teoria | Distingue mecanismo, parametro y equilibrio | Confunde relato con resultado |
| Codigo | Ejecuta completo y usa rutas relativas | Depende de rutas personales |
| Outputs | Exporta datos, tabla, figura y reporte | Faltan salidas verificables |
| Interpretación | Declara límites y evita causalidad | Trata la simulación como evidencia |
| Comunicación | Explica escenarios con claridad | Presenta números sin lectura económica |
