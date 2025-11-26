class Carro:
    def __init__(self, marca:str, modelo:str, velocidade:int=0) -> None:
        self._marca = marca
        self._modelo = modelo
        self._velocidade = velocidade
        self._velocidade_padrao = 10
        
    def acelerar(self):
        if self._velocidade < 100:
            self._velocidade += self._velocidade_padrao
        else:
            print("Você alcançõu a velocidade maxima do veiculo.")
    
    def frear(self):
        if self._velocidade > 0:
            self._velocidade -= self._velocidade_padrao
        else:
            print("O carro ja está parado!.")
        
        
    def velocidade_atual(self):
        return self._velocidade