'''
print('-'*35)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-'*35)
listagem = ('Lápis', 1.75,
           'Borracha', 2.00,
           'Caderno', 15.90,
           'Estojo', 25.00,
           'Transferidor', 4.20,
           'Compasso', 9.99,
           'Mochila', 120.32,
           'Canetas', 22.30,
           'Livro', 34.90)
for item in range(0,16,2):
    print(f'{listagem[item].ljust(25,".")}R$ {str(listagem[item+1]).rjust(7)}')
print('-'*35)
'''
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)
listagem = ('Lápis', 1.75,
           'Borracha', 2.00,
           'Caderno', 15.90,
           'Estojo', 25.00,
           'Transferidor', 4.20,
           'Compasso', 9.99,
           'Mochila', 120.32,
           'Canetas', 22.30,
           'Livro', 34.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)