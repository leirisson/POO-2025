from classes.Pessoa import Pessoa

def main():
    pessoa1 = Pessoa('Leirisson', 26, 1.69)

    print("nome informado pelo usuario: ")
    print(pessoa1.getNome())
    print("### Trocando o nome ###")
    pessoa1.setNome("Leirisson souza dos santos")
    print(pessoa1.getNome())
    print("testando o erro: ")
    pessoa1.setNome("bi")


if __name__ == "__main__":
    main()