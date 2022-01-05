def area(l,c):
    medida = l * c
    print(f'A area de um terreno {l}x{c} é de {medida:.2f}m².')


print(f'Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)




