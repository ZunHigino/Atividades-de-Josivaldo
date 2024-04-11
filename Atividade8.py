class Retangulo:
    def __init__ (self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (self.base * 2) + (self.altura * 2)
    
if __name__ == '__main__':
    retangulo1 = Retangulo(6,7)
    retangulo2 = Retangulo(7,9)

    print(f'O primeiro retangulo possui a área de {retangulo1.area()} metros.')
    print(f'O segundo retangulo possui a área de {retangulo2.area()} metros.')
    print(f'O primeiro retangulo possui o perimetro de {retangulo1.perimetro()} metros.')
    print(f'O segundo retangulo possui o perimetro de {retangulo2.perimetro()} metros.')