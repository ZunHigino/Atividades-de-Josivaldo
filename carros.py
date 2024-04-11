class Carro:
    def __init__(self,marca,cor,modelo,ano) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        
    def __str__(self) -> str:
        return f'''Marca: {self.marca} 
Modelo: {self.modelo} 
Cor: {self.cor} 
Ano: {self.ano}
'''
    def ligar(carro):
        return print(f'O seu {carro} ligou.')
    
    def desligar(carro):
        return print(f'O seu {carro} desligou!')
    
    def acelerar(carro):
        return print(f'O seu {carro} está acelerando.')
    
    def freiar(carro):
        return print(f'O seu {carro} freiou.')