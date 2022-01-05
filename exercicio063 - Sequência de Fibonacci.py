print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
nUser = int(input('Digite um número inteiro: '))
print(f'Os {nUser} primeiros elementos de uma SEQUÊNCIA de FIBONACCI')
contador = 3
n1 = 0
n2 = 1
print(f'{n1}-> {n2}', end='')
while contador <= nUser:
        n3 = n1 + n2
        print(f'-> {n3}', end= '')
        n1 = n2
        n2 = n3
        contador +=1
print('-> FIM')