# Proyecto CV 

Un proyecto sencillo para generar CV basados en la información seleccionada y la plantilla que queramos utilizar.
Consta de un panel en el que se introducen los distintos datos del empleado y de un front que muestra los diferentes tipos de datos en cada apartado y solo hay que ir marcando los 
checks para generar un cv con la información seleccionada.

## Preparación del entorno

1. Crear entorno virtual con python: ``python3 -m venv .env``
2. Activar entorno virtual: ``source .env/bin/activate``
3. Instalar librerías: ``pip install -r requirements``

## Preparación y arranque del proyecto

1. Lanzar las migraciones: ``python manage.py migrate``
2. Crear un superusuario: ``python manage.py createsuperuser``
3. Ejecutar el proyecto: ``python manage.py runserver``
