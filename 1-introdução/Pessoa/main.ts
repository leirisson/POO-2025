
import { Pessoa } from "./Pessoa";

// instanciando  a classe Pessoa
const umaPessoa = new Pessoa("Leirisson")
console.log(`Nome: ${umaPessoa.getName()}`)
console.log("Trocando o nome")
umaPessoa.setNome("Lucas Silva")
console.log(`Nome: ${umaPessoa.getName()}`) 