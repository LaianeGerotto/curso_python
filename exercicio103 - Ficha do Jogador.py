# def ficha(nome, gol):
#     if not nome:
#         nome = '<desconhecido>'
#     if not gol:
#         gol = 0
#     return f'O jogador {nome} fez {gol} gol(s) no campeonato.'
#
# nome = input('Nome do Jogador: ')
# gol = input('Número de Gols: ')
# resultado = ficha(nome, gol)
# print(resultado)

#CORREÇÃO GUANABARA
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)