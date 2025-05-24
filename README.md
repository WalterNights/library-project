# Library Project

Proyecto de biblioteca con Django (backend) y Angular (frontend).

## Requisitos

- Python 3.10+
- Node.js 18+
- PostgreSQL

---

## Instalación Backend (Django)

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/tu-repo.git
   cd tu-repo/library_project
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate   # En Windows: env\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura la base de datos en `settings.py` para usar PostgreSQL.

5. Aplica migraciones y crea un superusuario:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. Corre el servidor:
   ```bash
   python manage.py runserver
   ```

---

## Instalación Frontend (Angular)

1. Ve a la carpeta del frontend:
   ```bash
   cd ../library-frontend
   ```

2. Instala las dependencias:
   ```bash
   npm install
   ```

3. Corre la aplicación Angular:
   ```bash
   ng serve
   ```
   La app estará disponible en [http://localhost:4200](http://localhost:4200)

---

## Despliegue en Render

1. Sube tu código a GitHub.
2. Crea un servicio web en Render y una base de datos Postgres.
3. Configura las variables de entorno necesarias (`DATABASE_URL`, `SECRET_KEY`, etc).
4. Sube el frontend como Static Site o sírvelo desde Django.

---

¿Dudas o problemas? ¡Abre un issue!