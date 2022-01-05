# from time import sleep
# def mensagem(msg):
#     print('-' * 45)
#     print(msg)
#
#
# # Contador de 1 até 10
# def função1():
#     mensagem(f'Contagem de 1 até 10 de 1 em 1')
#     for contador in range(1, 11):
#         print(contador, end=' ')
#         # sleep(0.5)
#     print('FIM!')
#
#
# # Contador de 10 até 1
# def função2():
#     mensagem(f'Contagem de 10 até 0 de 2 em 2')
#     for contador in range(10, -1, -2):
#         print(contador, end=' ')
#         # sleep(0.5)
#     print('FIM!')
#
# #Contador personalizado
# def função3(p):
#     if not p or p == '0':
#         p = 1
#     else:
#         p = int(p)
#
#     if p < 0:
#         mensagem(f'Contagem de {i} até {f} de {p*-1} em {p*-1}')
#         if i < f:
#             for contador in range(i, f+1, p*-1):
#                 print(contador, end=' ')
#                 # sleep(0.5)
#             print('FIM')
#         if i > f:
#             for contador in range(i, f-1, p):
#                 print(contador, end=' ')
#                 # sleep(0.5)
#             print('FIM')
#     else:
#         mensagem(f'Contagem de {i} até {f} de {p} em {p}')
#         if i < f:
#             for contador in range(i, f+1, p):
#                 print(contador, end=' ')
#                 # sleep(0.5)
#             print('FIM')
#         if i > f:
#             for contador in range(i, f-1, -p):
#                 print(contador, end=' ')
#                 # sleep(0.5)
#             print('FIM')
#
#
# função1()
# função2()
# mensagem('Agora é sua vez de personalizar a contagem!')
# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = (input('Passo: '))
# função3(p)

#Correção Guanabara
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            #sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            #sleep(0.5)
            cont -= p
        print('FIM!')

#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)