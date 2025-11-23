🧩 Exercício 6 — Gerador de Relatórios de Vendas
Contexto do cliente:

"Quero gerar relatórios diários. Crie uma classe RelatorioVendas que receba uma lista de vendas:
[ { valor: 100, categoria: 'eletrônicos' }, ... ]. 
O cliente só deve chamar gerarRelatorio() e receber um objeto como:
{ total: 500, media: 100, categorias: { 'eletrônicos': 2 } }
A lógica de contagem, soma e agrupamento deve estar escondida." 

Objetivos de lógica:

Processamento de array (reduce, map, filter).
Agrupamento por chave (categoria).
Cálculo de estatísticas (soma, média).
Conceitos OO exigidos:
✅ Abstração (complexidade interna oculta)
✅ Classe com estado (vendas recebidas no construtor)