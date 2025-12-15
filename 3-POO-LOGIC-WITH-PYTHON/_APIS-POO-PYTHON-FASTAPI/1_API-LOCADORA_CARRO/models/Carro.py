from .Veiculo import Veiculo


class Carro(Veiculo):
    def __init__(
        self, 
        marca: str, 
        modelo: str, 
        ano: int, 
        valor_diaria: int,
        portas: int,
        ):
        super().__init__(marca, modelo, ano, valor_diaria)
        self.portas = portas
    
    def calcular_aluguel(self, dias: int) -> float:
        """
        POLIMORFISMO
        Carros têm taxa fixa extra de R$ 50
        """
        taxa_fixa_extra = 50
        
        return (self._valor_diaria * dias) + taxa_fixa_extra