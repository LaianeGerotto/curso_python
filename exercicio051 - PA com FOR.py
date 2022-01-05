print('=='*15)
print('  Progressão Aritmética - PA')
print('=='*15)
termo1 = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão: '))
print('')
print('Os 10º primeiros termos da PA:')
pa = termo1 + (10 - 1) * razao
for contador in range(termo1,pa + razao, razao):
    print(contador, end=' -> ')
print('Acabou')