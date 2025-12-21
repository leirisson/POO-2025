from exceptions.business_exception import BusinessException

# 🧠 Teoria aplicada
# Domínio não conhece input, não conhece controller
# Aqui vivem as regras reais do mundo

"""
    ENTIDADE DO DOMÍNIO

    Regras do domínio:
    - Conta tem saldo protegido
    - Saldo não pode ser alterado diretamente
"""
    
class Account:
    def __init__(self, number:  str, owner:str):
        self.number = number
        self.owner = owner
        self._balance = 0.0
        
    
    def deposit(self, amount: float):
        # 📜 REGRA DE DOMÍNIO:
        # Não é permitido depósito negativo ou zero
        if amount <= 0:
            raise BusinessException("Valor de depósito invalido.")
        self._balance += amount
    
    def get_balance(self):
        return self._balance