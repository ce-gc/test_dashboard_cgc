# Proyecto Dashboard de Ventas

## Descripción del Proyecto

Este proyecto consiste en un cuadro de mandos (dashboard) interactivo creado con Python y Streamlit. Visualiza datos de ventas almacenados en una base de datos SQLite local. Permite analizar métricas como pedidos sin fecha, ventas diarias por mes y categorías de productos vendidas.

## Cómo instalar

Para usar este proyecto solo necesitas tener instalada la herramienta `uv` en tu ordenador. No hace falta que instales las librerías manualmente, ya que `uv` gestionará todas las dependencias (como pandas, streamlit y matplotlib) de forma automática.

Si deseas ejecutar el proyecto en un contenedor, necesitarás tener instalado `podman` (o Docker).

## Cómo ejecutar

### Opción 1: Ejecutar con uv

Si estás en tu máquina local y tienes `uv` instalado, simplemente ejecuta el siguiente comando en la terminal dentro de la carpeta del proyecto:

```bash
uv run streamlit run dashboard.py
```

Al ejecutar este comando, `uv` preparará el entorno y lanzará la aplicación. Deberías ver en tu terminal una dirección local (normalmente http://localhost:8501) que puedes abrir en tu navegador para ver el dashboard.

### Opción 2: Ejecutar con Podman

Si prefieres usar contenedores con Podman, sigue estos pasos:

1. Construye la imagen del contenedor (asegúrate de estar en la carpeta del proyecto):

   ```bash
   podman build -t mi-dashboard -f dockerfile.txt .
   ```

   Nota: Se usa `-f dockerfile.txt` porque el archivo de configuración tiene extensión .txt en este proyecto.

2. Ejecuta el contenedor mapeando el puerto 8501:

   ```bash
   podman run -p 8501:8501 mi-dashboard
   ```

3. Abre tu navegador web y visita: `http://localhost:8501`
