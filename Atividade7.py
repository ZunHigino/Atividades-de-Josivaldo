class Livro:
    def __init__ (self,titulo,autor,numero):
        self.titulo = titulo
        self.autor = autor
        self.numero = numero

    def info (self):
        return f'Livro {self.titulo}, escrito por {self.autor}, o número das suas páginas são {self.numero}p.'
    
    def calcular (self):
        calcular_pala = 50000 / self.numero
        return f'O seu livro possui cerca de 50.000 palavras, {calcular_pala :.0f} em cada página.'
    
if __name__ == '__main__':
    livro1 = Livro('O Regresso do Peregrino', 'C.S Lewis', 325)
    print(livro1.info())
    print(livro1.calcular())