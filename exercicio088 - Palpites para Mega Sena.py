from random import randint
from time import sleep

print('-'*40)
print('{:^40}'.format('JOGA NA MEGA SENA'))
print('-'*40)
jogada = []
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print('-'*40)
print()
print('-=' * 5, f' SORTEANDO {quantidade} JOGOS', '-=' * 5)
print()
#     Fiz sozinha....

# for contador in range(0,quantidade):
#     for quantidade in range(0,6):
#         quantidade = randint(1,60)
#         jogada.append(quantidade)
#         jogada.sort()
#     print(f'Jogo {contador+1}:{jogada}')
#     jogada.clear()

# Com ajuda do Bruno, com verificação dos numeros sem ser repetido na lista
for contador in range(0, quantidade):
    while True:
        if len(jogada) == 6:
            break
        else:
            quantidade = randint(1, 60)
            if quantidade not in jogada:
                jogada.append(quantidade)
    jogada.sort()
    print(f'Jogo {contador + 1}:{jogada}')
    jogada.clear()
    sleep(1)
print()
print('-=' * 5, '  < BOA SORTE! >  ', '-=' * 5)
'''
lista = list()
jogos = list()
tot = 1
print('-'*30)
print('   JOGA NA MEGA SENA    ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f' SORTEANDO {quant} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}:{l}')
    sleep(1)
print('-='*5,'< BOA SORTE! >', '-='*5 )
'''

