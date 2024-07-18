import os

from fastapi import FastAPI, File, UploadFile, HTTPException
from starlette.responses import JSONResponse

app = FastAPI()


@app.post("/processUploadPdf")
async def processUploadPdf(file: UploadFile = File(...)):
    # Validar el archivo PDF
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type")
    # pdf_bytes = await file.read()
    # texto = dai.onlineProcessingPdf(pdf_bytes)
    if file.filename.endswith(".pdf"):
        # Guardar el archivo en el servidor
        file_path = os.path.join("uploads", file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return JSONResponse(content={"message": "Archivo PDF subido correctamente", "file_path": file_path})
    else:
        raise HTTPException(status_code=400, detail="El archivo debe ser un PDF")

    # Enviar una respuesta exitosa
    return {"message": "File uploaded successfully", "content": '4545'}
