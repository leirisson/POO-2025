from abc import ABC, abstractmethod


class Account:
    def __init__(self, number: str, holder: str, balance: float = 0.0):
        self.number = number
        self.holder = holder
        self.__balance = balance
        
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("O valor de déposito deve ser positivo.")
        self.__balance += amount
        
    @abstractmethod
    def withdraw(self, amount: float): # retirar ou sacar
        pass
    
    