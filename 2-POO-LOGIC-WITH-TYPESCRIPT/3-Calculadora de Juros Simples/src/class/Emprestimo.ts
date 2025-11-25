import { TEmprestimos } from "../types/TEmprestimos"



export class Emprestimo {
    private valor: number
    private taxaMensal: number
    private meses: number

    constructor(emprestimo: TEmprestimos) {
        this.valor = emprestimo.valor
        this.taxaMensal = (emprestimo.taxaMensal / 100)
        this.meses = emprestimo.meses
    }


    calcularMontanteJurosSimples(): number{
        if(this.valor < 0 || this.taxaMensal > 100){
            throw new Error("Não pode realizar um emprestimo comvalor negativo, ou ter uma taxa de emprestimo maior que 100%.")
        }
        const montante: number = this.calcularJurossimples(this.valor, this.taxaMensal, this.meses)
        return montante
    }

    private calcularJurossimples(capitalInicial:number, taxaCobrada:number, tempoPagamento: number): number{
        // return exemplo => 2000 × 0.03 × 5 
        return capitalInicial * taxaCobrada * tempoPagamento
    }
}