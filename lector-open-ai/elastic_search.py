# Indexación de documentos en Elasticsearch
from datetime import datetime

from elasticsearch import Elasticsearch, exceptions


def index_documents(docs, usuarioCreacion, index="documentacion_isspol", servidor_elastic="http://192.168.2.232:9200"):
    es = Elasticsearch([servidor_elastic])
    for i, doc in enumerate(docs):
        if not document_exists(doc, index):
            body = {
                "usuario_creacion": usuarioCreacion,
                "creacion_fecha": datetime.now().isoformat(),
                "contenido_documento": doc
            }
            es.index(index=index, id=i, body=body)
        else:
            print(f"Documento duplicado no indexado: {doc[:30]}...")


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
