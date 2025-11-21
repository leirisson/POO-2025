import { Livro } from "./class/Livro";


const livro1 = new Livro(
    "Sr. Dos Magos azul",
    "Leirison Souza",
    2005
)
const livro2 = new Livro(
    "Dom Casmurro", 
    "Machado de Assis", 
    1899);

console.log(livro1.descricao())
console.log(livro2.descricao())