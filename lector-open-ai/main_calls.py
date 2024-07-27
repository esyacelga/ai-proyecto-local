import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from src import lector_service as svr


def procesarDocumento(usario='eyacelga'):
    texto_dividido = svr.uploadAndProcessDocument(usario)
    print(texto_dividido)


def consultaDocumento():
    consulta = "Cual es la problematica del siisspolweb"
    texto_consutado = svr.get_test_open_ai_connection()
    print(texto_consutado)


if __name__ == "__main__":
    procesarDocumento()
