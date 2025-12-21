# Service coordena vários casos de uso
# Ele NÃO cria regras de negócio

# 🧠 Teoria aplicada
# Se amanhã surgir:
# saque + taxa + notificação
# 👉 isso fica aqui

class AccountService:
    def __init__(self, create_use_case, withdraw_use_case, repository):
        self.create_use_case = create_use_case
        self.withdraw_use_case = withdraw_use_case
        self.repository = repository
        
    def list_accounts(self):
        return self.repository.find_all()

    def delete_account(self, number):
        self.repository.delete(number)
        