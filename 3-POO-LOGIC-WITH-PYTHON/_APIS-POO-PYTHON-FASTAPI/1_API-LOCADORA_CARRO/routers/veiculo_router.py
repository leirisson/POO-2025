from fastapi import APIRouter
from controllers.veiculo_controller import VeiculoController

router = APIRouter(prefix="/veiculos", tags=["Veículos"])
veiculo_controller = VeiculoController()

@router.get("/")
def veiculos():
    return {"message": "API funcionando"}


@router.post("/carro")
def calcular_aluguel_carro(data: dict):
    valor = veiculo_controller.aluguel_carro(data)
    return {
        "tipo": "Carro",
        "valor_total" : valor
    }
    
"""
rota para calcular o valor total do aluguel da moto
"""  
@router.post("/moto")
def calcular_aluguel_moto(data: dict):
    valor  = veiculo_controller.aluguel_moto(data)
    return {
        "tipo": "moto",
        "valor_total": valor
    }