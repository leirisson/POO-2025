


class AccountController:
    # CONTROLLER — INTERFACE COM O MUNDO EXTERNO
    """
    CONTROLLER:
    - Traduz entrada do usuário em ações do sistema
    """
    
    def __init__(self, service):
        self.service = service
        
    def create_account(self, number, owner, acc_type): # acc_tipe = account_type
        return self.service.create_user_account.execute(number, owner, acc_type)
    
    def withdraw(self, number, amount):
        self.service.withdraw_user_account.execute(number, amount)
        
    def list_accounts(self):
        return self.service.list_accounts()
    
    def delete_account(self, number):
        self.service.delete_account(number)
    
    