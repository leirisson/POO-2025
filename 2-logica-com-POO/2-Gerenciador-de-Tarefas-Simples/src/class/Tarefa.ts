import { TTarefa } from "../types/TTarefa"
export class Tarefa {
    private titulo: string
    private descricao: string
    private status: string
    private dataVencimento: Date

    constructor(tarefa: TTarefa) {
        this.titulo = tarefa.titulo,
        this.descricao = tarefa.descricao,
        this.dataVencimento = tarefa.dataVencimento
        this.status = "pendente"
    }
    getTarefa() {
        const status = this.calcularStatus()
        const tarefa = {
            titulo: this.titulo,
            descricao: this.descricao,
            status,
            data_vencimento: this.dataVencimento
        }
        return tarefa
    }
    getTitulo() {
        return this.titulo
    }

    setTitulo(novoTitulo: string) {
        novoTitulo = this.validarTitulo(novoTitulo)
        this.titulo = novoTitulo
    }

    getDescricao() {
        return this.descricao
    }

    setDescricao(novaDescricao: string) {
        novaDescricao = this.validarDescricao(novaDescricao)
        this.descricao = novaDescricao
    }

    getData(){
        return this.dataVencimento
    }
    setData(novaData: Date){
        this.dataVencimento = novaData
    }


    private calcularStatus() {
        const dataAtual = new Date()
        if (dataAtual > this.dataVencimento) {
            const status: string = this.status = "Vencida"
            return status
        } else {
            const status: string  = this.status = "Pendente"
            return status

        }
    }

    private validarTitulo(titulo: string) {
        if (titulo.length > 2) {
            return titulo
        }

        throw new Error("Erro, esse titulo de ter pelo menos 3 caracter")

    }

    private validarDescricao(descricao: string) {
        if (descricao.length >= 10) return descricao 
        throw new Error("A sua nova descrição deve conter no minimo 10 caracter.")
    }


}


