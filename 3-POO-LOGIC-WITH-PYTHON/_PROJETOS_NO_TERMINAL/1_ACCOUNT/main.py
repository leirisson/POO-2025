from repository.account_repository import AccountRepository
from use_case.create_account_usecase import CreateAccountUseCase
from use_case.withdraw_usecase import WithdrawUseCase
from service.account_service import AccountService
from controllers.account_controller import Accountcontroller
from exceptions.business_exception import BusinessException




def main():
    # 🔧 Infraestrutura
    repository = AccountRepository()
    
    # 🎯 Casos de uso
    create_use_case = CreateAccountUseCase(repository)
    withdraw_use_case = WithdrawUseCase(repository)
    
    # 🧩 Service
    service = AccountService(create_use_case, withdraw_use_case, repository)
    
    # 🎮 Controller
    controller = Accountcontroller(service)
    
    opcoes_menu = [
        '=== MENU ===', 
        "1️⃣  ➡️   CRIAR CONTA", 
        "2️⃣  ➡️   SACAR", 
        "3️⃣  ➡️   LISTAR CONTAS",
        "4️⃣  ➡️   EXCLUIR CONTA",
        "5️⃣  ➡️   SAIR"
        ]
    
    
    while True:
        for opcao in opcoes_menu:
            print(opcao)
        opcao_escolhida = input("Escolha: ")
        try:
            match(opcao_escolhida):
                case "1":
                    controller.create_account()
                case "2":
                    controller.withdraw()
                case "3":
                    for conta in controller.list_accounts():
                        print(f"Nº Conta: {conta.number} | Titular: {conta.owner} | Saldo: {conta.get_balance()}")
                case "4":
                    number = input("número da conta: ")
                    controller.delete_account(number)
                    print("conta removida com sucesso.")
                case "5":
                    break
                case _:
                    print("opção invalida.")
                    continue
                
        except BusinessException as e:
            print(f"🔴 Erro: {e}")


if __name__ == "__main__":
    main()