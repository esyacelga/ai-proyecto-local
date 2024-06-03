import os
from google.cloud import storage
from google.cloud import documentai_v1 as documentai
import json

# Configurar la ruta a tu archivo de clave JSON de Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/eyacelga/repositorio-codigo/ai-proyecto-local/lector-pdf/src/data/documental-isspol-664f93e7c2fb.json"

# Configuración de parámetros
project_id = 'documental-isspol'
location = 'us'  # o cualquier otra ubicación donde tengas configurada Document AI
processor_id = 'f0348ea454d52124'
bucket_name = 'document-ai-reader'
#file_path = '/home/eyacelga/repositorio-codigo/ai-proyecto-local/lector-pdf/ISSPOL-TIC-2024-0033-I-ME.pdf'
#gcs_input_uri = f'gs://{bucket_name}/{os.path.basename(file_path)}'
mime_type = 'application/pdf'

def onlineProcessing(location,project_id, file_path):
    opts ={
        "api_endpoint":f"{location}-documentai.googleapis.com"

    }
    client = documentai.DocumentProcessorServiceClient(client_options=opts)
    name = client.processor_path(project_id,location, processor_id)
    image_content = leer_pdf_como_bytes(file_path)
    raw_document = documentai.RawDocument(content=image_content, mime_type= mime_type )
    request = documentai.ProcessRequest(name=name, raw_document=raw_document)   
    result = client.process_document(request)
    document = result.document
    return document

def leer_pdf_como_bytes(file_path):
    """Lee un archivo PDF y lo convierte a bytes."""
    with open(file_path, 'rb') as file:
        contenido_en_bytes = file.read()
    return contenido_en_bytes

def buscar_objetos_por_nombre(json_data, nombre_objeto):
    """
    Busca recursivamente en el JSON y devuelve una lista de objetos que coinciden con el nombre del objeto.

    Parámetros:
    json_data (dict): Diccionario que representa el objeto JSON.
    nombre_objeto (str): El nombre del objeto que se está buscando.

    Retorna:
    list: Lista de objetos encontrados que coinciden con el nombre del objeto.
    """
    resultados = []

    def buscar_recursivamente(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == nombre_objeto:
                    resultados.append(value)
                if isinstance(value, (dict, list)):
                    buscar_recursivamente(value)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    buscar_recursivamente(item)

    buscar_recursivamente(json_data)
    return resultados

def procesar_documento(file_path):
    return onlineProcessing(location,project_id,file_path )

def decirHola():
    print("**************")