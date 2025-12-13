
class Livro:
    def __init__(self, nome: str, autor: str, ano_publicacao: int) -> None:
        self.nome = nome
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    
    def descricao(self) -> str:
       return f"Livro: {self.nome} por {self.autor} ano de {self.ano_publicacao}" 