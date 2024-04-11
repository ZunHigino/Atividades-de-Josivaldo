class Carro:
    def __init__ (self,marca,modelo,ano,cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        return f'O carro da marca {self.marca} está ligado.'

    def acelerar(self):
        return f'Acelerar o {self.marca}.'
    
    def desligar(self):
        return f'O {self.marca} está desligado.'
    
if __name__ == '__main__':
    carro1 = Carro('Chevrollet','Hb20','2007','Azul')
    carro2 = Carro('Volks','Hb8','2999','Rosa')

    print(carro1.ligar())
    print(carro2.desligar())
    print(carro1.acelerar())

