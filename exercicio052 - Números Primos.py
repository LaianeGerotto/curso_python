"""
print('Verificador de número Primo')
n = int(input('Digite um número: '))
contador2 = 0
for contador in range(2, n-1):
    if n % contador == 0:
        contador2 += 1
if n == 1:
    print('Não é primo!')
elif contador2 == 0:
    print("Número Primo!")
else:
    print('Não é Primo!')

"""
'''Resolução GUANABARA'''
n = int(input('Digite um número: '))
total = 0
for contador in range(1, n + 1):
    if n % contador == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{contador}', end=' ')
print(f'\n\033[mO número {n} foi divisível {total} vezes.')
if total == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele NÃO é Primo!')
