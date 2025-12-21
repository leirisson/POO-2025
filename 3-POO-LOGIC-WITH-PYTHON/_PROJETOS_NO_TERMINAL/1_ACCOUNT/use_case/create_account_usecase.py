from domain.checking_account import CheckingAccount
from domain.savings_account import SavingsAccount
from exceptions.business_exception import BusinessException

class CreateAccountUseCase:
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, number, owner, account_type):
        # 🎯 AÇÃO DO CASO DE USO:
        # Criar uma nova conta conforme o tipo escolhido
        
        if self.repository.find_by_number(number):
            raise BusinessException("Conta já exite")
        
        if account_type == "checking":
            account = CheckingAccount(number, owner)
        elif account_type == "savings":
            account = SavingsAccount(number, owner)
        else:
            raise BusinessException("opção invalida.")
        self.repository.save(account)
        return account