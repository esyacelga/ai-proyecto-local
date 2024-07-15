import os

from google.cloud import documentai_v1 as documentai
from google.cloud import storage
from google.cloud.exceptions import NotFound

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './documentacion-isspol.json'


def guardar_entidades_en_json(document):
    entidades_json = {}

    # Itera sobre las entidades detectadas en el documento
    for entidad in document.entities:
        # Obtén el tipo de entidad y su valor asociado
        tipo_entidad = entidad.type_
        valor_entidad = entidad.mention_text

        # Agrega la entidad al objeto JSON
        if tipo_entidad not in entidades_json:
            entidades_json[tipo_entidad] = []
        entidades_json[tipo_entidad].append(valor_entidad)

    # Devuelve el objeto JSON con las entidades detectadas
    return entidades_json

def leer_pdf_como_bytes(file_path):
    """Lee un archivo PDF y lo convierte a bytes."""
    with open(file_path, 'rb') as file:
        contenido_en_bytes = file.read()
    return contenido_en_bytes


def onlineProcessing(project_id, file_path, processor_id):
    location = 'us'
    opts = {
        "api_endpoint": f"{location}-documentai.googleapis.com"

    }
    mime_type = 'application/pdf'
    client = documentai.DocumentProcessorServiceClient(client_options=opts)
    name = client.processor_path(project_id, location, processor_id)
    image_content = leer_pdf_como_bytes(file_path)
    raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)
    request = documentai.ProcessRequest(name=name, raw_document=raw_document)
    result = client.process_document(request)
    document = result.document
    print(document)
    return document


def obtener_o_crear_bucket(bucket_name):
    """
    Obtiene un bucket si ya existe, o lo crea si no existe.

    Args:
    bucket_name (str): El nombre del bucket a obtener o crear.

    Returns:
    google.cloud.storage.bucket.Bucket: La instancia del bucket.
    """
    # Configura las credenciales para Google Cloud
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './documentacion-isspol.json'

    # Crea un cliente de almacenamiento
    storage_client = storage.Client()

    # Verifica si el bucket ya existe
    try:
        bucket = storage_client.get_bucket(bucket_name)
        print(f'El bucket {bucket_name} ya existe.')
    except NotFound:
        # El bucket no existe, crearlo
        bucket = storage_client.bucket(bucket_name)
        bucket = storage_client.create_bucket(bucket)
        print(f'Bucket {bucket.name} creado en {bucket.location}')

    return bucket


def subir_archivo(bucket, ruta_archivo, blob_name=None):
    """
    Sube un archivo a un bucket de Google Cloud Storage.

    Args:
    bucket (google.cloud.storage.bucket.Bucket): La instancia del bucket.
    ruta_archivo (str): La ruta del archivo que se desea subir.
    blob_name (str): El nombre del blob en el bucket. Si no se proporciona, se usa el nombre del archivo.

    Returns:
    google.cloud.storage.blob.Blob: La instancia del blob subido.
    """
    if blob_name is None:
        blob_name = os.path.basename(ruta_archivo)

    blob = bucket.blob(blob_name)
    blob.upload_from_filename(ruta_archivo)

    print(f'Archivo {ruta_archivo} subido a {blob_name} en el bucket {bucket.name}.')
    return blob


# Uso de la función
#bucket_name = 'data_bucket_isspol'
#bucket = obtener_o_crear_bucket(bucket_name)
#print(f'Bucket {bucket.name} está listo para usarse.')
ruta_archivo = './prueba-documento.pdf'  # Reemplaza con la ruta de tu archivo
project_id = 'documentacion-isspol'
pocesador = '89b174137f081104'
documento = onlineProcessing(project_id, ruta_archivo, pocesador)
documento_json = documento.text
print(documento_json)

#subir_archivo(bucket, ruta_archivo)
