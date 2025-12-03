from classes.Funcionario import Funcionario


def main():
    nome = input("nome: ")
    idade = int(input("idade: "))
    
    funcaionario = Funcionario(nome, idade)
    
    print(funcaionario.exibi_info())



if __name__ == "__main__":
    main()