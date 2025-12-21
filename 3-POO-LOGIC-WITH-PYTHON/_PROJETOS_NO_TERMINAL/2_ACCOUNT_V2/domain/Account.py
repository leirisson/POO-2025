from exceptions.BussinessException import BussinessException

"""
    ENTIDADE DO DOMÍNIO

    Regras do domínio:
    - Conta tem saldo protegido ✅
    - Saldo não pode ser alterado diretamente ✅
"""

class Account:
    def __init__(self, number: str, owner: str):
        self.number = number
        self.owner = owner
        self._balance = 0.0
        
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount: float):
        """
        REGRA DE NEGÓCIO:
        - Não aceita depósito negativo ou zero ✅
        """
        if amount <= 0:
            raise BussinessException("Depósito invalido")
        self._balance += amount
        