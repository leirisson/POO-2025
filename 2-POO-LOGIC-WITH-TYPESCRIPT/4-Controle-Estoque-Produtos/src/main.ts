import { Estoque } from "./class/Estoque";
import { TEstoque } from "./types/TEstoque";

const protduto: TEstoque = {
    nome: "Computador de mesa",
    preco: 1500,
    quantidade: 1000,
    estoque: 2500
}

const estoque = new Estoque(protduto)

estoque.relatorioEstoque()

// realizando uma venda 
estoque.vender(2200)
estoque.relatorioEstoque()
estoque.reporEstoque(120)
estoque.relatorioEstoque()
