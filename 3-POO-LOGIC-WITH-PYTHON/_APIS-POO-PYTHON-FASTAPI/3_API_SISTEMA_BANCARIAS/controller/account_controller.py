


class AccountController:
    def __init__(self, service):
        self.service = service
        
    def creta_account(self, number: str, owner:str):
        self.service.deposit(number, )