from repository.account_repository import AccountRepository
from use_cases.create_account_usecase import CreateAccountUseCase
from use_cases.withdraw_usecase import WithdrawUseCase
from services.account_service import AccountService
from controller.account_controller import AccountController
from exceptions.BussinessException import BussinessException


# injeção manual de dependencias
account_repository = AccountRepository()
# casos de uso -> ações do sistema
create_account = CreateAccountUseCase(account_repository)
withdraw_account = WithdrawUseCase(account_repository)
# service
account_service = AccountService(create_account, withdraw_account, account_repository)
#cobntroller
account_controller = AccountController(account_service)

while True:
    print("\n=== SISTEMA BANCÁRIO CLI ===")
    print("1 - Criar conta")
    print("2 - Sacar")
    print("3 - Listar contas")
    print("4 - Excluir conta")
    print("0 - Sair")

    option = input("Escolha: ")

    try:
        if option == "1":
            number = input("Número da conta: ")
            owner = input("Titular: ")
            acc_type = input("Tipo (checking/savings): ")
            account_controller.create_account(number, owner, acc_type)
            print("Conta criada com sucesso")

        elif option == "2":
            number = input("Número da conta: ")
            amount = float(input("Valor do saque: "))
            account_controller.withdraw(number, amount)
            print("Saque realizado")

        elif option == "3":
            for acc in account_controller.list_accounts():
                print(f"{acc.number} | {acc.owner} | Saldo: {acc.get_balance()}")

        elif option == "4":
            number = input("Número da conta: ")
            account_controller.delete_account(number)
            print("Conta removida")

        elif option == "0":
            break

        else:
            print("Opção inválida")

    except BussinessException as e:
        print(f"ERRO DE NEGÓCIO: {e}")
    except Exception as e:
        print(f"ERRO INESPERADO: {e}")