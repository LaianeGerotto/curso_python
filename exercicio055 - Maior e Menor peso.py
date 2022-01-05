'''
peso = []
for contador in range(0,3):
    peso.append(float(input(f'Digite o peso da {contador+1}ª pessoa: ')))
print(f'O Maior peso é {(max(peso))} e Menor peso é {(min(peso))}')

'''
#Resolução GUANABARA
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}Kg.')
print(f'O menor peso é {menor}Kg.')
