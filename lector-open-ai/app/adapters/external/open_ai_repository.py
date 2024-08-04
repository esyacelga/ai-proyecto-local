from openai import OpenAI

from app.adapters.config.settings import OPEN_AI_API_KEY_CONNECTION
from app.utils import lector_utils as lect


def procesarConsulta(query, contexto):
    consulta = generarConsulta(query, contexto)
    response, texto = obtenerRespuesta(consulta)
    return response, texto


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
    ruta_config = OPEN_AI_API_KEY_CONNECTION
    texto_completo = ""
    result, text = lect.obtener_secret_key(ruta_config)
    if result == False:
        return result, text

    client = OpenAI(api_key=text) if text else None
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
    return 1, texto_completo
