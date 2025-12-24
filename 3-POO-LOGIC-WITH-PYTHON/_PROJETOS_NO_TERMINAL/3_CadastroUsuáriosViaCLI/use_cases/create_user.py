# ➡️ Orquestra tudo
# Valida regras de negócio
# Cria entidade
# Persiste
# Chama serviço externo

from repository.user_repository import UserRepository
from services.email_service import EmailService
from exceptions.EmailAlreadyExists import EmailAlreadyExists
from domain.User import User


class CreateUseCase:
    def __init__(self, repository: UserRepository, emailService: EmailService):
        self.repository = repository
        self.emailService = emailService
        
    def execute(self, name: str, email: str):
        if self.repository.find_by_email(email):
            raise EmailAlreadyExists("E-mail já cadastrado")
        
        # criando objeto
        user = User(name, email)
        self.repository.save(user) # salvando no banco de dados
        self.emailService.send_welcome(email) # enviando email de boas vindas
        
        return user
        
    