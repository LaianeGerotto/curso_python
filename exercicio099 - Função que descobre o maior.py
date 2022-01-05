from time import sleep

# def maior(*n):
#     print('-='*30)
#     print('Analisando os valores passados...')
#     contador = 0
#     while contador < len(n):
#         print(f'{n[contador]}', end=' ')
#         #sleep(0.5)
#         contador += 1
#     if (len(n) == 1 and n[0] == 0) or not n:
#         print(f'Foram informados 0 valores ao todo.')
#         print('O maior valor informado foi 0.')
#     else:
#         print(f'Foram informados {len(n)} valores ao todo.')
#         print(f'O maior valor informado foi {(max(n))}.')
#
#
# maior(2,9,4,5,7,1)
# maior(4,7,0)
# maior(1,2)
# maior(6)
# maior()


#Correção Guanabara
def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        #sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()