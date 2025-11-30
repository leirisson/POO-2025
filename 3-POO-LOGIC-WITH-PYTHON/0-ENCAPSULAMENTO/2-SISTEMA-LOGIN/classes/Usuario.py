class Usuario:
    def __init__(self, nome: str, senha:str) -> None:
        self.nome = nome
        self.__senha = senha
        
    def validar_senha(self, senha_digitada: str):
        verificar_se_as_senha_sao_iguais = (senha_digitada == self.__senha) 
        return verificar_se_as_senha_sao_iguais
    
    def alterar_senha(self, senha_antiga:str, nova_senha:str):
        if self.validar_senha(senha_antiga):
            self.__senha = nova_senha
            return "Senha alterada com sucesso!."
        return "Senha antiga incorreta."