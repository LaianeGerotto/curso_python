# tipos de funções: print, len, input, int, floot....
# def = definição de função, depois do DEF precisa ter 2 linhas separando

# def mensagem(msg):
#     print('-' * 30)
#     print(msg)
#     print('-' * 30)
#
#
# mensagem('SISTEMAS CANINOS')
# mensagem('MEG LINDA')

# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')
#     print()
#
# #Programa principal sempre no início
# soma(4, 5) #os numeros são parametros
# soma(8, 9)
# soma(2, 1)

# def contador(* num):
#     tam = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tam} numeros')
#
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos]*=2
#         pos += 1
#
# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}' )


soma(5, 2)
soma(2, 9, 4)