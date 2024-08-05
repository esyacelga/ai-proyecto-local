
from fastapi import FastAPI
from app.adapters.web.endpoints import router as api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:4200",  # URL de tu aplicación Angular
    "http://your-angular-app-domain.com",  # Agrega otras URLs según sea necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api")

# Opcional: Personaliza la documentación
app.title = "Document AI - Open Ai"
app.description = "Document application using FastAPI and Document AI"
app.version = "1.0.0"