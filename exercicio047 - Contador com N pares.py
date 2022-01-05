'''
for contador in range (0, 51, 2):
       print(contador, end=',')

# esse usa MENOS memória
'''

print('Todos os números Pares entre 1 e 50.')
for contador in range(1, 51):
    if contador % 2 == 0:
        print(contador, end=' ')
#esse usa MAIS memória.