#Crie um programa onde o usuário possa digitar 7 valores númericos e cadastre-os em uma lista única que mantenha separados
#os valores pares e impares. No final mostre os valores pares e impares em ordem crescente.
lista = [[], []]
for contador in range(1,8):
    num = int(input(f'Digite o {contador}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')