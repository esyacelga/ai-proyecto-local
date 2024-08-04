import os

import PyPDF2
from fastapi import APIRouter, Form
from fastapi import File, UploadFile, HTTPException
from starlette.responses import JSONResponse

import app.core.services.lector_service as lect

router = APIRouter()


@router.get("/hello")
def read_hello():
    return {"message": "Hello, World!"}


@router.get("/get_first_answer/{query}")
def get_first_answer(query: str):
    response, message = lect.get_first_answer_from_documents(query)
    return {
        "response": response,
        "message": message
    }


@router.get("/get_answers_by_text/{context}/{query}")
def get_answers_by_text(context: str, query: str):
    response, message = lect.get_answer_from_context_and_query(context, query)
    return {
        "response": response,
        "message": message
    }


@router.post("/processUploadPdf")
async def processUploadPdf(file: UploadFile = File(...),
                           creacion_usuario: str = Form(...),
                           creacion_equipo: str = Form(...)):
    # Validar el archivo PDF
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type")
    # pdf_bytes = await file.read()
    # texto = dai.onlineProcessingPdf(pdf_bytes)
    if file.filename.endswith(".pdf"):
        # Crear el directorio 'uploads' si no existe
        upload_dir = "uploads"
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        # Guardar el archivo en el servidor
        file_path = os.path.join(upload_dir, 'documento.pdf')
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        # Validar el número de páginas del PDF
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            num_pages = len(reader.pages)
            if num_pages > 16:
                os.remove(file_path)  # Eliminar el archivo temporal
                raise HTTPException(status_code=400, detail="El archivo PDF tiene más de 16 páginas")

        if not os.path.exists(file_path):
            raise HTTPException(status_code=400, detail="El archivo no se ha cargado en el servidor")

        resultado, mensaje = lect.procesarDocumento(creacion_usuario, creacion_equipo, file_path)
        os.remove(file_path)  # Eliminar el archivo temporal
        if resultado == True:
            return JSONResponse(status_code=200, content={"response": resultado, "message": mensaje})
        else:
            return JSONResponse(status_code=200, content={"response": resultado, "message": mensaje})
    else:
        raise HTTPException(status_code=400, detail="El archivo debe ser un PDF")
