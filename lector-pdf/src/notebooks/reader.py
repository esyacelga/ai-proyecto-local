import os
from google.cloud import storage
from google.cloud import documentai_v1 as documentai

# Configurar la ruta a tu archivo de clave JSON de Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/eyacelga/repositorio-codigo/ai-proyecto-local/lector-pdf/src/notebooks/data/documental-isspol-664f93e7c2fb.json"

# Configuración de parámetros
project_id = 'documental-isspol'
location = 'us'  # o cualquier otra ubicación donde tengas configurada Document AI
processor_id = 'f0348ea454d52124'
bucket_name = 'document-ai-reader'
file_path = '/home/eyacelga/repositorio-codigo/ai-proyecto-local/lector-pdf/src/notebooks/data/ISSPOL-TIC-2024-0033-I-ME.pdf'
gcs_input_uri = f'gs://{bucket_name}/{os.path.basename(file_path)}'
mime_type = 'application/pdf'

def onlineProcessing(location,project_id):
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

def cargar_documento_en_bytes(bucket_name, gcs_input_uri):
    """Carga un documento desde GCS y lo devuelve en formato de bytes."""
    # Inicializar el cliente de GCS
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(gcs_input_uri)
    
    # Descargar el contenido del archivo en bytes
    contenido_bytes = blob.download_as_bytes()
    return contenido_bytes


def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Sube un archivo al bucket de Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f'Archivo {source_file_name} subido a {destination_blob_name}.')


def process_document(project_id, location, processor_id, gcs_input_uri):
    """
    Processes a document stored in a Cloud Storage bucket using the specified Document AI processor.

    Args:
        project_id (str): The project ID of your GCP project.
        location (str): The location of the Document AI processor (e.g., "us").
        processor_id (str): The ID of the Document AI processor (e.g., "4234234234").
        gcs_input_uri (str): The Cloud Storage URI of the document to process (e.g., "gs://your-bucket/your-document.pdf").

    Returns:
        documentai.types.Document: The processed document object.
    """
    client = documentai.DocumentProcessorServiceClient()
    gcs_document=documentai.GcsDocument(gcs_uri=gcs_input_uri, mime_type="application/pdf")

    # Configure the process request
    request = documentai.ProcessRequest(name='CUSTOM', gcs_document=gcs_document)

    result = client.process_document(request=request)

    document = result.document

    return document


# Paso 1: Subir el archivo PDF a Google Cloud Storage
#upload_to_gcs(bucket_name, file_path, os.path.basename(file_path))

# Paso 2: Procesar el documento con Document AI
#resultado = process_document(project_id, location, processor_id, gcs_input_uri)
resultado = onlineProcessing(location,project_id)
# Paso 3: Imprimir el texto extraído
print('Texto extraído del documento:')
print(resultado)
