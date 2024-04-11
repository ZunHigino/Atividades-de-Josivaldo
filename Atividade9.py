class Aluno:
    def __init__ (self,nome,idade,notas=0.0):

        self.nome = nome
        self.idade = idade
        self.notas = notas

    def medias(self):
        media = sum(self.notas) / len(self.notas)
        return media
    
    def verificador(self):
        resul = self.medias()
        if resul < 7.0:
            return f'Aluno Reprovado. Média {resul()}'
        else:
            return f'O aluno {self.nome}, de {self.idade}, teve uma média de {resul} pontos!'

if __name__ == '__main__':
    notas_aluno = [10,10,9.9,10]
    aluno1 = Aluno('Heitor','16 anos', notas_aluno)
    print(aluno1.verificador())