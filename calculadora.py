class Calcu:
    def menu():
        print('''====Cálculos====
1 - Soma
2 - Subtração
3 - Multiplicar
4 - Divisão
0 - Sair''')
    
    def soma():
        x = int(input('1º número: '))
        y = int(input('2º número: '))
        return print(f'Resultado: {x + y}')
    
    def sub():
        x = int(input('1º número: '))
        y = int(input('2º número: '))
        return print(f'Resultado: {x - y}')
    
    def multi():
        x = int(input('1º número: '))
        y = int(input('2º número: '))
        return print(f'Resultado: {x * y}')
    
    def div():
        x = int(input('1º número: '))
        y = int(input('2º número: '))
        return print(f'Resultado: {x / y}')