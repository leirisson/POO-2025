🧩 Exercício 3 — Calculadora de Juros Simples
Contexto do cliente:

"Sou corretor. Preciso simular finanças para clientes. 
Crie uma classe Emprestimo que receba: 
-> valor (number), 
-> taxa mensal (%, ex: 2.5), 
-> meses (int)
Nunca permita valores negativos nem taxa > 100%. 
O cálculo de juros (J = C × i × t) deve estar escondido — 
o cliente só chama calcularMontante() e recebe o total a pagar." 

Objetivos de lógica:

Validação de domínio (valores ≥ 0, taxa ≤ 100).
Cálculo de juros simples.
Isolamento da fórmula (mudanças futuras não quebram API).
Conceitos OO exigidos:
✅ Encapsulamento (atributos protegidos)
✅ Abstração (usuário não vê #calcularJuros())

