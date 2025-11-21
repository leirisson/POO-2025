import { ContaBancaria } from "./class/ContaBancaria";

const contaBancaria = new ContaBancaria("Leirisson", 100)

console.log("informações da conta: ")
console.log("Saldo: ",contaBancaria.getSaldo())
contaBancaria.depositar(50)
console.log("Saldo: ",contaBancaria.getSaldo())
contaBancaria.sacar(20)
console.log("Saldo: ",contaBancaria.getSaldo())
contaBancaria.sacar(100)
console.log("Saldo: ",contaBancaria.getSaldo())