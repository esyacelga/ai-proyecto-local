# Indexación de documentos en Elasticsearch
from datetime import datetime

from elasticsearch import Elasticsearch, exceptions

from app.adapters.config.settings import ELASTIC_SEARCH_URL


def insert_documet(texto, usuarioCreacion, equipo, index="documentacion_isspol"):
    try:
        es = Elasticsearch([ELASTIC_SEARCH_URL])
        body = {
            "usuario_creacion": usuarioCreacion,
            "creacion_fecha": datetime.now().isoformat(),
            "creacion_equipo": equipo,
            "contenido_documento": texto
        }
        es.index(index=index, body=body)
        return True, 'Documento creado'
    except Exception as e:
        error_message = str(e)
        print(f"Error indexando documentos: {error_message}")
    return False, f"Error al indexar documentos: {error_message}"


def index_documents(lst_documentos, usuario_creacion, creacion_equipo, index="documentacion_isspol"):
    try:
        for doc in lst_documentos:
            if not document_exists(doc, index, ELASTIC_SEARCH_URL):
                return insert_documet(doc, usuario_creacion, creacion_equipo, index)
            else:
                print(False, "Elemento duplicado")
                return False, "Documento duplicado index_documents"
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
        es = Elasticsearch([servidor_elastic])
        response = es.search(
            index=index,
            body={
                "query": {
                    "match_phrase": {"contenido_documento": content}
                },
                "size": 5  # Número de documentos a recuperar
            }
        )
        return len(response["hits"]["hits"]) > 0
    except exceptions.NotFoundError as e:
        print(f"No se ha encontrado el documento, ya que el indice no esta creado....: {e}")
        return False


def document_exists_match(content, index="documentacion_isspol", servidor_elastic="http://192.168.2.232:9200"):
    print("Incia el metodo document_exists buscando: ", content, index, servidor_elastic)
    try:
        es = Elasticsearch([servidor_elastic])
        response = es.search(
            index=index,
            body={
                "query": {
                    "match_phrase": {"contenido_documento": content}
                },
                "size": 5  # Número de documentos a recuperar
            }
        )
        print("*************************************************************************************")
        print("Este es el resultado", response)
        return len(response["hits"]["hits"]) > 0
    except exceptions.NotFoundError as e:
        print(f"No se ha encontrado el documento, ya que el indice no esta creado....: {e}")
        return False
