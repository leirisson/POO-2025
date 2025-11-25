



class Veiculo:
    def __init__(self, marca: str, modelo:str, cor:str) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor =  cor
    
    def descricao(self) -> str:
        descricao_carro = f"""
DESCRIÇÃO DO CARRO
Marca: {self.marca},
Model: {self.modelo},
Cor: {self.cor}
        """
        
        return descricao_carro