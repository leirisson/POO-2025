

class Circulo:
    def __init__(self, raio:float):
        self._pi = 3.14
        self._raio = raio
        
    def calcular_circunferencia(self) :
        circunferencia = 2 * self._pi * self._raio
        return circunferencia
    
    def calcular_area_circulo(self) :
        area_circulo = self._pi * (self._raio * self._raio)
        return area_circulo
    
