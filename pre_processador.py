from funcao1 import pre_processador
from funcao3 import pre_processador2

arquivo = "teste.c"

#Criando as listas 

lista_linha = pre_processador(arquivo)
lista_linha = pre_processador2(lista_linha)

#tratando para execução
funcoes = ['void','int','char']

#substituindo funções para execução

for funcao in funcoes:
    if funcao in lista_linha:
        funcao_aux = funcao + ' '
        lista_linha = lista_linha.replace(funcao,funcao_aux)

if 'print f' in lista_linha:
    lista_linha = lista_linha.replace('print f','printf')


print('\n\nO pre_processador foi executado com sucesso!\n\n')

#gravando o programa pre processado em outro arquivo para execução
with open('Pre-processado.c','w') as output:
        output.write(lista_linha)
        output.close()
        
