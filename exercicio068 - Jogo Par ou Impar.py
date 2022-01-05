'''from random import randint
print('-='*30)
print('                  VAMOS JOGAR PAR ou ÍMPAR?!')
print('-='*30)
contador = 0
while True:
    nuser = int(input('Digite um número: '))
    escolha = str(input('Você quer Par[P] ou Ímpar[I]? ')).upper().strip()
    computador = randint(0, 10)
    resultado = nuser + computador
    if resultado % 2 != 0:
        print(f'Você jogou {nuser} e o Computador {computador}. Total de {resultado} que é IMPAR.')
        if escolha != 'I':
            print('Você perdeu!')
            break
        print('Você ganhou!')
    else:
        print(f'Você jogou {nuser} e o Computador {computador}. Total de {resultado} que é PAR.')
        if escolha != 'P':
            print('Você perdeu!')
            break
        print('Você ganhou!')
    print('-_' * 30)
    contador += 1
print('-_' * 30)
print('GAME OVER!!')
print(f'Você venceu {contador} vezes!')'''

#Correção Guanabara
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o Computador {computador}. Total de {total}', end=' - ')
    print(' DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
    print(f'GAME OVER! Você venceu {v} vezes')











