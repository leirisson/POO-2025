from fastapi import APIRouter



router = APIRouter(prefix="/contas", tags=["Contas"])


@router.get("/")
def teste_rota():
    return {
    "status" : "200",
    "message": "API rodando com sucesso."
    }