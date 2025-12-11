from utils.menu import menu
from utils.limpar_tela import limpar_tela
from utils.linha import linha
from utils.titulo import titulo

# classes 
from classes.Dispositivo import Dispositivo
from classes.Estrela import Estrela


def main():
    titulo_sistema = "Sistema com varias classes"
    while True:
        menu(titulo_sistema, 
            "1 - Usar a classe Dipositivo",
            "2 - Usar a classe Estrela"
            )
        op = input("Escolha uma opcao: ")
        match op:
            case "1":
                titulo_mod = "Usando a classe -> Dipositivo"
                varios_dp = []
                while True:
                    limpar_tela()
                    linha(titulo_mod,1)
                    titulo(titulo_mod)
                    linha(titulo_mod,1)
                    id_serie = input("Informe um id: ")
                    localizacao = input("Qual a localização: ")
                    dispositivo_usuario = Dispositivo(id_serie, localizacao)
                    varios_dp.append(dispositivo_usuario)
                    op = input("deseja conectar outro dipositivo: (s-sim ou n-não)")
                    if op in 'sS' or op == "Sim" or op == "SIM" or op == "sim":
                        continue
                    else:
                        titulo_v = "Dipositivos conectados"
                        limpar_tela()
                        linha(titulo_v,1)
                        titulo(titulo_v)
                        linha(titulo_v,1)
                        for dispositivo in varios_dp:
                            print(dispositivo.conexao())
                            linha(dispositivo.conexao(), 2)
                        input("Aperte em alguma tecla para continuar...")
                        break
                    
                    
            case "2":
                titulo_mod = "Usando a classe -> Estrela"
                estrelas = []
                while True:
                    limpar_tela()
                    linha(titulo_mod,1)
                    titulo(titulo_mod)
                    linha(titulo_mod,1)
                    nome = input("Qual o nome da estrela A: ")
                    massa = float(input("Qual a massa da estrela A: "))
                    
                    estrela_a = Estrela(nome, massa)
                    estrelas.append(estrela_a)
                    op = input("deseja catalogar outra estrela: (s-sim ou n-não)")
                    if op in 'sS' or op == "Sim" or op == "SIM" or op == "sim":
                        continue
                    else:
                        titulo_v = "Estrelas catalogadas"
                        limpar_tela()
                        linha(titulo_v,1)
                        titulo(titulo_v)
                        linha(titulo_v,1)
                        for estrela in estrelas:
                            print(estrela.descricao_estrela())
                            linha(estrela.descricao_estrela(),2)
                        input("Aperte em alguma tecla para continuar...")
                        break
                
            case _:
                input("opção invalida, tente novamente.")
    


if __name__ == "__main__":
    main()