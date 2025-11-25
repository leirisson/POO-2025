import { Emprestimo } from "./class/Emprestimo";
import { TEmprestimos } from "./types/TEmprestimos";


const datEMprestimo: TEmprestimos = {
    valor: 1000,
    taxaMensal: 30, // de 0 há 100
    meses: 12
}
const emp1 = new Emprestimo(datEMprestimo)
console.log(emp1.calcularMontanteJurosSimples())
