

class Account:
    def __init__(self, number: str, owner:str):
        self.number = number
        self.owner = owner
        self._balance = 0.0
        
    def get_balance(self):
        return self._balance
    