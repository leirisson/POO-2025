

class Funcionario:
    def __init__(self, nome: str, cargo: str, salario:float):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    def almento_percentual(self, valor_almento: int):
        almento = self.salario * (valor_almento/100)
        self.salario += almento
    
    
    def calcular_salario_anual(self):
        return self.salario * 12