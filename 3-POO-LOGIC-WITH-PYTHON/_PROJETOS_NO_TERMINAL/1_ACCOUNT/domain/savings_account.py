from domain.account import Account
from exceptions.business_exception import BusinessException


class SavingsAccount(Account):
    def withdraw(self, amount: float):
        # 📜 REGRA DE DOMÍNIO:
        # Conta poupança NÃO pode ficar negativa
        if amount > self._balance:
            raise BusinessException("Saldo insuficiente")
        self._balance -= amount