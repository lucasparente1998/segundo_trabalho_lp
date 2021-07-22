from funcao2 import define

def pre_processador2(lista_linha):
    #deletando a linha dos define
    for elemento in lista_linha:
        if '#define' in elemento:
            lista_linha = define(elemento[1],elemento[2], lista_linha)
            lista_linha[lista_linha.index(elemento)] = ''

    # removendo os comentários do tipo '/*' '*/'.

    for string in lista_linha:
        index = lista_linha.index(string)
        lista_linha[index] = ''.join(lista_linha[index])

    lista_linha = ''.join(lista_linha)
    lista_linha = lista_linha.replace('/*','*/')
    lista_linha = lista_linha.split('*/')


    for y in range(1,len(lista_linha),2):
        lista_linha[y]= ""
    lista_linha = ''.join(lista_linha)
    return lista_linha