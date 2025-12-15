from models.Carro import Carro  # ← isso é o módulo Carro.py, não a classe!
from models.Moto import Moto

class VeiculoService: 
    def calcular_aluguel_carro(
        self,
        marca: str,
        modelo: str,
        ano: int,
        valor_diaria: float,
        portas: int,
        dias: int
    ):
        carro = Carro(marca, modelo, ano, valor_diaria, portas)
        return carro.calcular_aluguel(dias)
    
    def calcular_aluguel_moto(
        self,
        marca: str,
        modelo: str,
        ano: int,
        valor_diaria: float,
        cilidradas: int,
        dias: int
        ):

        moto = Moto(marca, modelo, ano, valor_diaria, cilidradas)
        return moto.calcular_aluguel(dias)