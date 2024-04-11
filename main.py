#Chamando arquivo restaurante

from restaurante import Pedidos

#Atividade 10

if __name__ == '__main__':
    L_itens = []
    L_total = []
    pedindo = True
    status = 1
    
    while pedindo:
        Pedidos.menu()
        
        pedido = int(input())
        match pedido:
            case 1:
                item = 'Hamburguer'
                total = 15
                Pedidos.adicionar(L_itens, L_total, item,total)
            case 2:
                item = 'Pizza'
                total = 25
                Pedidos.adicionar(L_itens, L_total, item,total)
            case 3:
                item = 'Refrigerante'
                total = 8
                Pedidos.adicionar(L_itens, L_total, item,total) 
            case 0:
                pedindo = False
            case _:
                print('Pedido não identificado.')
        
        Pedidos.status(status)
        
    print(f'''Itens pedidos: {L_itens}
Valor dos Itens: {L_total}''')
    print(Pedidos.calculo_total(L_total))
        
    res = int(input('Comfirmar pedido? (1/0) '))
    
    if res == 1:
        print('Pagamento feito.')
        status = 0
        Pedidos.status(status)
    elif res == 0:
        status = 2
        Pedidos.status(status)