#Docstring é o manual criado para auxiliar na ajuda interativa
# def somar(a=0, b=0, c=0): # inserindo o zero, não dá erro caso, não tenha valor declarado
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela.
#     :param a: o primeiro valor
#     :param b: o segundo valor
#     :param c: o terceiro valor
#     :return: não há return
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')
#
# somar(3)

#Escopo de variáveis - Local e Global
# def funcao():
#     n1 = 4
#     print(f'N1 local/dentro vale {n1}')
#
#
# n1 = 2
# funcao()
# print(f'N1 global/fora vale {n1}')

# def funcao():
#     global n1 #usa a variável global dentro da local, porém a global recebe um novo valor
#     n1 = 4
#     print(f'N1 local/dentro vale {n1}')
#
#
# n1 = 2
# funcao()
# print(f'N1 global/fora vale {n1}')

#Retorno de valores
# def somar(a=0, b=0, c=0): # inserindo o zero, não dá erro caso, não tenha valor declarado
#     s = a + b + c
#     return s
#
# r1 = somar(3,2,5)
# r2 = somar(2,2)
# r3 = somar(6)
# print(f'Os resultados foram {r1}, {r2} e {r3}')

# def fatorial(num=1): # caso não informe o valor, num receberá 1
#     f = 1 # variável local
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')