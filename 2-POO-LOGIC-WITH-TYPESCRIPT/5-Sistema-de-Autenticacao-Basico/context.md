🧩 Exercício 5 — Sistema de Autenticação Básico

Contexto do cliente:
"Preciso simular login. Um UsuarioAutenticavel tem e-mail e senha. 
Não quero guardar senhas em texto claro — salve o hash (use senha.toUpperCase() como simulação de hash). 
O método autenticar(senhaFornecida) deve comparar o 
hash da senha fornecida com o armazenado e retornar true/false. 
Ninguém deve acessar o hash diretamente." 

Objetivos de lógica:

Simulação de hash (transformação determinística).
Comparação segura.
Isolamento do dado sensível.
Conceitos OO exigidos:
✅ Encapsulamento (hash privado)
✅ Abstração (usuário só chama .autenticar())

💡 Você já trabalha com tokens e persistência — esse é um passo prévio para entender segurança em camadas.
