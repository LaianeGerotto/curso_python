matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
somac3 = 0
maior = 0
for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares = matriz[linha][coluna]
            somaPares += pares
print('-='*30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {somaPares}.')

for linha in range(0,3):
    somac3 += matriz[linha][coluna]
print(f'A soma dos valores da terceira coluna  é {somac3}.')

for coluna in range(0,3):
    if coluna == 0:
        maior == matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior}.')

