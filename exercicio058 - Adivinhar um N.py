'''
from random import randint
n1 = randint(0,10)
contador = 0
print(n1)
nUser = []
while n1 != nUser:
    nUser = int(input('Digite um número de 0 a 10: '))
    print('Tente novamente!')
    contador += 1
if n1 == nUser:
    print('Você acertou!')
print('*' * 20)
print(f'Computador: {n1}')
print(f'Usuário: {nUser}')
print(f'Tentativas: {contador}')
print('*' * 20)
'''

#Correção Guanabara
from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um nº entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print(f'Acertou com {palpites} tentativas. Parabéns!!')