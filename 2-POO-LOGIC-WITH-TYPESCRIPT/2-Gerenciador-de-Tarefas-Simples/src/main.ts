import { Tarefa } from "./class/Tarefa";
import { TTarefa } from "./types/TTarefa";

const t: TTarefa = {
    titulo : "comprar pão",
    descricao: "acordar de manhã para comprar pão.",
    dataVencimento: new Date("2025-11-10")
    
}
const tarefa1 = new Tarefa(t)

console.log("################################################")
// regatando a tarefa como todo
console.log("RESGATANDO A TAREFA ORIGINAL: ")
console.log(tarefa1.getTarefa())
console.log()
console.log("################################################")
// resgatando o titulo da tarefa e editando o titulo da tarefa editada
console.log("RESGATANDO E EDITANDO O TITULO: ")
console.log(tarefa1.getTitulo())
tarefa1.setTitulo("rer")
console.log("novo titulo: ",tarefa1.getTitulo())
console.log()
console.log("################################################")

// resgatando a descrição e editando a descricao
console.log("RESGATANDO E EDITANDO A DESCRIÇÃO: ")
console.log(tarefa1.getDescricao())
tarefa1.setDescricao("Comprar pão, manteiga, e café")
console.log("nova descrição: ",tarefa1.getDescricao())
console.log()
console.log("################################################")
console.log("RESGATANDO E EDITANDO A DATA DA TAREFA:")
console.log("Data da tarefa: ",tarefa1.getData())
tarefa1.setData(new Date("2025-11-29"))
console.log()
console.log("################################################")
console.log("TAREFA FINAL: ")
console.log(tarefa1.getTarefa())