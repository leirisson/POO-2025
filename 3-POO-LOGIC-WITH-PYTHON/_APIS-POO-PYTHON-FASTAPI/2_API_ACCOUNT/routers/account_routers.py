from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def hello_api():
    return {"message": "API RODANDO!"}