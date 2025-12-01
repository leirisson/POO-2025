from classes.Produto import Produto

class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso):
        super().__init__(nome, preco)
        self.__peso = peso
    
    def get_peso(self):
        return self.__peso
    
    def set_peso(self, novo_peso):
        self.__peso = novo_peso
        
    def calcular_total(self, quantidade):
        peso = self.get_peso()
        subtotoal = super().calcular_total(quantidade)
        frete = peso * quantidade * 0.5
        return subtotoal + frete
            
    def adicionar_produto_no_estoque(self, quantidade_do_produto):
        return super().adicionar_produto_no_estoque(quantidade_do_produto)
    
    
    
        