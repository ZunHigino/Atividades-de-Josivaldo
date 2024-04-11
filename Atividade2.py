class Animal:
    def __init__(self,nome,idade,especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def vaca(self):
        print(f'{self.especie}: Animal Herbívoro que se alimenta de pastagens, possui cifres e é valorizada pela sua carne e leite.')
        return f'A especie {self.especie} faz Mooo'
    
    def gato(self):
        print(f'{self.especie}: Animal felino bastante conhecido, é um dos animais domésticos mais cuidado do mundo pela sua beleza e agilidade.')
        return f'A espécie {self.especie} faz Miau'
    
    def cao(self):
        print(f'{self.especie}: É conhecido pelo seu companherismo e lealdade para com o homem atavés dos séculos.')
        return f'A espécie {self.especie} faz Au Au'
    
    def peixe(self):
        print(f'{self.especie}: É um ser vivo que vive nas águas, é de fácil cuidado e bastante belo pela sua relusência aquática.')
        return f'O som que a espécie {self.especie} produz é Blu Blu'
    
if __name__ == '__main__':
    animal1 = Animal('Salomé','7 anos','Vaca')
    animal2 = Animal('Safira','3 anos','Gato')
    animal3 = Animal('Rex','5 anos','Cachorro')
    animal4 = Animal('Geraldo','6 meses','Peixe Betta')

    print(animal1.vaca())
    print(animal2.gato())
    print(animal3.cao())
    print(animal4.peixe())


