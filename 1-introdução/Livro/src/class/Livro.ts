

export class Livro {
    titulo: string
    autor: string
    anoPublicacao: number

    constructor(titulo: string, autor: string, anoPublicacao: number) {
        this.titulo = titulo
        this.autor = autor
        this.anoPublicacao = anoPublicacao
    }

    descricao(){
        return `Livro: ${this.titulo}, por ${this.autor} ano ${this.anoPublicacao}`
    }
}