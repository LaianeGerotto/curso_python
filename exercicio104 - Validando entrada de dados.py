def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        x = str(input(msg))
        if x.isnumeric():
            valor = int(x)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


print('-'*20)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')