# Repository é responsável por armazenar e recuperar dados
# Aqui usamos memória para simplificar


# 🧠 Teoria aplicada
# Use case não sabe onde salva
# Hoje é memória, amanhã banco, depois API externa


class AccountRepository:
    def __init__(self):
        self._accounts = {}
        
    def save(self, account):
        self._accounts[account.number] = account
        
    def find_by_number(self, number):
        return self._accounts.get(number)
    
    
    def find_all(self):
        return self._accounts.values()

    def delete(self, number):
        if number in self._accounts:
            del self._accounts[number]