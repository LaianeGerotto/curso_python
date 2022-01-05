from exercicio107_Exercitando_Módulos import funções

preço = float(input('Digite o preço: R$ '))
print(f'A METADE de {preço} é {funções.metade(preço)}')
print(f'A DOBRO de {preço} é {funções.dobro(preço)}')
print(f'Aumentando 10%, temos {funções.aumentar(preço,10)}')
print(f'Reduzindo 13%, temos {funções.diminuir(preço, 13)}')