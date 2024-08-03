import app.adapters.external.document_ai_repository as dai
import app.adapters.persistence.elastic_search_repository as elas
import app.utils.lector_utils as utll
import app.adapters.external.open_ai_repository as openai


def uploadAndProcessDocument(usuario):
    raw_text = cargarDocumento()
    cleaned_text = utll.normalize_text(raw_text)
    chunks = utll.segment_by_length(cleaned_text, max_tokens=10000)
    elas.index_documents(chunks, usuario)
    return chunks


def cargarDocumento(ruta_archivo='./uploads/prueba-documento.pdf'):
    documento = dai.onlineProcessing(ruta_archivo)
    documento_pdf = documento.text
    return documento_pdf


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
