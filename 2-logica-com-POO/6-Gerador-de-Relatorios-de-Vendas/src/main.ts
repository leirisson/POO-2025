import { RelatorioVendas } from "./class/RelatorioVendas";
import { vendas } from './data/vendas'

const reports = new RelatorioVendas(vendas)


reports.gerarRelatorio()