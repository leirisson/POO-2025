from services.veiculo_service import VeiculoService

class VeiculoController:
    def __init__(self):
        self.service = VeiculoService()
    
    def aluguel_carro(self, data: dict):
        return self.service.calcular_aluguel_carro(
            marca=data["marca"],
            modelo=data["modelo"],
            ano=data["ano"],
            valor_diaria=data["valor_diaria"],
            portas=data["portas"],
            dias=data["dias"]
        )
    
    def aluguel_moto(self, data:dict):
        return self.service.calcular_aluguel_moto(
            marca=data["marca"],
            modelo=data["modelo"],
            ano=data["ano"],
            valor_diaria=data["valor_diaria"],
            cilidradas=data["cilindradas"],
            dias=data["dias"]
        )
    
    