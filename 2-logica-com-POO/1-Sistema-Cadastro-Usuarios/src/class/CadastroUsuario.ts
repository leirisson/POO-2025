

export class Cadastrousuario {
    nome: string
    email: string
    private senha: string

    constructor(nome: string, email: string, senha: string) {
        this.nome = nome
        this.email = email
        this.senha = senha
    }

    cadastrar() {
        const aSenhaEValida = this.validaNome()
        const oEmailEValido = this.validaEmail()

        if (aSenhaEValida || oEmailEValido) {
            throw new Error("Dados invalidos, nome deve conter no minimo 2 caracter, e o email deve seguir o padrão: jhon@example.com")
        } else {
            console.log("usuario:", this.nome, " com o e-mail:", this.email, "cadastrado com sucesso.")
        }
    }

    getNome() {
        return this.nome
    }

    setNome(novoNome: string) {
        const aSenhaEValida = this.validaNome()

        if (aSenhaEValida) {
            throw new Error("Dados invalidos, nome deve conter no minimo 2 caracter.")
        }

        this.nome = novoNome
    }

    getEmail() {
        return this.email
    }
    setEmail(novoEmail: string) {
        const oEmailEValido = this.validaEmail()
        if (oEmailEValido) {
            throw new Error("O email deve seguir o padrão: jhon@example.com")
        }
        this.email = novoEmail
    }

    private validaNome(): boolean {
        return this.nome.length < 2
    }

    private validaEmail(): boolean {
        return !this.email.includes('.') || !this.email.includes('@')
    }


}