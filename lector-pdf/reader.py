import os
from google.cloud import storage
from google.cloud import documentai_v1 as documentai

# Configurar la ruta a tu archivo de clave JSON de Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/eyacelga/repositorio-codigo/ai-proyecto-local/lector-pdf/documental-isspol-f6c83c0f9d41.json"

# Configuración de parámetros
project_id = 'documental-isspol'
location = 'us'  # o cualquier otra ubicación donde tengas configurada Document AI
processor_id = 'f0348ea454d52124'
bucket_name = 'document-ai-reader'
file_path = '/home/eyacelga/repositorio-codigo/ai-proyecto-local/lector-pdf/ISSPOL-TIC-2024-0033-I-ME.pdf'
gcs_input_uri = f'gs://{bucket_name}/{os.path.basename(file_path)}'

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Sube un archivo al bucket de Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f'Archivo {source_file_name} subido a {destination_blob_name}.')

def process_document(project_id, location, processor_id, gcs_input_uri):
    """Procesa el documento usando Document AI."""
    client = documentai.DocumentProcessorServiceClient()

    # La ruta del recurso del procesador
    name = client.processor_path(project_id, location, processor_id)

    # La fuente de contenido (en este caso, un archivo en Google Cloud Storage)
    gcs_document = documentai.types.GcsDocument(gcs_uri=gcs_input_uri, mime_type='application/pdf')
    input_config = documentai.types.BatchProcessRequest.BatchInputConfig(gcs_document=gcs_document)

    # Configurar la solicitud
    request = documentai.types.BatchProcessRequest(
        name=name,
        input_configs=[input_config],
        document_output_config=documentai.types.DocumentOutputConfig(gcs_output_config=documentai.types.DocumentOutputConfig.GcsOutputConfig(gcs_uri='gs://{bucket_name}/output/'))
    )

    # Procesar el documento
    operation = client.batch_process_documents(request=request)

    print('Esperando a que la operación se complete...')
    operation.result()

    # Descargar y leer el resultado
    bucket = storage.Client().bucket(bucket_name)
    blob = bucket.blob('output/processed_document.json')
    result = blob.download_as_string()

    return result

# Paso 1: Subir el archivo PDF a Google Cloud Storage
upload_to_gcs(bucket_name, file_path, os.path.basename(file_path))

# Paso 2: Procesar el documento con Document AI
resultado = process_document(project_id, location, processor_id, gcs_input_uri)

# Paso 3: Imprimir el texto extraído
print('Texto extraído del documento:')
print(resultado)
