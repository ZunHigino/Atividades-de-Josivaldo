from banco import ContaBancaria

if __name__ == '__main__':
    conta1 = ContaBancaria('123123', 1000, 'Higino')

    print(type(conta1.saldo))
    
    rodar = True
    
    while rodar:
        ContaBancaria.menu()

        r = int(input())
    
        if r == 1:
            qnt = int(input('Quanto dinheiro deseja sacar?: '))
            conta1.sacar(qnt)
                
        elif r == 2:
            qnt = int(input('Quanto dinheiro deseja depositar?: '))
            conta1.depositar(qnt)
            
        elif r ==  3:
            ContaBancaria.saldo_atual(conta1.saldo)
            
        elif r == 0:
            rodar = False
            
    print('Obrigado pela visita!')