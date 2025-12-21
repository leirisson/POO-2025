# Controller traduz a entrada do usuário em ações do sistema
# 🧠 Controller

# Lê input
# Chama sistema
# Mostra resposta
# Zero regra de negócio

class Accountcontroller:
    def __init__(self, service):
        self.service = service
        
    def create_account(self):
        number  = input("Número da conta: ")
        owner = input("Titular: ")
        
        account_type =  input("Tipo (checking/savings): ")
        
        self.service.create_use_case.execute(number, owner, account_type)
        print("✅ Conta criada com sucesso")
        
    def withdraw(self):
        number = input("Número da conta: ")
        amount = float(input("Valor do saque: "))
        
        self.service.withdraw_use_case.execute(number, amount)
        print("✅ Saque realizado com sucesso.")
        
    
    def list_accounts(self):
        return self.service.list_accounts()

    def delete_account(self, number):
        self.service.delete_account(number)