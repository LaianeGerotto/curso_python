while True:
    print('-'*34)
    n = int(input('Quer ver a Tabuada de qual valor? '))
    print('-'*34)
    if n < 0:
        break
    for contador in range(1, 11):
        tabuada = n * contador
        print(f'{n} x {contador} = {tabuada}')
print('PROGRAMA DE TABUADA ENCERRADO.')