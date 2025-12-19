from models.Account import Account


class SavingsAccount(Account):
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("O valor do saque deve ser positivo")
        if self.__balance - amount < 0:
            raise ValueError("Conta poupamça não pode ficar negativa.")
        self.__balance -= amount
        
    def apply_interest(self):
        self.__balance *=1.005