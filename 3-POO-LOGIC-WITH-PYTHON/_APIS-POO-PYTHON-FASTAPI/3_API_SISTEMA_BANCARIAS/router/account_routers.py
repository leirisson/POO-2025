from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def hello_api():
    return   {
        "status":200,
        "messge" : "api funcionando com sucesso"
    }





 