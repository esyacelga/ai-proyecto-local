# Documentación Técnica del Proyecto de Machine Learning

El proyecto consta de servicios rest usando fastapi, docker, python y algoritmos de machine learning

## Descripción del Proyecto

El objetivo principal de este proyecto es integrar varios proyectos pequeños de Machine Learning en uno proyecto geneneral y documentar detalladamente cada paso, desde la adquisición de datos hasta la implementación de modelos.

## Estructura del Repositorio

El repositorio está estructurado de la siguiente manera:

* `api/`: Codigo usado para crear los servicios rest
* `Dockerfile`: Archivo Docker que contiene las instrucciones para generar la imagen con sus respectivas dependencias

### Proyectos individuales

- `src/notebooks/data/`: Contiene los datos de entrenamiento y prueba.
- `src/notebooks/models/`: Contiene los modelos entrenados.
- `venv/`: Contiene la iformación de los ambiente virual del proyecto
- `README.md`: Este archivo, que proporciona una visión general del proyecto.
- `requeriments.txt`: Dependencias del proyecto individual

### Comando para exportación de dependencias

pip freeze

## Instalación

Para instalar las dependencias del proyecto, puedes ejecutar el siguiente comando:

`pip3 install -r proyecto-a-ejecuatar/requeriments.txt`

## Comandos para la ejecución en Docker

`sudo docker run -d -p 8000:8000 model-api:v1`: Corre el contenedor
