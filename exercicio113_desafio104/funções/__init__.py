def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não informar esse número!\033[m')
            return 0
        else:
            return inteiro



def leiaReal(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número Real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mO usuário preferiu não informar esse número!\033[m')
            return 0
        else:
            return real


