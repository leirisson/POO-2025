from classes.Item_Biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, titulo, codigo, autor, paginas): # Herança
        super().__init__(titulo, codigo)
        self.autor = autor
        self.__paginas = paginas # Encapsulamento
        
    def emprestar(self): # polimorfismo
        status_tem = self.get_disponivel()
        if status_tem:
            resultado_emprestimo = super().emprestar()
            return f"LIVRO: {resultado_emprestimo} - Prazo: 14 dias."
        return "Livro indisponivel."
    
    def get_info(self):
        return f"LIVRO:'{self._titulo}' de {self.autor} ({self.__paginas}) pág."
    