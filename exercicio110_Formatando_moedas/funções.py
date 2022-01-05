
def metade(preço=0, formato=False):
    resp = preço/2
    return resp if formato is False else moeda(resp)


def dobro(preço=0, formato=False):
    resp = preço*2
    return resp if not formato else moeda(resp)


def aumentar(preço=0, taxa=0, formato=False):
    resp = preço + (preço * taxa/100)
    return resp if not formato else moeda(resp)


def diminuir(preço=0, taxa=0, formato=False):
    resp = preço - (preço * taxa / 100)
    return resp if formato is False else moeda(resp)

def moeda(preço=0, moeda='R$'):
    if True:
        return f'{moeda}{preço:>.2f}'.replace('.', ',')

# def resumo(preço, mais=10, menos=5):
#     print('-' * 30)
#     print('RESUMO DO VALOR'.center(30))
#     print('-' * 30)
#     listagem = ('Preço analisado:',
#                 'Dobro do preço:',
#                 'Metade do preço:',
#                 '80% de aumento:',
#                 '35% de redução:')
#
#     calculos = (moeda(preço),
#                 dobro(preço, True),
#                 metade(preço, True),
#                 aumentar(preço, mais, True),
#                 diminuir(preço, menos, True))
#
#     for pos in range(0, len(listagem)):
#         print(f'{listagem[pos]:<20}', end='')
#         print(f'{calculos[pos]:<20}', end='')
#         print()
#     print('-' * 30)

#Correção Guanabara
def resumo(preço=0, mais=10, menos=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{mais}% de aumento: \t{aumentar(preço, mais, True)}')
    print(f'{menos}% de redução:  \t{diminuir(preço, menos, True)}')
    print('-' * 30)


