export class PessoaApresenta {
    nome: string
    idade: number

    constructor(nome: string, idade: number) {
        this.nome = nome
        this.idade = idade
    }

    aprsentar(){
        return `Olá, meu nome é ${this.nome} e tnho ${this.idade} anos.`
    }
}