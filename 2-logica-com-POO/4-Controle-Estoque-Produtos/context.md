🧩 Exercício 4 — Controle de Estoque de Produtos
Contexto do cliente:

"Minha loja tem produtos com:
-> nome, 
-> preço 
-> quantidade 
-> estoque. 
Não posso vender mais do que tenho, e o preço nunca pode ser negativo ou zero. Preciso de métodos:
-> vender(qtd)
-> repor(qtd) 
Se tentarem vender além do estoque, devo lançar um erro claro, mas o sistema não deve permitir acesso direto ao estoque — ex: produto.estoque = -10 deve ser impossível."

Objetivos de lógica:

Mutação controlada do estado (estoque).
Validação em operações (venda / reposição).
Garantir consistência.
Conceitos OO exigidos:
✅ Encapsulamento rigoroso (estoque privado)
✅ Getter público para consulta, mas sem setter direto
