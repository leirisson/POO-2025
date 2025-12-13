


class Pessoa:
    def __init__(self, nome, idade,altura) -> None:
        self._nome = nome
        self._idade = idade
        self._altura = altura
    
    
    def getNome(self):
        return self._nome
    
    def setNome(self, novoNome):
        if(len(novoNome) < 3):
            print("erro, o nome deve conter no minimo 3 caracter")
        self._nome = novoNome
    



