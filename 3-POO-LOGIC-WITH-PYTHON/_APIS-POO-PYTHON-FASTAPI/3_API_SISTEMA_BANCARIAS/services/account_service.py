class AccountService:
    def deposit(self, account, amount):
        if amount <= 0:
            raise Exception("Valor inválido")
        self._balance += amount