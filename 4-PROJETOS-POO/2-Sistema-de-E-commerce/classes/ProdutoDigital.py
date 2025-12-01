from classes.Produto import Produto

class ProdutoDigital(Produto):
    def __init__(self, nome, preco, tamanho_mb):
        super().__init__(nome, preco)
        self.__tamanho_mb = tamanho_mb
    
    def get_tamanho(self):
        return f"{self.__tamanho_mb}MB"
    
    def calcular_total(self, quantidade):
        # Produtos digitais têm desconto progressivo
        subtotal = super().calcular_total(quantidade)
        if(quantidade > 5):
            return subtotal * 0.85
        return subtotal
    
    def adicionar_produto_no_estoque(self, quantidade_do_produto):
        return super().adicionar_produto_no_estoque(quantidade_do_produto)
    
    