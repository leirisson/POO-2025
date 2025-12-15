from abc import ABC, abstractmethod

class Veiculo(ABC):
    """
    Classe abstrata (ABSTRAÇÃO)
    Não pode ser instanciada diretamente
    """
    
    def __init__(self, marca: str, modelo: str, ano:int, valor_diaria:float):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self._valor_diaria = valor_diaria # ENCAPSULAMENTO
    
    @abstractmethod
    def calcular_aluguel(self, dias:int) -> float:
        """
        Método abstrato
        Obriga as classes filhas a implementar
        """
        pass
    
    
    def get_valor_diaria(self):
        return self._valor_diaria