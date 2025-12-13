from classes.Usuario import Usuario

def main():
    nome = input("Usuario: ")
    senha = input("Senha: ")
    
    usuario = Usuario(nome, senha)
    print("logado, com sucesso")
    print("=== Trocar a senha ===")
    senha_antiga = input("senha antiga: ")
    nova_senha = input("nova senha: ")
    print(usuario.alterar_senha(senha_antiga, nova_senha))

if __name__ == "__main__":
    main()