'''
n = 0
tres = 'O valor 3 não foi digitado em nenhuma posição'
par = ''
n0 = int(input('Digite o 1º número: '))
n1 = int(input('Digite o 2º número: '))
n2 = int(input('Digite o 3º número: '))
n3 = int(input('Digite o 4º número: '))
tupla = (n0, n1, n2, n3)

contador = 0
for n in tupla:
    if n == 3:
        tres = f'O valor 3 apareceu na {contador+1}ª posição'
    if n % 2 == 0:
        par = par + ' ' + str(n)
    contador += 1

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
print(tres)
print(f'Os valores pares digitados foram {par} pares')
'''

#Correção Guanabara
num = (int(input('Digite o 1º número: ')),
     int(input('Digite o 1º número: ')),
     int(input('Digite o 1º número: ')),
     int(input('Digite o 1º número: ')))
print(f'Você digitou os valores {num}.')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

