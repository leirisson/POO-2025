


class ItemBiblioteca:
    def __init__(self, titulo, codigo):
        self._titulo = titulo
        self._codigo = codigo # encapsulamento
        self.__disponivel = True # atributo privado
        
    def get_titulo(self):
        return self._titulo
    
    def set_titulo(self, novo_titulo):
        self._titulo = novo_titulo
    
    def get_codigo(self):
        return self._codigo
    
    def set_codigo(self, novo_codigo):
        self._codigo = novo_codigo
    
    def get_disponivel(self):
        return self.__disponivel
    
    def set_disponivel(self, novo_status):
        self.__disponivel = novo_status
        
    def emprestar(self) -> str: # Será sobrescrito (Polimorfismo) pela classe filha
        status_item = self.get_disponivel()
        if status_item:
            novo_status_item = False
            self.set_disponivel(novo_status_item)
            return f"{self.get_titulo()} emprestado com sucesso!"
        return f"Item: {self.get_titulo()} indisponivel."
            
    def devolver_item(self):
        novo_status_item = True
        self.set_disponivel(novo_status_item)
        return f"{self.get_titulo()} devolvido."
    
    def verifica_esta_disponivel(self):
        status_item = self.get_disponivel()
        return status_item
    
        
    