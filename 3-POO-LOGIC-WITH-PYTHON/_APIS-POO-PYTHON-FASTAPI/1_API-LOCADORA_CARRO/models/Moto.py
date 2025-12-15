from .Veiculo import Veiculo


class Moto(Veiculo):
    def __init__(
        self, 
        marca: str, 
        modelo: str, 
        ano: int, 
        valor_diaria: float, 
        cilindradas: int):
        super().__init__(marca, modelo, ano, valor_diaria)
        self.cilindradas = cilindradas
    
    def calcular_aluguel(self, dias):
        """
        POLIMORFISMO
        Motos têm desconto de 10%
        """
        total = self._valor_diaria * dias
        return total * 0.9
        