🎯 OBJETIVO DO EXEMPLO

Criar um mini sistema bancário no terminal para provar que:

A entrada de dados (terminal, API, formulário) é só um detalhe


TERMINAL (input)
   ↓
CONTROLLER
   ↓
USE CASE
   ↓
DOMÍNIO (POO)
   ↓
REPOSITORY (memória)



📁 ESTRUTURA DO PROJETO (CLI)
app/
├── main.py
├── controllers/
│   └── account_controller.py
├── use_cases/
│   ├── create_account_usecase.py
│   └── withdraw_usecase.py
├── repositories/
│   └── account_repository.py
├── domain/
│   ├── account.py
│   ├── checking_account.py
│   └── savings_account.py
└── exceptions/
    └── business_exception.py
