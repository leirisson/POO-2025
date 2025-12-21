
class AccountService:
    # SERVICE — ORQUESTRAÇÃO
    """
    SERVICE:
    - Orquestra os casos de uso
    - Não contém regras de negócio
    """
    def __init__(self, create_user_account, withdraw_user_account, repository):
        self.create_user_account = create_user_account
        self.withdraw_user_account = withdraw_user_account
        self.repository = repository
    
    def list_accounts(self):
        return self.repository.find_all()
    
    def delete_account(self, number):
        self.repository.delete(number)
