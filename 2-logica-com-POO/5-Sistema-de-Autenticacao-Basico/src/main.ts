import { Auth } from "./Auth"
import { User } from "./interfaces/User"


const user: User = {
    email: "leirisson.souza@exemple.com",
    password: "password"
}


const login = new Auth(user)

console.log(login.getEmail())
console.log(login.getPassword())
login.alterarEmail("leirisson.souza@exemple.com")
console.log(login.getEmail())
login.autenticar(user.email, user.password)