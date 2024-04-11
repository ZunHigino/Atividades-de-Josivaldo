class Pessoa:
    def __init__(self,nome, sexo, cpf) -> None:
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        
    def __str__(self) -> str:
        return f'''{self.nome}, {self.sexo}, {self.cpf}
'''
    