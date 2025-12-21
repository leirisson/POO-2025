from domain.Account import Account
from exceptions.BussinessException import BussinessException


class SavingsAccount(Account):
    """
    REGRA DO DOMÍNIO:
    - Conta poupança NÃO pode ficar negativa
    """
    
    def withdraw(self, amount: float):
        if amount > self._balance:
            raise BussinessException("Saldo insuficiente")
        self._balance -= amount