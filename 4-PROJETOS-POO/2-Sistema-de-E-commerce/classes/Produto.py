class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco # encapsulamento
        self.__estoque = 0
        
    def get_preco(self):
        return self.__preco
    def set_preco(self, novo_preco):
        self.__preco = novo_preco
        
        
    def get_quantidade_em_estoque(self):
        return self.__estoque
    def set_estoque(self, nova_quantidade):
        self.__estoque += nova_quantidade
        
    
    def adicionar_produto_no_estoque(self, quantidade_do_produto):
        estoque_atual = self.get_quantidade_em_estoque()
        if(quantidade_do_produto > 0):
            estoque_atual += quantidade_do_produto
            self.set_estoque(estoque_atual)
            
    def calcular_total(self, quantidade):
        estoque_atual = self.get_quantidade_em_estoque()
        preco_produto = self.get_preco()
        if quantidade <= estoque_atual:
            return preco_produto * quantidade
        return 0 
    
    def tem_estoque(self, quantidade):
        estoque_atual = self.get_quantidade_em_estoque()
        verificar_se_tem_estoque =  quantidade <= estoque_atual
        return verificar_se_tem_estoque
    