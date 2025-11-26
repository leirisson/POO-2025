# Classe Aluno: 
# Crie uma classe Aluno com nome e lista de notas. 
# Implemente métodos para adicionar nota, 
# calcular média e verificar se está aprovado (média >= 7)

from classes.Aluno import Aluno
        
def main():
    nome_aluno = input("Qual o nome do aluno: ")
    aluno = Aluno(nome_aluno)

    for i in range(4):
        nota = float(input("Qual a sua nota: "))
        aluno.adicionar_nota(nota)
        
    print(aluno.verificar_status_aluno())




if __name__ == "__main__":
    main()
