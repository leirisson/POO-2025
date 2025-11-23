import { Produto } from "../interfaces/produto";


export class RelatorioVendas {
    private vendas: Array<Produto>
    constructor(vendas: Array<Produto>) {
        this.vendas = vendas
    }

    gerarRelatorio() {
        console.log('Total de vendas | ' + this.totalVendas())
        console.log('Ticket médio por venda | ', this.TicketMediovenda())
        console.log("Total de vendas de livros | " + this.ValorMedioVendaPorcategoria("livros"))


    }

    private totalVendas(): number {
        let valorInicial = 0
        const somaTodasAsVendas =
            this.vendas.reduce((acumulador = 0, itemAtual) => {
                return acumulador += itemAtual.valor
            }, valorInicial)
        return Number(somaTodasAsVendas.toFixed(2)) // retornando o valor com apenas duas casas decimais
    }

    private TicketMediovenda(): number {
        const numeroVendas = this.vendas.length
        const ticketMedio = this.totalVendas() / numeroVendas
        return Number(ticketMedio.toFixed(2))
    }

    private ValorMedioVendaPorcategoria(categoria: string): number {
        const valorInicial = 0
        const vendasPorCategoria = this.vendas
            .filter(v => v.categoria === categoria)
            .reduce((acumulador, itemAtual) => acumulador + itemAtual.valor, valorInicial)
        return Number(vendasPorCategoria.toFixed(2))
    }


    // Ticket médio por forma de pagamento

    // Produto com maior lucro absoluto


}