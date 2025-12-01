from classes.Dvd import Dvd
from classes.Livro import Livro


def main():
    # cadstrando livro
    titulo  = input("titulo do livro: ")
    codigo  = input("codigo do livro: ") 
    autor   = input("autor do livro: ") 
    paginas = int(input("paginas do livro: "))
    
    # instanciando um livro
    livro = Livro(titulo, codigo, autor, paginas)
    
    # instaciando um Dvd
    titulo  = input("titulo do DVD <: ")
    codigo  = input("codigo do DVD <: ")
    duracao = input("duração do fime <: ") 
    
    dvd_filme = Dvd(titulo, codigo, duracao)
    
    # Polimorfismo: mesmo método, comportamentos diferentes
    print(livro.emprestar())
    print(dvd_filme.emprestar())
    
    # Encapsulamento: acesso controlado
    print(livro.get_info())
    print(dvd_filme.get_duracao())


if __name__ == "__main__":
    main()