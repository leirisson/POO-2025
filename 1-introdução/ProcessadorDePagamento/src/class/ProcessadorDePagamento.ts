

export class ProcessadorDePagamento {
    // Método abstrato (simplificado): o usuário só precisa saber que "paga"
    pagar(valor: number, metodo: string) {
        if (metodo === "cartao") {
            this.processarPagamentoCartao(valor)
        } else if (metodo === "pix") {
            this.processarPagamentoPix(valor)
        }
    }

    private processarPagamentoCartao(valor: number) {
        console.log(`[CARTÃO] Validando... cobrando R$${valor}...`)
        this.mensagemConfirmacao()
    }

    private processarPagamentoPix(valor: number) {
        console.log(`[PIX] Validando... cobrando R$${valor}...`)
        this.mensagemConfirmacao()
    }

    mensagemConfirmacao() {
        setTimeout(() => {
            console.log(`transação confirmada. `)
        }, 1000)

    }

}