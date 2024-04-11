#classe

class ContaBancaria:
    def __init__(self,numero,saldo,titular):
        self.numero = numero
        self.saldo = saldo
        self.titular = titular
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, value):
        self._saldo = value
    
    def depositar(self,quantidade):
        self._saldo += quantidade
        print(f'Foram depositados R${quantidade}')
    
    def sacar(self, quantidade):
        if self._saldo < quantidade:
            print('Conta não possui este saldo.')
        else:
            self._saldo -= quantidade
            print(f'''Você retirou R${quantidade}
                ''')
    
    def saldo_atual(saldo):
        return print(f'''Saldo Atual: R${saldo}
                     ''')
    
    def menu():
        print('''--O que deseja executar?--
1 - Sacar
2 - Depositar
3 - Ver saldo
0 - Sair''')