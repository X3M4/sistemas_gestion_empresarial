class Rectangulo:
    altura = 0.0
    base = 0.0
    
    #Constructor
    def __init__(self, base:float, altura:float):
        self.base = base
        self.altura = altura
    
    def calculaArea(self):
        print(f"El área del rectángulo es: {self.base*self.altura}")
        
    def calculaPerimetro(self):
        print(f"El perímetro del rectángulo es: {2*(self.base+self.altura)}")
        

rect = Rectangulo(5,3)
rect.calculaArea()
rect.calculaPerimetro()