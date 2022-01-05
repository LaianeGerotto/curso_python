# OPÇÃO 1 - É a mais recomendada
from uteis import numeros


num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O Dobro de {num} é {numeros.dobro(num)}.')
print(f'O Triplo de {num} é {numeros.triplo(num)}.')


# OPÇÃO 2 - não é tão recomendada devido as outras importações padrões, se tiver funções repetidas, o programa usa a ultima importação.
# from funções import fatorial, dobro, triplo
#
# num = int(input('Digite um valor: '))
# fat = fatorial(num)
# print(f'O fatorial de {num} é {fat}.')
# print(f'O Dobro de {num} é {dobro(num)}.')
# print(f'O Triplo de {num} é {triplo(num)}.')