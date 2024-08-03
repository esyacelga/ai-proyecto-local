
## Instalación de ambiente

`virtualenv env` : Creacion de ambiente virtual

`source proyecto-a-ejecutar/venv/bin/activate`: Activación de ambiente

`pip3 install -r proyecto-a-ejecutar/requeriments.txt`: Instalacion de dependencias


## Activacion del servicio
`uvicorn main:app --host 0.0.0.0 --port 8000 --reload`: Comando

`docker ps -a`: Comando para revisar si el contenedor esta activa

`sudo docker run -d -p 8000:8000 lector-documental-ai`: Comando para correr la aplicacion

`docker build -t lector-documental-ai .`: Comando para construir el proyecto


