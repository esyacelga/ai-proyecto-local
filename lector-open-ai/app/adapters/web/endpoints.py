import os

import PyPDF2
from fastapi import APIRouter, Form
from fastapi import File, UploadFile, HTTPException
from starlette.responses import JSONResponse

import app.core.services.lector_service as lect
from app.core.services.example_service import get_message

router = APIRouter()


@router.get("/hello")
def read_hello():
    return {"message": "Hello, World!"}


@router.get("/greet/{name}")
def read_greet(name: str):
    message = get_message(name)
    return {"message": message}


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
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            num_pages = len(reader.pages)
            if num_pages > 15:
                os.remove(file_path)  # Eliminar el archivo temporal
                raise HTTPException(status_code=400, detail="El archivo PDF tiene más de 15 páginas")

        resultado, mensaje = lect.procesarDocumento(creacion_usuario, creacion_equipo, file_path)
        if resultado == True:
            return JSONResponse(status_code=200, content={"message": mensaje, "file_path": file_path})
        else:
            return JSONResponse(status_code=200,
                                content={"message": "Advertencia:", "file_path": file_path, "detalle": mensaje})
    else:
        raise HTTPException(status_code=400, detail="El archivo debe ser un PDF")
