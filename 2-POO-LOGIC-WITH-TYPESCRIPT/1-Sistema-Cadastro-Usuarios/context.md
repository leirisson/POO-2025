🧩 Exercício 1 — Sistema de Cadastro de Usuários
Contexto do cliente:

"Preciso de um módulo para cadastrar usuários. 
O nome deve ter pelo menos 2 caracteres,
o e-mail deve ser válido (ex: user@dominio.com)
e a senha nunca pode ser exposta diretamente. 
Quero poder criar usuários e recuperar 
dados públicos (nome e e-mail), mas sem vazar a senha." 


Objetivos de lógica:

Validação de entrada (tamanho do nome, formato de e-mail).
Proteger dado sensível (senha).
Retornar apenas dados permitidos.
Conceitos OO exigidos:
✅ Classe + Objeto + Construtor
✅ Encapsulamento (senha privada + getters controlados)

💡 Dica: use expressão regular simples para validar e-mail (/.+@.+\..+/), ou apenas verifique se tem "@" e ".". 