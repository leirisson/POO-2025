

class AccountRepository:
    """
    RESPONSABILIDADE:
    - Guardar e recuperar contas
    - Não conhece regras de negócio
    """
    
    def __init__(self):
        self._accounts = {}
        
    def save(self, account):
        self._accounts[account.number] = account
    
    def find_by_number_account(self,number):
        return self._accounts.get(number)
    
    def find_all(self):
        return self._accounts.values()
    
    def delete(self, number):
        if number in self._accounts:
            del self._accounts[number]