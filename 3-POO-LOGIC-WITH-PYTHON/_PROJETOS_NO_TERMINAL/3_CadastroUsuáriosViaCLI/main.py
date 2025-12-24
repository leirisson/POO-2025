from repository.user_repository import UserRepository
from services.email_service import EmailService
from use_cases.create_user import CreateUseCase
from controllers.user_controller import UserController

def main():
    repository = UserRepository()
    emailService = EmailService()
    create_user_use_case = CreateUseCase(repository, emailService)
    controller = UserController(create_user_use_case)
    
    
    while True:
        print("\n=== CADASTRO DE USUÁRIOS ===")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("0 - Sair")

        option = input("Escolha: ")

        if option == "1":
            name = input("Nome: ")
            email = input("Email: ")
            controller.create_user(name, email)

        elif option == "2":
            for user in repository.list_all():
                print(user)

        elif option == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida")
    


if __name__ == "__main__":
    main()