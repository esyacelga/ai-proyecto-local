import json
import os
import re
import unicodedata


def leer_api_key():
    """
    Lee la clave API desde un archivo JSON.

    :return: La clave API si se encuentra, None en caso contrario.
    """
    # Construir la ruta completa al archivo JSON
    ruta_config = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../secret-key-open-ai.json')

    try:
        with open(ruta_config, 'r') as file:
            config = json.load(file)
            return config.get('api_key')
    except FileNotFoundError:
        print(f"El archivo {ruta_config} no se encuentra.")
        return None


def file_exists_in_directory(file_name, directory):
    """
    Verifica si un archivo existe en un directorio dado.

    :param file_name: Nombre del archivo a buscar.
    :param directory: Directorio donde buscar el archivo.
    :return: True si el archivo existe, False en caso contrario.
    """
    file_path = os.path.join(directory, file_name)
    return 1, os.path.isfile(file_path)


def obtener_secret_key(secret_key_file):
    directory = '../../'
    file_path = directory + secret_key_file
    existe_archivo = file_exists_in_directory(secret_key_file, directory)
    if existe_archivo:
        with open(file_path, 'r') as archivo:
            config = json.load(archivo)
            return True, config.get('secret_key')
    else:
        return False, 'No existe el archivo desde' + file_path


def leer_pdf_como_bytes(file_path):
    """Lee un archivo PDF y lo convierte a bytes...."""
    with open(file_path, 'rb') as file:
        contenido_en_bytes = file.read()
    return contenido_en_bytes


def normalize_text(text):
    # Convertir a minúsculas
    text = text.lower()

    # Eliminar acentos y caracteres especiales
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode('utf-8')

    # Reemplazar saltos de línea y tabulaciones por un espacio
    text = re.sub(r'\s+', ' ', text)

    # Eliminar caracteres especiales no deseados
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Eliminar espacios en blanco al inicio y al final
    text = text.strip()

    return text


# Segmentación del texto por longitud
def segment_by_length(text, max_tokens=4096):
    words = text.split()
    chunks = []
    chunk = []
    for word in words:
        if len(chunk) + len(word) <= max_tokens:
            chunk.append(word)
        else:
            chunks.append(' '.join(chunk))
            chunk = [word]
    if chunk:
        chunks.append(' '.join(chunk))
    return chunks
