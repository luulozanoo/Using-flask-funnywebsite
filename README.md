# 🪨 The Rock's Personal Web Page & Portfolio 🐬

[![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/es/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/es/docs/Web/CSS)

> **Aplicación web personal desarrollada con Flask, HTML y CSS.**
> 
> Este proyecto es una introducción al desarrollo web backend y frontend. Consiste en una página web temática y humorística estructurada como el portfolio de Dwayne "The Rock" Johnson en su nueva aventura como entrenador de delfines, incluyendo enrutamiento dinámico y manejo de formularios.

---

## 📑 Secciones de la Web

La aplicación cuenta con tres rutas principales gestionadas por Flask:

* 🏠 **Inicio (`/`):** Página de presentación principal con una biografía introductoria y la imagen de perfil centrada.
* 📋 **Curriculum Vitae (`/cv`):** Sección detallada con la experiencia laboral (desde estrella de acción en Hollywood hasta el océano), habilidades e idiomas (incluyendo clicks de delfín).
* 📥 **Contacto (`/contact`):** Formulario interactivo. Utiliza métodos `GET` para mostrar la vista inicial y `POST` para procesar los datos introducidos (nombre, email, teléfono), devolviendo una página de confirmación personalizada.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3, Flask (Enrutamiento y renderizado de plantillas Jinja2).
* **Frontend:** HTML5 (Estructuración semántica), CSS3 (Estilos básicos, fondos y centrado de elementos).
* **Arquitectura:** Patrón básico de vistas y plantillas estáticas (`/templates`, `/static`).

---

## ⚙️ Cómo ejecutar la web en local

Si deseas probar esta página web en tu propio equipo, sigue estos pasos:

### 1. Clona el repositorio
```bash
git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
cd TU_REPOSITORIO
```

### 2. Crea y activa un entorno virtual (Recomendado)
```bash
# En Windows:
python -m venv venv
venv\Scripts\activate

# En macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```
### 3. Instala Flask
Como es un proyecto ligero, solo necesitas instalar la librería principal:
```bash
pip install Flask
```

### 4. Ejecuta el servidor de desarrollo
Asegúrate de estar en el directorio donde se encuentra el archivo main.py y ejecuta:
```bash
flask --app main run
```

Abre tu navegador y entra en http://127.0.0.1:5000 para ver a The Rock en acción.

## 📩 Contacto
Si tienes alguna duda sobre el proyecto, el despliegue en local o quieres conectar conmigo, puedes encontrarme a través de los siguientes canales oficiales:

* 📧 **Email:** lucia.lozano110@gmail.com
* 💼 **LinkedIn:** [linkedin.com/in/tu-perfil](https://linkedin.com/in/tu-perfil)
* 🐙 **GitHub:** [github.com/luulozanoo](https://github.com/luulozanoo)
