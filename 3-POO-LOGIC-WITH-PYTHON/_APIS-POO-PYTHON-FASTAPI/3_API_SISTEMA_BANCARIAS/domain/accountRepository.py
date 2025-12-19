
class AccountRepository:
    def __init__(self):
        self.accounts = []
        
    def save(self, account):
        self.accounts.append(account)
        
    def find_by_number(self, number):
        return next((a for a in self.accounts if a.number == number), None)