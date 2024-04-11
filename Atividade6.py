class Pessoa:
    def __init__ (self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def registro(self):
        return f'O cidadão {self.nome} possui {self.idade} anos e tem {self.altura} m de altura.'
    
    def cumprimento(self):
        return f'Olá, {self.nome}! Estou cumprimentando você!'
    
if __name__ == '__main__':
    pessoa1 = Pessoa('Josivaldo',14, 1.88)
    print(pessoa1.registro())
    print(pessoa1.cumprimento())