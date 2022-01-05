
def leiaDinheiro(msg):
    valido = False
    while not valido:
        preço = str(input(msg)).replace(',','.').strip()
        if preço.isalpha() or preço == '':
            print(f'\033[0;31mERRO! "{preço}" é um preço inválido!.\033[m')
        else:
            valido = True
            return float(preço)