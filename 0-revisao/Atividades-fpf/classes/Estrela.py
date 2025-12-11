


class Estrela:
    total_estrelas_catalogadas = 0
    tipo_corpo = "Corpo Celeste"
    def __init__(self, nome:str, massa:float):
        self.nome = nome
        self.massa = massa
        self.em_atividade = True
        Estrela.total_estrelas_catalogadas += 1
        
    def descricao_estrela(self):
        status = self.verificar_atividade()
        return f"Nome Estrela: {self.nome} | Masa: {self.massa} | Atividade: {status} | quantidade de estrelas: {Estrela.total_estrelas_catalogadas}" 
    
    def verificar_atividade(self):
        if self.em_atividade:
            return "Em atividade"
        return "Sem atividade"