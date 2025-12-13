from classes.Conta_bancaria import Conta_bancaria

def main():
    conta_corrente = Conta_bancaria()
    saldoInicial =  conta_corrente.getSaldo()
    
    print("Saldo inicial: ",saldoInicial)
    conta_corrente.depositar(150)
    saldoatual =  conta_corrente.getSaldo()
    print("Saldo atual: ",saldoatual)
    print("sacando dinheiro: ")
    conta_corrente.sacar(160)
    saldoatual =  conta_corrente.getSaldo()
    print("Saldo atual: ",saldoatual)
    

if __name__ == "__main__":
    main()