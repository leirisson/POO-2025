from exceptions.DomainException import DomainException
from use_cases.create_user import CreateUseCase

# ➡️ Controller não tem regra
# ➡️ Apenas:
# Chama caso de uso
# Traduz exceções
# Exibe mensagens no CLI


class UserController:
    def __init__(self, create_use_user_case: CreateUseCase):
        self.create_use_user_case = create_use_user_case
    
    def create_user(self, name:str, email:str):
        try:
            user = self.create_use_user_case.execute(name, email)
            
            print(f"Usúario criado com sucesso: {user}")
        except DomainException as e:
            print(f"Erro de negócio: {e}")
        except Exception as e:
            print(f"🔴 Erro inesperado")
            print(f"Detalhes: {e}")