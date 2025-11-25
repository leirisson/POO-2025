from classes.Livro import Livro



def main():
    livro1 = Livro('Escreveu, mas não  leu', 'Leirisson Santos', 2016)
    descricao = livro1.descricao()
    print(descricao)
    
    
if __name__ == "__main__":
    main()