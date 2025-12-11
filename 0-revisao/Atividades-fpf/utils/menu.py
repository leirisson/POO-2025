from utils.titulo import titulo
from utils.linha import linha
from utils.limpar_tela import limpar_tela



def menu(titulo_menu:str, *opcoes_menu) -> None:
    limpar_tela()
    linha(titulo_menu,1)
    titulo(titulo_menu)
    linha(titulo_menu,1)
    
    for opcao in opcoes_menu:
        print(opcao)
        linha(opcao,2)