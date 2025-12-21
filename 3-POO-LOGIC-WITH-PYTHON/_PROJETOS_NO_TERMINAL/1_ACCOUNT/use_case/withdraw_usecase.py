from exceptions.business_exception import BusinessException

class WithdrawUseCase:
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, number, amount):
        # 🎯 AÇÃO DO CASO DE USO:
        # Realizar saque em uma conta existente
        account = self.repository.find_by_number(number)
        if not account:
            raise BusinessException("Conta não encontrada")
        
        account.withdraw(amount)