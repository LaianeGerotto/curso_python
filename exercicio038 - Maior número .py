#verificar qual número é maior.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'O primeiro número é MAIOR.')
elif n2 > n1:
    print(f'O segundo número é MAIOR.')
#elif n1 == n2:
else:
    print('Não existe número maior, os dois são iguais!')