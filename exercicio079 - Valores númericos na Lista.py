'''
valores = []
while True:
    #modo Bruno
    valor_digitado = int(input(('Digite um valor: ')))
    if valores.count(valor_digitado) >= 1:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(valor_digitado)
        print('Valor adicionado com Sucesso...')

    #modo Laiane
    # valores.append(int(input(('Digite um valor: '))))
    # atual = valores[-1]
    # if valores.count(atual) > 1:
    #     valores.pop()
    #     print('Valor duplicado! Não vou adicionar...')
    # else:
    #     print('Valor adicionado com Sucesso...')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-='*20)
valores.sort()
print(f'Você adicionou os valores {valores}')
'''

#Correção Guanabara

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso... ')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os valores {numeros}')