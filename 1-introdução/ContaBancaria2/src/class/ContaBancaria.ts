

export class ContaBancaria {
    private saldo: number
    public titular: string

    constructor(titular: string, saldoInicial=0){
        this.titular = titular
        this.saldo = saldoInicial
    }

    //metodo publico para consultar o saldo
    getSaldo(){
        return this.saldo
    }

    // metodo publico para depositar
    depositar(valor: number){
        if(valor > 0){
            this.saldo += valor
            console.log(`Depósito de R$${valor} realizado.`)
        } else {
            throw new Error("Valor de depósito invalido.")
        }
    }

    // metodo publico para sacar
    sacar(valor:number){
        if(valor > 0 && valor <= this.saldo){
            this.saldo -= valor
            console.log(`Saque de R$${valor} Realizado.`)
        } else {
            throw new Error("Saldo insuficiente ou inválido.")
        }
    }


}