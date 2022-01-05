'''print('Fatorial')
n = int(input('Digite um número: '))
fatorial = 1
contador = 1
while contador <= n:
    fatorial *= contador
    contador += 1
print(f'Fatorial do número {n}! é {fatorial}')
'''

#Correção Guanabara

#Correção Mais SIMPLES
from math import factorial
n = int(input('Digite um número para calcular o seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')

#Correção mais complexa sem o Import
# n = int(input('Digite um número para calcular o seu Fatorial: '))
# contador = n
# f = 1
# print(f'Calculando {n}! = ', end='')
# while contador > 0:
#     print(f'{contador}', end='')
#     print(' x ' if contador > 1 else ' = ', end='')
#     f *= contador
#     contador -= 1
# print(f'{f}')
