# # Herança com super()
# ====================
# # clase Pai
# ====================
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        return f"olá, o meu nome é: {self.nome}"
class Estudante:
    pass