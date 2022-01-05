import random
from time import sleep
print('********'*4)
print('           JOKENPÔ')
print('********'*4)
print('O Famoso Pedra, Papel e Tesoura!')
print('')
computador = random.choice(['pedra', 'papel', 'tesoura'])
#usuario = random.choice(['pedra', 'papel', 'tesoura'])
usuario = str(input('Digite a sua opção: ').lower())
print(f'Computador: {computador}')
print(f'Você: {usuario}')
print('********'*4)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('********'*4)
print('Resultado:')
if computador == usuario:
    print('Houve empate, inicie uma nova rodada!')
    #PEDRA
elif ((computador == 'pedra' or usuario == 'pedra') and (computador == 'papel' or usuario == 'papel')):
    if computador == 'pedra':
        print('Você ganhou!')
    else:
        print('Você perdeu!')
    print('Papel enrola Pedra!')
    #TESOURA
elif ((computador == 'pedra' or usuario == 'pedra') and (computador == 'tesoura' or usuario == 'tesoura')):
    if computador == 'tesoura':
        print('Você ganhou!')
    else:
        print('Você perdeu!')
    print('Pedra quebra tesoura!')
    #PAPEL
elif ((computador == 'papel' or usuario == 'papel') and (computador == 'tesoura' or usuario == 'tesoura')):
    if computador == 'tesoura':
        print('Você perdeu!')
    else:
        print('Você ganhou!')
    print('Tesoura corta papel!')


'''
Resolução Guanabara
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence!')
    elif jogador == 2:
        print('Computador Vence!')
    else:
        print('Jogada Inválida!')
        
elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('Computador Vence!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador Vence!')
    else:
        print('Jogada Inválida!')
        
computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('Jogador Vence!')
    elif jogador == 1:
        print('Computador Vence!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada Inválida!')    
    
'''



