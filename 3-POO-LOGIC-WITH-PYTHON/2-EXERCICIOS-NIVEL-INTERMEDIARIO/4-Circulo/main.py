# Classe Círculo: Implemente uma classe Circulo com raio. 
# Adicione métodos para calcular área, 


from classes.Circulo import Circulo


def main():
    c = Circulo(5.0)
    area = c.calcular_area_circulo()
    circunferencia = c.calcular_circunferencia()
    print(f"Area do circulo: {area:.2f}")
    print(f"circunferência do circulo: {circunferencia:.2f}")

if __name__ == "__main__":
    main()