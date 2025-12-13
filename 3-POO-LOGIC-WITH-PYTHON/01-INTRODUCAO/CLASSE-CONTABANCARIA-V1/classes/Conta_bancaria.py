

class Conta_bancaria:
    def __init__(self, saldo:float=0.0):
        self.saldo = float(saldo)
    
    
    def depositar(self, valor:float):
        self.saldo += valor
    
    def getSaldo(self) -> float:
        return self.saldo
    
    def sacar(self, valor:float):
        if(valor > 0 and valor <= self.saldo):
            self.saldo -= valor
        else:
            return "Saldo insuficiente."