from .ContaBancaria import ContaBancaria


class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, nome_titular, saldo = 0):
        super().__init__(numero_conta, nome_titular, saldo)
        
    def sacar(self, valor: float):
        saldo = self.get_saldo()
        if(valor > 0 and saldo > 0):
            saldo -= valor
            self.set_saldo(saldo)
            return {
                "status": True,
                "message": "Saque realizado",
                "saldo_atual": self.get_saldo()
            }
            
    
    def depositar(self, valor):
        if(valor > 0):
            saldo = self.get_saldo()
            saldo += valor
            self.set_saldo(saldo)
            return {
                "status": True,
                "message": "Deposito realizado",
                "saldo_atual": self.get_saldo()
            }
        return {
                "status": False,
                "message": "Deposito não realizado",
                "saldo_atual": self.get_saldo()
            }
    
    def extrato(self):
        extrarto = {
            "numero_Conta": self.get_numero_conta(),
            "nome" : self.get_nome_titular(),
            "saldo": self.get_saldo()
        
        }
        return extrarto
    
    def aplicar_rendimento(self):
        saldo = self.get_saldo()
        redimento = saldo * 0.99
        self.set_saldo(redimento)
        return {
            "numero_Conta": self.get_numero_conta(),
            "nome" : self.get_nome_titular(),
            "rendimento": redimento 
        }