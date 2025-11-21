import { Conta } from "./class/Conta";


// primeiro deposito 
const minhaConta  = new Conta()
minhaConta.depositar(100)
console.log("==========================")
console.log("Saldo: ", minhaConta.getSaldo())
console.log("==========================")

// segundo deposito
minhaConta.depositar(300)
console.log("==========================")
console.log("Saldo: ", minhaConta.getSaldo())
console.log("==========================")