from domain.account import Account

class SavingsAccount(Account):
    def withdraw(self, amount: float):
        if amount > self._balance:
            raise Exception("Saldo insuficiente")
        self._balance -= amount
        
        