from domain.Account import Account
from exceptions.BussinessException import BussinessException

class CheckinAccount(Account):
    """
    REGRA DO DOMÍNIO:
    - Conta corrente pode ficar negativa até -1000
    """
    
    def withdraw(self, amount: float):
        if self._balance - amount < -1000:
            raise BussinessException("Limite da conta corrente excedido")
        self._balance -= amount
    