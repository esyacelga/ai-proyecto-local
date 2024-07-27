from openai import OpenAI
import lector_utils as lect

def procesarConsulta(query, contexto):
    consulta = generarConsulta(query, contexto)
    response = obtenerRespuesta(consulta)
    return response


def generarConsulta(consulta, contenido):
    query = consulta
    context = contenido
    messages = [
        {"role": "system", "content": "Eres un asistente util."},
        {"role": "user", "content": f"Documentos: {context}"},
        {"role": "user", "content": f"Pregunta: {query}"}
    ]
    return messages


def obtenerRespuesta(messages):
    ruta_config = './secret-key-open-ai.json'
    texto_completo = ""
    api_key = lect.obtener_secret_key(ruta_config)
    client = OpenAI(api_key=api_key) if api_key else None
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        stream=True,
        max_tokens=50,
        presence_penalty=0,
        temperature=0
    )
    for chunk in stream:
        texto_completo += chunk.choices[0].delta.content or ""
    return texto_completo
