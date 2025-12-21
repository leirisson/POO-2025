from domain.account import Account
from exceptions.business_exception import BusinessException

class CheckingAccount(Account):
    def __init__(self, number, owner):
        super().__init__(number, owner)
        self._balance = 0.0

        
    def withdraw(self, amount:float):
        # 📜 REGRA DE DOMÍNIO:
        # Conta corrente pode ficar negativa até -1000
        if self._balance - amount < -1000:
            raise BusinessException("Limite da conta corrente excedido")
        self._balance -= amount