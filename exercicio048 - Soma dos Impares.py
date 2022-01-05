print('Soma entre todos os números Ímpares que são Múltiplos de 3.')
print('Intervalo da soma é 1 até 500.')
s = 0
cont = 0
for contador in range(1, 501,2):
    if contador % 3 == 0:
        s += contador
        cont += 1
print(f'A soma de todos os {cont} valores solcitados é {s}.')
