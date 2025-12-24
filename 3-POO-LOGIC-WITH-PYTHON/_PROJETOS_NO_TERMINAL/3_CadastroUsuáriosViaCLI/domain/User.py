from exceptions.InvalidEmail import InvalidEmail

# ➡️ Regras puras do negócio
# Email válido
# Nenhuma dependência externa
# Estado protegido

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self._validate()
        
    def _validate(self):
        if "@" not in self.email:
            print(self.email)
            raise InvalidEmail("E-mail inválido")
        
    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"