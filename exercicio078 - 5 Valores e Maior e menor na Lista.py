valores = []
maior = 0
menor = 0
for contador in range(0,5):
    valores.append(int(input(f'Digite um valor para a Posição {contador}: ')))
    if contador == 0:
        maior = menor = valores[contador]
    else:
        if valores[contador] > maior:
            maior = valores[contador]
        elif valores[contador] < menor:
            menor = valores[contador]
print('-'*35)
print(f'Você digitou os valores {valores}')
print(f'O Maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O Menor valor digitado foi {menor} nas posições ', end='...')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()