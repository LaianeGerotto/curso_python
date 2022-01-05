'''
lista = []
pares = []
impar = []
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impar.append(num)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de pares é {impar}')
'''
#Correção Guanabara

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de pares é {impares}')
