🧩Exercício 2 — Gerenciador de Tarefas Simples



`Contexto do cliente:`
"Meus funcionários esquecem de anotar prazos. 
Crie uma classe Tarefa onde eu possa definir: 
-> título (obrigatório), 
-> descrição (opcional) 
-> data de vencimento (obrigatória, no formato 'YYYY-MM-DD'). 
[ Se a data for no passado, o sistema deve automaticamente marcar como vencida ], 
mas eu não quero ter que verificar isso manualmente ao acessar o status." 

`Objetivos de lógica:`
Conversão e comparação de datas.
Lógica condicional no getter (get status() → "pendente", "vencida").
Validação no construtor.

`Conceitos OO exigidos:`
✅ Classe + Construtor com validação
✅ Encapsulamento + abstração (método interno para calcular status; usuário só acessa tarefa.status)