
"""
	* Projeto: Conversor de automatos 
	* Autor: Joyce Claine, Marcos Monteiro
	* Dados: 12/11/2020
	* Versao: 1.0
	* Data da ultima modificao: 12/11/2020
	* Descricao: Algoritmo que converte automato AFN para AFD.
"""
import pandas as pd

#--------------------------------------------------------
# Recebendo AFN como entrada do usuário

afn = {}
n = int(input("N° de Estados: "))                #Digite o nº total dos estados
t = int(input("N° de Transições/alfabeto: "))   #Digite o nº total de transições/caminhos, por exemplo: a, b, então insira 2 para a, b, c, entrada 3
for i in range(n):  
    estado = input("Nome do estado: ")          #Insira o nome do estado, por exemplo: A, B, C, q1, q2 ..etc
    afn[estado] = {}                             #Criação de um dicionário aninhado
    for j in range(t):
        caminho = input("Transicao: ")             #Insira a transição, por exemplo: a ou b em {a, b} 0 ou 1 em {0,1}
        print("Chegue ao estado final a partir do estado {} viajando pelo caminho {}:".format(estado,caminho))
        estado_alcancado = [x for x in input().split()]  #Insira todos os estados finais
        afn[estado][caminho] = estado_alcancado       #Atribuindo os estados finais aos caminhos no dicionário

print("\nAFN :\n")
print(afn)                                      #Printando AFN
print("\nAFN: ")
tabela_afn = pd.DataFrame(afn)
print(tabela_afn.transpose())

print("Qual o estado final da AFN : ")
afn_estado_final = [x for x in input().split()]  #Entre com o estado final da AFN
#--------------------------------------------------------                 
    
lista_novos_estados = []                          #contém todos os novos estados criados no AFD
afd = {}                                      #dicionário/tabela AFD ou a estrutura de saída necessária
lista_chaves = list(list(afn.keys())[0])     #contém todos os estados em afn mais os estados criados em afd também são anexados posteriormente
lista_caminhos = list(afn[lista_chaves[0]].keys())    #lista de todos os caminhos, por exemplo: [a, b] ou [0,1]

#-------------------------------------------------------- 

# Calculando a primeira linha da tabela de transição AFD

afd[lista_chaves[0]] = {}                        #criando um dicionário aninhado no afd
for y in range(t):
    var = "".join(afn[lista_chaves[0]][lista_caminhos[y]])   #criando uma única string de todos os elementos da lista que é um novo estado
    afd[lista_chaves[0]][lista_caminhos[y]] = var            #atribuir o estado na tabela AFD
    if var not in lista_chaves:                         #se o estado for recém-criado
        lista_novos_estados.append(var)                  #em seguida, anexe-o a lista de novos estados
        lista_chaves.append(var)                        #bem como para lista de chaves que contém todos os estados
        
#-------------------------------------------------------- 
 
# Calculando as outras linhas da tabela de transição AFD

while len(lista_novos_estados) != 0:                     #condição é verdadeira apenas se a lista de novos estados não estiver vazia
    afd[lista_novos_estados[0]] = {}                     #pegando o primeiro elemento da lista de novos estados e examinando-o
    for _ in range(len(lista_novos_estados[0])):
        for i in range(len(lista_caminhos)):
            temp = []                                #criando uma lista temporária
            for j in range(len(lista_novos_estados[0])):
                temp += afn[lista_novos_estados[0][j]][lista_caminhos[i]]  #levando a união dos estados
            s = ""
            s = s.join(temp)                         #criando uma única string (novo estado) de todos os elementos da lista
            if s not in lista_chaves:                   #se o estado for recém-criado
                lista_novos_estados.append(s)            #em seguida, anexe-o a lista de novos estados
                lista_chaves.append(s)                  #bem como para lista de chaves que contém todos os estados
            afd[lista_novos_estados[0]][lista_caminhos[i]] = s   #atribuir o novo estado na tabela AFD
        
    lista_novos_estados.remove(lista_novos_estados[0])       #Removendo o primeiro elemento da lista de novos estados

print("\nAFD: \n")    
print(afd)                                           #Impressão do AFD criado
print("\nTabela AFD ")
tabela_afd = pd.DataFrame(afd)
print(tabela_afd.transpose())

afd_lista_estados = list(afd.keys())
afd_estados_finais = []
for x in afd_lista_estados:
    for i in x:
        if i in afn_estado_final:
            afd_estados_finais.append(x)
            break
        
print("\nEstados finais do afd: ",afd_estados_finais)       #Imprimindo estados finais do AFD
