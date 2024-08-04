# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requeriments.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requeriments.txt

# Copia el resto del código fuente al directorio de trabajo
COPY . .

# Expone el puerto en el que tu aplicación se ejecuta (modifica si es necesario)
EXPOSE 8000

# Comando para ejecutar la aplicación
# Asumiendo que estás usando Uvicorn para ejecutar una aplicación FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
