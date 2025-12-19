class CreateAccountCase:
    def __init__(self, repository):
        self.repository = repository
    
    def execute(self, account):
        self.repository.save(account)