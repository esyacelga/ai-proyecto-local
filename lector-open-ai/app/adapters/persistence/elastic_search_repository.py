# Indexación de documentos en Elasticsearch
from datetime import datetime

from elasticsearch import Elasticsearch, exceptions
from app.adapters.config.settings import ELASTIC_SEARCH_URL


def index_documents(docs, usuarioCreacion, index="documentacion_isspol"):
    es = Elasticsearch([ELASTIC_SEARCH_URL])
    try:
        for doc in docs:
            if not document_exists(doc, index, ELASTIC_SEARCH_URL):
                body = {
                    "usuario_creacion": usuarioCreacion,
                    "creacion_fecha": datetime.now().isoformat(),
                    "contenido_documento": doc
                }
                es.index(index=index, body=body)
                return True, "Documento subido correctamente"
            else:
                return False, "Documento duplicado"
    except Exception as e:
        error_message = str(e)
        print(f"Error indexando documentos: {error_message}")
        return False, f"Error al indexar documentos: {error_message}"


def search_documents(query, index="documentacion_isspol", servidor_elastic="http://192.168.2.232:9200"):
    es = Elasticsearch([servidor_elastic])
    response = es.search(
        index=index,
        body={
            "query": {
                "match": {
                    "contenido_documento": query
                }
            },
            "size": 5  # Número de documentos a recuperar
        }
    )
    return [hit["_source"]["contenido_documento"] for hit in response["hits"]["hits"]]


def document_exists(content, index="documentacion_isspol", servidor_elastic="http://192.168.2.232:9200"):
    try:
        print(index, servidor_elastic)
        es = Elasticsearch([servidor_elastic])
        response = es.search(
            index=index,
            body={
                "query": {
                    "match": {
                        "contenido_documento": content
                    }
                }
            }
        )
        return len(response["hits"]["hits"]) > 0
    except exceptions.NotFoundError as e:
        print(f"No se ha encontrado el documento, ya que el indice no esta creado....: {e}")
        return False
