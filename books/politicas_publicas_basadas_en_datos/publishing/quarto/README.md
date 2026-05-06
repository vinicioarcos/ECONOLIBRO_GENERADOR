# Publicacion Quarto

Use la configuracion principal del libro en:

```text
books/politicas_publicas_basadas_en_datos/book/_quarto.yml
```

Comando sugerido desde la carpeta `book`:

```powershell
quarto render
```

Antes de publicar, verificar que los notebooks se ejecuten de arriba hacia abajo,
que no existan rutas absolutas y que toda tabla o figura tenga interpretacion en
el capitulo correspondiente.
