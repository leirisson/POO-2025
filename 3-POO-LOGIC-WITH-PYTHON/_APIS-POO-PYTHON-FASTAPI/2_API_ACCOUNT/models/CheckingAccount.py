from models.Account import Account


class CheckingAccount(Account):
   LIMIT = -1000
   
   def withdraw(self, amount: float):
      if amount <= 0:
          raise ValueError("O valor de saque deve ser positivo.")
      if self.__balance - amount < self.LIMIT:
          raise ValueError("Limite de cheque especial excedidio.")
      self.__balance -= amount 