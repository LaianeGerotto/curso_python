from random import randint
n1 = randint(0,5)
print('*' * 43)
print(' Tente adivinhar o número do Computador :)')
print('*' * 43)
n2 = int(input('Digite um número de 0 a 5: '))
if n1 == n2:
    print('PARABÉNS!!! Você acertou!')
else:
    print('Você perdeu!')
    print(f'Número escolhido pelo Computador foi {n1} e não {n2}.')
