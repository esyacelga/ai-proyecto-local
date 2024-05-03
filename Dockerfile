# Usa una imagen de Python 3.11.9 como base
FROM python:3.11.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio /app
COPY api/requirements.txt .

# Instala las dependencias de la API
RUN pip install -U pip && pip install -r requirements.txt

# Copia el código fuente de la API al directorio /app/api
COPY api/ ./api

# Copia el archivo model-salary.pkl al directorio /app/regresion_lineal_simple/src/notebooks/model/
COPY regresion_lineal_simple/src/notebooks/model/model-salary.pkl /app/regresion_lineal_simple/src/notebooks/model/

# Copia el script initializer.sh al directorio /app
COPY initializer.sh /app/initializer.sh

# Concede permisos de ejecución al script initializer.sh
RUN chmod +x /app/initializer.sh

# Expone el puerto 8000 para la API
EXPOSE 8000

# Establece el script initializer.sh como punto de entrada del contenedor
#ENTRYPOINT ["/app/initializer.sh"]
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0", "api.main:app", "-w", "2", "-k", "uvicorn.workers.UvicornWorker"]
