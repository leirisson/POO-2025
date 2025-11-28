
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def emitir_som(self):
        print("o animal emite um som.")
        
        
class Cachorro(Animal):
    def emitir_som(self) -> str:
        return "au - au "

class Gato(Animal):     
    def emitir_som(self) -> str:
        return "miau - miau"
    
class Boi(Animal):
    def emitir_som(self):
        return "Eu sou o iago !"
    
def main():
    # cachorro = Cachorro("rex")
    # cachorro.emitir_som()
    # # gato 
    # gato = Gato("luna")
    # # gato.emitir_som()
    
    # polimorfismo
    animais = [Cachorro("Rex"), Gato("lina"), Boi("Iago")]
    
    for animal in animais:
        # se animal for uma instacia (filho(a)) de da Classe Animal, será emitido o som do animal correspondente
        if isinstance(animal, Cachorro):
            print(f"Cachorro faz: ", animal.emitir_som())
            
        elif isinstance(animal, Boi) : 
            print(f"O iago faz o som: {animal.emitir_som()}")
        else:
            print(f"O Leirisson faz o som: ", animal.emitir_som())

if __name__ == "__main__":
    main()