import { ProcessadorDePagamento } from "./class/ProcessadorDePagamento";

const pagador = new ProcessadorDePagamento()


// pagador.pagar(99, "pix")

pagador.pagar(500, "cartao")