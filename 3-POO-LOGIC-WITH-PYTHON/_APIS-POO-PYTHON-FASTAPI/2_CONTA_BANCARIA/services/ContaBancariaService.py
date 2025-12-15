from models.ContaCorrente import ContaCorrente
from models.ContaPoupanca import ContaPoupanca

class ContaBancariaService:
    
    def criar_conta_corrente(
        self,
         numero_conta: str, 
         nome_titular: str, 
         saldo: float
    ):
        conta = ContaCorrente(numero_conta, nome_titular, saldo)
        return conta.extrato()
    
    def conta_poupanca():
        pass