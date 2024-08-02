from fastapi import APIRouter
from app.core.services.example_service import get_message
from app.core.models.example_model import ExampleModel

router = APIRouter()

@router.get("/hello")
def read_hello():
    return {"message": "Hello, World!"}

@router.get("/greet/{name}")
def read_greet(name: str):
    message = get_message(name)
    return {"message": message}
