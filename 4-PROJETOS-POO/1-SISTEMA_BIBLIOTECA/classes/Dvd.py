from classes.Item_Biblioteca import ItemBiblioteca


class Dvd(ItemBiblioteca):
    def __init__(self, titulo, codigo, duracao):
        super().__init__(titulo, codigo)
        self.__duracao = duracao
    
    def emprestar(self):
        status_do_item = self.get_disponivel()
        if status_do_item:
            resultado = super().emprestar()
            return f"DVD: {resultado} - Prazo: 7 dias"
        return "DVD indiposnivel."
    
    def get_duracao(self):
        return f"Filme: {self._titulo} tem {self.__duracao} minutos"
    