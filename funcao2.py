# muda os '#define' pelos seus determinados valores.

def define(nomedef, valordef, lista_linha):
    for linhas in lista_linha:
        for palavras in linhas:
            if nomedef in palavras:
                index_linha = lista_linha.index(linhas)
                index_palavra = lista_linha[index_linha].index(palavras)
                lista_linha[index_linha][index_palavra] = lista_linha[index_linha][index_palavra].replace(nomedef, valordef)
    return lista_linha
