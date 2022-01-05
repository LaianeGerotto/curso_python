def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação do aluno.
    """
    result = dict()
    result['Total'] = len(n)
    result['Maior'] = max(n)
    result['Menor'] = min(n)
    result['Media'] = round(sum(n)/len(n),2)
    if sit:
        if result['Media'] >= 7:
            result['Situação'] = 'BOA'
        elif result['Media'] >= 5:
            result['Situação'] = 'RAZOÁVEL'
        else:
            result['Situação'] = 'RUIM'
    return result

resp = notas(3.5, 2, 6.5, 2, 7, 4)
print(resp)