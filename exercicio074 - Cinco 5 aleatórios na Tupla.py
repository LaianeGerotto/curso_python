from random import randint
'''
#OPÇÃO 1 #Guanabra também usou essa resolução
lista =(
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10)
)
print(f'Os valores sorteados foram: {lista}')
print(f'O maior valor sorteado foi: {max(lista)}')
print(f'O maior valor sorteado foi: {min(lista)}')
'''
'''
#OPÇÃO 2
gerador0 = randint(0,10)
gerador1 = randint(0,10)
gerador2 = randint(0,10)
gerador3 = randint(0,10)
gerador4 = randint(0,10)
lista = (gerador0,gerador1, gerador2, gerador3,gerador4)
print(lista)
print(max(lista))
print(min(lista))
'''

#OPÇÃO 3
maior = 0
menor = 10
lista =(
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10)
)
print('Os valores sorteados foram:', end=" " )
for numero in lista:
    print(f'{numero}', end="  ")
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print('')
print(f'O maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')
