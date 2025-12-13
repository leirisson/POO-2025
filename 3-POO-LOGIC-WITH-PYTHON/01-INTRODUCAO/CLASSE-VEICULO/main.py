from classes.Veiculo import Veiculo



def main():
    carroUno = Veiculo("Fiate", "Uno", "Preto")
    carroGolQuadrado = Veiculo("Wolwksvagem", "Gol Quadrado", "Branco")

    print(carroUno.descricao())
    print(carroGolQuadrado.descricao())
if __name__ == "__main__":
    main()