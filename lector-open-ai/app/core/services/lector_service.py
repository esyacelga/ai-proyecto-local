import app.adapters.external.document_ai_repository as dai
import app.adapters.external.open_ai_repository as openai
import app.adapters.persistence.elastic_search_repository as elas
import app.utils.lector_utils as utll


def procesarDocumento(usario='eyacelga', equipo='localhost', rutaDirectorio=''):
    result, texto = uploadAndProcessDocument(usario, equipo, rutaDirectorio)
    print(result, texto)
    return result, texto


def uploadAndProcessDocument(usuario, equipo, rutaDirectorio):
    result, raw_texto = cargarDocumento(rutaDirectorio)
    if result == False:
        return False, raw_texto
    cleaned_text = utll.normalize_text(raw_texto)
    chunks = utll.segment_by_length(cleaned_text, max_tokens=10000)
    result, message = elas.index_documents(chunks, usuario, equipo)
    if result == False:
        return False, message
    else:
        return True, message


def cargarDocumento(ruta_archivo='./uploads/prueba-documento.pdf'):
    result, documento = dai.onlineProcessing(ruta_archivo)
    if result == False:
        return False, documento
    else:
        text = documento.text
    return True, text


def get_answer_from_documents(query):
    fragments = elas.search_documents(query)
    texto_simple = fragments[0]
    respuesta = openai.procesarConsulta(query, texto_simple)
    return respuesta


def get_test_open_ai_connection():
    query = "quien es Rocio Yuquilema"
    contexto = 'Rocio Yuquilema es sargento segundo de la policia nacional del ecuador, nacida en Riobamba y de padre y madre de la misma provincia'
    respuesta = openai.procesarConsulta(query, contexto)
    return respuesta
