export interface Produto {
  nome: string;
  descricao: string;
  quantidade: number;
  valor: number;       
  valorCusto: number;  
  total: number;     
  categoria: string;
  formaPagamento: 'pix' | 'cartao_credito' | 'cartao_debito' | 'dinheiro' | 'boleto';
  data: string;        // 'YYYY-MM-DD'
}