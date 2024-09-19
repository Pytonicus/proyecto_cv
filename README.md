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

## Como generar un CV

1. Acceder al panel de django con nuestro usuario y contraseña: http://127.0.0.1:8000/admin
2. Vamos a la opción Curriculums y hacemos click en **AÑADIR CURRICULUM VITAE** arriba a la derecha.
3. Seguimos los pasos para añadir el curriculum, se abrirán distintas ventanas para ir añadiendo datos dinámicos que podremos ir seleccionando o quitando para ajustar la vista.
4. Para mostrar el curriculum que se está generando vamos a la ruta: http://127.0.0.1:8000/export_cv/
5. Una vez finalizado podremos descargar el CV desde la vista anterior.
