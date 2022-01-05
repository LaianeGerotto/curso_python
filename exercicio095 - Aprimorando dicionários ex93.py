# cadastro = dict()
# jogadores = list()
# while True:
#     partidas = list()
#     cadastro.clear()
#     cadastro['nome'] = str(input('Nome do Jogador: '))
#     quantidade = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
#     for contador in range(0, quantidade):
#         partidas.append(int(input(f'   Quantos gols na partida {contador+1}? ')))
#     cadastro['gols'] = partidas[:]
#     cadastro['total'] = sum(partidas)
#     jogadores.append(cadastro.copy())
#     while True:
#         resp = input('Quer continuar? [S/N] ').upper().strip()
#         if resp in 'SN':
#             break
#         print('ERRO! Responda apenas S ou N.')
#     if resp == 'N':
#         break
# print('-='*30)
# print(f'{"cod":<4}{"nome":<10}{"gols":<20}{"total":<4}')
# print('--'*30)
#
# for i, jogador in enumerate(jogadores):
#     print(f'{i:>3} {jogador["nome"]:<10}{str(jogador["gols"]):<20}{jogador["total"]:<4}')
#
# print('--'*30)
# while True:
#
#     opc = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
#     if opc == 999:#
#         break
#     elif opc > len(jogadores) - 1:
#         print(f'ERRO! Não existe jogador com o codigo {opc}! Tente novamente')
#         print('--' * 30)
#     elif opc <= len(jogadores) - 1:
#         print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opc]["nome"]}:')
#         for i, gols in enumerate(jogadores[opc]["gols"]):
#             print(f'No jogo {i+1} fez {gols} gols.')
#print('<<< VOLTE SEMPRE >>>')

#Correção Guanabara
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if resp == 'N':
        break

print('-='*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o codigo {busca}! Tente novamente')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')


