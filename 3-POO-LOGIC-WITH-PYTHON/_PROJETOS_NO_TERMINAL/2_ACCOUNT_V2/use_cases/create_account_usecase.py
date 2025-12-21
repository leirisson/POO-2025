from domain.checking_account import CheckinAccount
from domain.savings_account import SavingsAccount
from exceptions.BussinessException import BussinessException



class CreateAccountUseCase:
    """
    USE CASES — AÇÕES DO SISTEMA
    CASO DE USO:
    - Criar uma nova conta
    """
    
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, number, owner, account_type):
        
        # verifica se a conta já existe
        if self.repository.find_by_number_account(number):
            raise BussinessException("Conta já existe")
        
        
        if account_type == "checking":
            account = CheckinAccount(number, owner)
        elif account_type == "savings":
            account = SavingsAccount(number, owner)
        else: 
            raise BussinessException("Tipo de conta inválida")    
        
        self.repository.save(account)
        return account