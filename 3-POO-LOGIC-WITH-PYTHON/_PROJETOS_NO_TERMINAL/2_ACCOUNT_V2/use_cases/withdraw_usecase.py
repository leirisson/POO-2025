from exceptions.BussinessException import BussinessException



class WithdrawUseCase:
    """
    CASO DE USO:
    - Realizar saque em uma conta
    """
    
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, number, amount):
        account = self.repository.find_by_number_account(number)
        
        # se a conta não existi
        if not account:
            raise BussinessException("Conta não encontrada")
        
        # Polimorfismo: não importa o tipo da conta
        account.withdraw(amount)
        