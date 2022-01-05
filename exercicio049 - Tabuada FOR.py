n1 = int(input('Digite um número: '))
print('='*22)
print(f' Tabuada do número {n1}')
print('='*22)
for contador in range(1,11):
    tabuada = n1 * contador
    print(f'{n1} x {contador} = {tabuada}')