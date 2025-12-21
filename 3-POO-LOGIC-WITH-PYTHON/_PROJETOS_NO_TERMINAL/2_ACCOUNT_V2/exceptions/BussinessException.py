
# Erros de negócio NÃO são erros técnicos
# Eles representam regras violadas do domínio

class BussinessException(Exception):
    pass