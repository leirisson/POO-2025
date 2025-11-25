import { User } from './interfaces/User'


export class Auth {
    private email: string
    private password: string

    constructor(user: User) {
        this.email = user.email
        this.password = user.password.toLocaleUpperCase()
    }

    getEmail() {
        return this.email
    }

    private setEmail(novoEmail: string) {
        if (!novoEmail.includes('@') || !novoEmail.includes('.')) {
            throw new Error("Informe um email valido, exemplo: jhon@example.com")
        }

        this.email = novoEmail
    }

    getPassword() {
        return this.password
    }

    private setPassword(password: string) {
        if (password.toLocaleUpperCase() != this.password) {
            throw new Error("Deve fornecer a senha correta, para poder alterar a senha.")
        }

        this.password = password.toUpperCase()
    }



    public alterarEmail(novoEmail: string) {
        if (!novoEmail.includes('@') || !novoEmail.includes('.')) {
            throw new Error("Informe um email valido, exemplo: jhon@example.com")
        }

        this.setEmail(novoEmail)
    }

    public alterarSenha(password: string, newPassword: string) {
        if (password.toLocaleUpperCase() != this.password) {
            throw new Error("Deve fornecer a senha correta, para poder alterar a senha.")
        }

        this.setPassword(newPassword.toUpperCase())
    }

    public autenticar(email: string, password: string) {
        setTimeout(() => { console.log("autenticando ...") }, 1000)
        if (this.email === email && this.password === password.toUpperCase()) {
            setTimeout(() => {
                console.log("Logago com sucesso no sistema.")
            }, 1000)
        }
        else {
            console.log("Email ou Senha incorreto.")
        }
    }

}