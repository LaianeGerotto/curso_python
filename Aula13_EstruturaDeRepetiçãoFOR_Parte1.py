#Laços de Repetição - Parte 01
'''

for contador in range(0,2):
    print('Oi')
print('FIM!')
for contador in range(0,4):
    print(contador, end=", ")
print('FIM!')
for contador in range(4,0,-1):
    print(contador, end=", ")
print('FIM!')
for contador in range(0, 7,2):
    print(contador, end=", ")
print('FIM!')
for contador in range(0, 4+1):
    print(contador, end=", ")
print('FIM!')
for contador in range(0, 2):
    n = int(input('Digite um Valor:'))
print('FIM!')
'''

s = 0
for contador in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'A somátória de todos os valores foi {s}')