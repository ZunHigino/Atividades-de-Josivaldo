#Puxando classe do arquivo banco

from formas import Triangulo

#atividade 5

if __name__ == '__main__':
    triangulo_equi = Triangulo(10,10,10)
    triangulo = Triangulo(3,4,5)
    
    print('Triângulo 1')
    Triangulo.calculo_area(triangulo_equi.ladobase, triangulo_equi.ladoAltura)
    Triangulo.calculo_perimetro(triangulo_equi.lado1, triangulo_equi.ladoAltura, triangulo_equi.ladobase)
    print('Triângulo 2')
    Triangulo.calculo_area(triangulo.ladoAltura, triangulo.ladobase)
    Triangulo.calculo_perimetro(triangulo.lado1, triangulo.ladoAltura, triangulo.ladobase)