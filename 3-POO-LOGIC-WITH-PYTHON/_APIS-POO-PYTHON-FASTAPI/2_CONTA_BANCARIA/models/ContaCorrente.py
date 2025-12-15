from .ContaBancaria import ContaBancaria


class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, nome_titular, saldo = 0):
        super().__init__(numero_conta, nome_titular, saldo)
        
    def depositar(self, valor):
        if(valor > 0):
            saldo = self.get_saldo()
            saldo += valor
            self.set_saldo(saldo)
            return True
        return False
    
    def sacar(self, valor):
        saldo = self.get_saldo()
        if(valor > 0 or saldo <= -1000):
            saldo -= valor
            self.set_saldo(saldo)
            return True
        return False
    
    def extrato(self) -> dict:

        extrarto = {
            "numero_Conta": self.get_numero_conta(),
            "nome" : self.get_nome_titular(),
            "saldo": self.get_saldo()
        
        }
        
        return extrarto