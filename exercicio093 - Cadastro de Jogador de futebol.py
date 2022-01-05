'''
cadastro = dict()
soma = 0
partidas = []
cadastro['nome'] = str(input('Nome do Jogador: '))
quantidade = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
for contador in range(0, quantidade):
    partidas.append(int(input(f'   Quantos gols na partida {contador}? ')))
soma = sum(partidas)
cadastro['gols'] = partidas
cadastro['total'] = soma

print('-='*30)
print(cadastro)
print('-='*30)
for k, v in cadastro.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {cadastro["nome"]} jogou {quantidade} partidas.')
for contador in range(0, quantidade):
    print(f'  => Na partida {contador}, fez {partidas[contador]} gols.')
print(f'Foi um total de {soma} gols.')
'''
#Correção Guanabara
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')