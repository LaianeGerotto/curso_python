'''
teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = '22'
galera.append(teste[:])
print(galera)

'''
'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# print(galera[0])
# print(galera[0][0])
# print(galera[1])
for p in galera:
    #print(p[0]) #0 imprime só os nomes, sem 0 imprime a lista completa
    print(f'{p[0]} tem {p[1]} de idade')
'''

galera = list()
dado = list()
totalmaior = totalmenor = 0
for contador in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor += 1
print(f'Temos {totalmaior} maiores de idade e {totalmenor} menores de idade')
