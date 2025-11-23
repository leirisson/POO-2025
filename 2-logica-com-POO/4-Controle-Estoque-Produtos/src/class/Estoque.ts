import { TEstoque } from "../types/TEstoque"


export class Estoque {
    private nome: string
    private preco: number
    private quantidade: number
    private estoque: number

    constructor(produto: TEstoque) {
        this.nome = produto.nome
        this.preco = produto.preco
        this.quantidade = produto.quantidade
        this.estoque = produto.estoque
    }

    getNome() {
        return this.nome
    }

    setNome(novoNome: string) {
        if (this.nome.length > 3) {
            this.nome = novoNome
            console.log("nome atualizado com sucesso. ✅")
        } else {
            throw new Error("O nome do produto não pode ter menos de 3 caracteres.")
        }
    }

    getPreco() {
        return this.preco
    }

    setPreco(novoPreco: number) {
        if (novoPreco <= 0) {
            throw new Error("Não pode informar zero ou valor negativo para um produto.")
        }

        this.preco = novoPreco
        console.log("Preço do produto alterado com sucesso.")
    }

    getQuantidade() {
        return this.quantidade
    }

    setQuantidade(novaQuantidade: number) {
        if (this.quantidade <= 0) {
            throw new Error("Forneça um novo valor para quantidade que não seja 0 ou megativo.")
        }

        this.quantidade = novaQuantidade
        console.log("quantidade do produto ")
    }

    getEstoque() {
        return this.estoque
    }

    setEstoque(novaQuantidade: number) {
        this.estoque = novaQuantidade
    }

    vender(qtdItem: number) {
        if (qtdItem > this.estoque) {
            throw new Error("Você não pode vender mais produtos do que os que tem em estoque.")
        } else if (this.preco <= 0) {
            throw new Error("Reajuste o erro no valor do produto, não pode ser 0 ou negativo.")
        }

        let qtdEstoque = this.getEstoque()

        qtdEstoque -= qtdItem
        this.setEstoque(qtdEstoque)

        console.log(`venda de ${qtdItem}, ${this.nome} realizada com sucesso.`)
    }

    reporEstoque(qtdItem: number) {
        if (qtdItem <= 0) {
            throw new Error("não pode repor o estoque com quantidade de produtos zerados ou negativos")
        }

        let qtdEstoque = this.getEstoque()
        qtdEstoque += qtdItem

        this.setEstoque(qtdEstoque)
        console.log(`Estoque do produto reposto com sucesso.`)

    }

    relatorioEstoque() {
        console.log("###########################################")
        console.log("########## RELATORIO DO ESTOQUE ###########")
        console.log(`PRODUTO| NOME: ${this.nome} | PREÇO: ${this.preco} | QUANTIDADE: ${this.quantidade} | ESTOQUE: ${this.estoque}`)
        console.log("###########################################")
    }

}