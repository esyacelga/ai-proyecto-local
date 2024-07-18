import os

from google.cloud import documentai_v1 as documentai

import lector_utils as lectorUtil


def onlineProcessing(file_path, project_id='documentacion-isspol', processor_id='89b174137f081104'):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './secret-key-document-ai.json'
    location = 'us'
    opts = {
        "api_endpoint": f"{location}-documentai.googleapis.com"

    }
    mime_type = 'application/pdf'
    client = documentai.DocumentProcessorServiceClient(client_options=opts)
    name = client.processor_path(project_id, location, processor_id)
    image_content = lectorUtil.leer_pdf_como_bytes(file_path)
    raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)
    request = documentai.ProcessRequest(name=name, raw_document=raw_document)
    result = client.process_document(request)
    document = result.document
    return document


def onlineProcessingPdf(pdfFile, project_id='documentacion-isspol', processor_id='89b174137f081104'):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './secret-key-document-ai.json'
    location = 'us'
    opts = {
        "api_endpoint": f"{location}-documentai.googleapis.com"

    }
    mime_type = 'application/pdf'
    client = documentai.DocumentProcessorServiceClient(client_options=opts)
    name = client.processor_path(project_id, location, processor_id)
    image_content = pdfFile
    raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)
    print("va a procesar******************************************************")
    request = documentai.ProcessRequest(name=name, raw_document=raw_document)
    result = client.process_document(request)
    print("Acabo de  procesar******************************************************")
    document = result.document

    return document
