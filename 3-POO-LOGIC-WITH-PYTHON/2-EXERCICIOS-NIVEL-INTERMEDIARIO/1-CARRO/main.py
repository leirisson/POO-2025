# Classe Carro: Implemente uma:
# -> classe Carro com atributos privados:
# -> marca, 
# -> modelo 
# -> velocidade. 
# Adicione métodos para acelerar, frear e exibir velocidade atual.
from classes.Carro import Carro

def main():
    carro_uno = Carro("Fiat", "Uno quadrado", 80)
    print("velocidade atual:", carro_uno.velocidade_atual())
    carro_uno.acelerar()
    carro_uno.acelerar()
    carro_uno.acelerar()
    carro_uno.frear()
    carro_uno.frear()
    carro_uno.frear()
    carro_uno.frear()
    carro_uno.frear()
    carro_uno.frear()
    carro_uno.frear()
    carro_uno.frear()
    carro_uno.frear()
    carro_uno.frear()
    carro_uno.frear()
    print("velocidade atual:", carro_uno.velocidade_atual())

if __name__ == "__main__":
    main()
