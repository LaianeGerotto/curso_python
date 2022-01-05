# fonte_branco = '\033[1;97m'
# fonte_preto = '	\033[1;30m'
# fundo_verde = '\033[1;42m'
# fundo_azul = '\033[1;44m'
# fundo_branco = '\033[1;107m'
# reset = '\033[m'
#
# def interação(msg):
#     while True:
#         print(f'{fundo_verde}{fonte_branco}SISTEMA DE AJUDA PyHELP')
#         opc = str(input(msg)).lower().strip()
#         if opc not in 'fim':
#             print(f"{fundo_azul}{fonte_branco}Acessando o manual do Comando '{opc}'")
#             print(fundo_branco, fonte_preto)
#             help(opc)
#         else:
#             while opc not in 'fim':
#                 opc = input('Função ou Biblioteca > ').lower()
#             if opc == 'fim':
#                 break
#             return msg
#
#
# n = interação(f'{reset}Função ou Biblioteca > ')

c = ('\033[m',        # 0 sem cor
     '\033[0;30;41m', # 1 vermelho
     '\033[0;30;42m', # 2 verde
     '\033[0;30;43m', # 3 amarelo
     '\033[0;30;44m', # 4 azul
     '\033[0;30;45m', # 5 roxo
     '\033[7;40m',    # 6 branco
     );

def ajuda(com):
    titulo(f"Acessando o manual do Comando '{comando}'", 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'{msg.center(tamanho)}')
    print('~' * tamanho)
    print(c[0], end='')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)





