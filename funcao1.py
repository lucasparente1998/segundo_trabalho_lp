def pre_processador(arquivo):
    arq = open(arquivo,'r')
    #verificando se houve algum problema na abertura do arquivo

    if arq == None:
        print('erro na leitura do arquivo')

    # separando o código do arquivo entrada em linhas

    lista_entrada = []

    for line in arq:
        linha = line.strip('\n')
        lista_entrada.append(linha)
    arq.close()
    
    #removendo os comentarios 

    for linha in lista_entrada:
        if '//' in linha:
            #recorta as linhas com comentarios
            aux_linha = linha.index('/')
            aux_lista_entrada = lista_entrada.index(linha)
            lista_entrada[aux_lista_entrada] = linha[0:aux_linha] 
    
    #Separando as listas de strings em lista de listas
     
    lista_linha = []
    for string in lista_entrada:
        palavra = string.split()
        lista_linha.append(palavra)
    
    #Armazenamento dos includes

    lista_include = []
    for include in lista_linha:
        if("#include" in include):
            lista_include.append(include[1][1:-1])
            del(lista_linha[lista_linha.index(include)])
    
    #Colocando as linhas da blibioteca na frente

    if len(lista_include) != 0:
        for elemento in lista_include:
            aux = pre_processador(elemento)
            lista_linha = aux + lista_linha
    
    return lista_linha