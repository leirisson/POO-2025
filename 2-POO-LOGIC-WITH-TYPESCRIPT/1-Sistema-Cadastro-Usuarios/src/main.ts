import { Cadastrousuario } from "./class/CadastroUsuario";


const cadastro = new Cadastrousuario(
    "Leirisson",
    "leirison@example.com",
    "123456"
)

cadastro.cadastrar()
console.log("Email: ", cadastro.getEmail())
console.log("Nome: ", cadastro.getNome())