import lector_service as svr


def procesarDocumento():
    texto_dividido = svr.uploadAndProcessDocument('eyacelga')
    print(texto_dividido)

def consultaDocumento():
    consulta = "Cual es la problematica del siisspolweb"
    texto_consutado = svr.get_test_open_ai_connection()
    print(texto_consutado)


if __name__ == "__main__":
    consultaDocumento()
