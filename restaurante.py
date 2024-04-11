class Pedidos:
    def __init__(self,itens,total,status) -> None:
        self.itens = itens
        self.total = total
        self.status = status
        
    def menu():
        print('''==========Menu==========
1 - Hamburguer    - R$15
2 - Pizza         - R$25
3 - Refrigerante  - R$8
0 - Sair          - R$0
========================
''')    
        
    def adicionar(itens, total,x, y):
        itens.append(x)
        total.append(y)
        
    def calculo_total(total):
        o = 0
        for i in total:
            i == o + i
            o = i + o
        return f'Preço total: R${o}'
    
    def status(i):
        if i == 1:
            print('Pedido em andamento.')
        elif i == 2:
            print('Pedido cancelado.')
        else:
            print('Pedido finalizado.') 