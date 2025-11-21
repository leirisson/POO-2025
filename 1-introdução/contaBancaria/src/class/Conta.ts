


export class Conta {
    private saldo = 0

    depositar(valor: number) {
        this.saldo += valor
    }

    getSaldo() {
        return this.saldo
    }
}