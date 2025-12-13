from classes.Livro import Livro

livros = []

def main():
    for i in range(1,3):
        
        titulo = input("titulo: ")
        autor = input("autor: ")
        ano_publicacao = input("ano de publicação: ")
        livro = Livro(titulo, autor, ano_publicacao)
        livros.append(livro)

    for livro in livros:
        print(livro.descricao())
    
    
if __name__ == "__main__":
    main()