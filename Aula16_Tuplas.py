#Tuplas são variáveis compostas e são imutáveis (não é possível mudar uma tupla)
#() tuplas não precisa mais usar acima do Python 3.7
#[] lista
#{} dicionario
lanche = 'Hambúrguer','Suco', 'Pizza', 'Pudim'
'''print(lanche)
print(len(lanche))
print(lanche[1:3])
print(lanche[2:])
print(lanche[3])
print(lanche[-1])
print(lanche[-3:])
print(lanche[:3])
print(sorted(lanche)) #coloca em ordem alfabética
#-----------------------------------------------------------------------------------------------------------------------
'''
'''
#Duas maneiras de escrever, ambos vão apresentar o mesmo resultado, porém o exemplo 2 não vai apresentar a posição
print ('Exemplo 1')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('--'*30)

print ('Exemplo 2')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi bastante!')
print('--'*30)

print ('Exemplo 3')
# Para mostrar a posição do FOR (Exemplo 2) é necessário editar o cód. conforme abaixo:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi bastante!')
#-----------------------------------------------------------------------------------------------------------------------
'''
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a+b
print(f'a - {a}')
print(f'b - {b}')
print(f'c - {c}')
print(f'c Organizado - {sorted(c)}')
print(f'Tamanho de C é {len(c)}')
print(f'{c.count(5)} é a quantidade de vezes que aparece o nº (5)')
print(f'{c.index(8)} é a posição que está o nº (8)')
print(f'{c.index(5)} é a posição que está o nº (5)')
print(f'{c.index(5,2)} é a posição que está o nº (5)') # o 2 se refere a partir da posição 2 q o prox número 5 está, pq o primeiro 5 está na 1.
#-----------------------------------------------------------------------------------------------------------------------
'''
'''
#Dados diferentes dentro das Tuplas
pessoa = ('Meg', 6, 'Femêa', 15)
#del(pessoa) #apaga os dados da Variável
print(pessoa)
'''