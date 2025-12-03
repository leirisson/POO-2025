

# declaração do nome
class Funcionario:
    def __init__(self, nome: str, idade:int):
        self.nome = nome
        self.idade = idade
        
    def exibi_info(self): #metodo:
        informacao = f"Nome: {self.nome} tem a Idade: {self.idade}"
        return informacao
        
    


    