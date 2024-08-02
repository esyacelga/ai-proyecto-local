
from fastapi import FastAPI
from app.adapters.web.endpoints import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")

# Opcional: Personaliza la documentación
app.title = "Document AI - Open Ai"
app.description = "Document application using FastAPI and Document AI"
app.version = "1.0.0"