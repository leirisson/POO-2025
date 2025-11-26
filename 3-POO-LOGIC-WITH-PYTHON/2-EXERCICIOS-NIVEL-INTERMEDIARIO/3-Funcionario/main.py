# Classe Funcionário: 
# ================================
# Faça uma classe Funcionario com nome, salário e cargo. 
# Adicione métodos para dar aumento percentual e calcular salário anual.

from classes.Funcionario import Funcionario


def main():
    nome = str(input("Qual o nome: "))
    cargo = str(input("qual o cargo: "))
    salario = float(input("Qual o salario: "))
    
    funcionario = Funcionario(nome, cargo, salario)
    salario_anual = funcionario.calcular_salario_anual()
    print('antigo salario anual: ', salario_anual)
    # almento de 5% no salario
    funcionario.almento_percentual(5)
    salario_anual = funcionario.calcular_salario_anual()   
    print('novo salario anual: ', salario_anual)

if __name__ == "__main__":
    main()