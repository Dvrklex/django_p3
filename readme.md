# Comandos básicos para configurar un proyecto Django con Postgres
## Instalar Python 3.9 y Postgres
    - Descargar e instalar Python 3.9: https://www.python.org/downloads/
    - Descargar e instalar Postgres: https://www.postgresql.org/download/

## Crear un entorno virtual y activarlo
    - Crear un nuevo entorno virtual: python -m venv nombre_entorno
    - Activar el entorno virtual: source nombre_entorno/bin/activate (Linux/macOS) o nombre_entorno\Scripts\activate (Windows)

## Instalar Django y psycopg2-binary
    - Instalar Django: pip install django
    - Instalar psycopg2-binary: pip install psycopg2-binary
## Configurar el archivo settings.py
    Añadir la siguiente configuración en el archivo settings.py del proyecto:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nombre_db',
        'USER': 'nombre_usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Reemplazar nombre_db, nombre_usuario y contraseña con los valores correspondientes.

## Crear una base de datos
    - Crear una base de datos en Postgres: createdb nombre_db

## Crear modelos y migraciones
    - Crear modelos en el archivo models.py
    - Generar migraciones: python manage.py makemigrations
    - Ejecutar migraciones: python manage.py migrate

## Verificar que los modelos se han creado correctamente
    - Iniciar la consola interactiva de Django: python manage.py shell
    - Importar los modelos: from nombre_app.models import NombreModelo
    - Verificar que los modelos están disponibles: NombreModelo.objects.all()

## Crear un superusuario
    - Crear un superusuario: python manage.py createsuperuser

## Iniciar el servidor de desarrollo
    - Iniciar el servidor de desarrollo: python manage.py runserver
    - Ingresar al panel de administación: http://<localhost>/admin

    