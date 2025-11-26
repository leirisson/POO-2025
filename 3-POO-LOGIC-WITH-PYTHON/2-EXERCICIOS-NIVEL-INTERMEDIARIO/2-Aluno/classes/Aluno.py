class Aluno:
    def __init__(self, nome:str) -> None:
        self.nome = nome
        self.notas = []
        
    def adicionar_nota(self, nota:float):
        if(nota >=0):
            self.notas.append(nota)
        else: 
            raise Exception("Erro, não podemos adicionar uma nota negativa.")
    
    def calcular_media(self) -> float:
        divisor = len(self.notas)
        soma_das_notas = 0
        
        for n in range(divisor):
            soma_das_notas += self.notas[n]
        media = soma_das_notas / divisor
        
        return media
    
    def verificar_status_aluno(self) -> str :
        media = self.calcular_media()
        if(media >= 7):
           return  f"o aluno: {self.nome} está APROVADO. com a média: {media:.1f}"
        else:
            return  f"o aluno: {self.nome} está REPROVADO. com a média: {media:.1f}"