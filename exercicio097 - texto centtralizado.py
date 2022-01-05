def centralizar(mensagem):
    tamanho = len(mensagem) + 4
    print('~' * tamanho)
    print(mensagem.center(tamanho))
    print('~' * tamanho)

centralizar('Meg maravilhosa')
centralizar('Canina')
centralizar('Tineném')