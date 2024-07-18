import re
import unicodedata
import json

def obtener_secret_key(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        config = json.load(archivo)
        return config.get('secret_key')

def leer_pdf_como_bytes(file_path):
    """Lee un archivo PDF y lo convierte a bytes."""
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