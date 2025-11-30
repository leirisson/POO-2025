class Conta_Bancaria:
    def __init__(self, titular:str, saldo_inicial:float):
        self.titular = titular
        self.__saldo = saldo_inicial
    
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, valor):
        self.__saldo = valor
    
    def depositar(self, valor) -> bool:
        saldo_atual = self.get_saldo()
        if valor > 0:
            saldo_atual += valor
            self.set_saldo(saldo_atual)
            return True
        return False
    
    def sacar(self, valor: float) -> bool:
        saldo_atual = self.get_saldo()
        if 0 < valor <= saldo_atual:
            saldo_atual -= valor
            self.set_saldo(saldo_atual)
            return True
        return False
    