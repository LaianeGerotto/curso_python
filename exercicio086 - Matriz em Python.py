
matriz = [[], [], []]
for contador in range(0,3):
    num = int(input(f'Digite um valor para [0, {contador}] : '))
    matriz[0].append(num)
for contador in range(0, 3):
    num = int(input(f'Digite um valor para [1, {contador}] : '))
    matriz[1].append(num)
for contador in range(0, 3):
    num = int(input(f'Digite um valor para [2, {contador}] : '))
    matriz[2].append(num)
for contador in (matriz[0]):
    print(f'[{contador:^5}]', end=' ')
print()
for contador in (matriz[1]):
    print(f'[{contador:^5}]', end=' ')
print()
for contador in (matriz[2]):
    print(f'[{contador:^5}]', end=' ')


#Correção Guanabara
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for linha in range(0,3):
#     for coluna in range(0,3):
#         matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}] : '))
# print('-='*30)
# for linha in range(0, 3):
#     for coluna in range(0, 3):
#         print(f'[{matriz[linha][coluna]:^5}]', end='')
#     print()
