from typing import List, Optional
from domain.User import User

# ➡️ Simula banco de dados
# ➡️ Isolado do domínio e do caso de uso

class UserRepository:
    def __init__(self):
        self._users: List[User] = []
        
    def save(self, user: User):
        self._users.append(user)
        
    def find_by_email(self, email: str) -> Optional[User]:
        for user in self._users:
            if user.name == email:
                return user
        return None
    
    def list_all(self):
        return self._users