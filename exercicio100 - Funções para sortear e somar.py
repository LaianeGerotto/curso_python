# from random import randint
# from time import sleep
#
# def lista():
#     lista = []
#     print('Sorteando 5 valores da lista:', end=' ')
#     for contador in range(0,5):
#         num = (randint(1,10))
#         lista.append(num)
#         print(num, end=' ')
#         sleep(0.5)
#     print('PRONTO!')
#     print(f'Somando os valores pares de {lista}, temos', end=' ')
#     pares(lista)
#
#
# def pares(lista):
#     soma = 0
#     for num in lista:
#         if num % 2 == 0:
#             soma += num
#     print(soma)
#
# lista()

#CORREÇÃO GUANABARA
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)

