def matchingstrings(strings, queries):
    # dicionario para contar as ocorrencias de cada query na string
    contagem = {}

    # lista para armazenar esses resultados para impressao na formataçao correta
    resultado = []

    # loop percorrendo a lista de strings, checando se estas existem na lista de queries. Se sim, cria uma chave no
    # dicionario com a query e incrementa o valor, senao cria uma chave com a query e seta o valor para 0
    for i in strings:
        if i in queries:
            contagem[i] = contagem.get(i, 0) + 1
        else:
            contagem[i] = 0
    # for do tamanho da lista de queries, adicionando a lista resultado criada acima os valores do dicionario
    # contagem, para impressao na tela

    for i in queries:
        resultado.append(contagem.get(i, 0))

    print(resultado)

    return list(contagem.values())


l1 = ['def', 'de', 'fgh']
l2 = ['de', 'lmn', 'fgh']

print(matchingstrings(l1, l2))
