from classes.Conta_bancaria import Conta_Bancaria

def main():
    nome_titular_conta = input("Qual o nome do usuario da conta ?: ")
    saldo_inicial_conta = float(input("Saldo incial para a conta: "))
    
    conta = Conta_Bancaria(nome_titular_conta, saldo_inicial_conta)
    
    print("informações da conta bancaria")
    print("Saldo inicial: ", conta.get_saldo())
    valor_deposito = float(input("informe o valor do deposito:> "))
    conta.depositar(valor_deposito)
    print("informações da conta bancaria")
    print("Saldo inicial: ", conta.get_saldo())
    valor_saque = float(input("Qual o valor do saque:> "))
    conta.sacar(valor_saque)
    print("informações da conta bancaria")
    print("Saldo inicial: ", conta.get_saldo())

if __name__ == "__main__":
    main()