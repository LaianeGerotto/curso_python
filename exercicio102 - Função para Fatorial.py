#Correção Gunanabara
def fatorial(num, show=False):
    """
    -> Calcule o Fatorial de um número.
    :param num: O numero a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um numero num
    """
    f = 1
    for contador in range (num, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= contador
    return f


print(fatorial(5, show=True))
print(fatorial(5, show=False))
print(fatorial(5))
