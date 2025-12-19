from domain.account import Account

class ChechingAccount(Account):
    def withdraw(self, amount: float):
        if self._balance - amount < -1000:
            raise Exception("Limite excedidio")
        self._balance -= amount
    


