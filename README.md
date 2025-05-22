# 🎮 Ranking de Videojuegos

Esta es una aplicación web desarrollada con **Flask** que muestra un ranking de videojuegos destacados, permitiendo explorar una lista de juegos con títulos, descripciones y detalles individuales.

---

## ✨ Funcionalidades

- Página de inicio con mensaje de bienvenida.
- Ruta para ver todos los videojuegos.
- Ruta para ver el detalle de cada videojuego usando slugs en la URL.
- Estilo visual mejorado con CSS personalizado.
- Uso de plantillas HTML con `Jinja2`.
- Datos cargados desde estructuras de Python (listas y diccionarios).
- Código simple y educativo, ideal para aprender Flask.

---

## 📂 Estructura del proyecto

- `mi_app_juegos/`
  - `app.py` — Archivo principal con rutas Flask.
  - `datos.py` — Lista de videojuegos en formato diccionario.
  - `static/`
    - `estilo.css` — Archivo CSS con los estilos personalizados.
  - `templates/`
    - `base.html` — Plantilla base común.
    - `index.html` — Página de inicio.
    - `juegos.html` — Página con lista de juegos.
    - `detalle.html` — Página de detalle para cada juego.
  - `README.md` — Este archivo.

---

## ⚙️ Requisitos

- Python 3.x
- Flask
---

## 🚀 Instrucciones de instalación y ejecución

1. Cloná este repositorio o descargá el proyecto:
   ```bash
   git clone https://github.com/tu_usuario/mi_app_juegos.git
   cd mi_app_juegos
