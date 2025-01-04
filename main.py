# Clarice Lopes Costa - 20230014256

from table import *

#01 - Criar tabela 
print("01 - TABELA") 
table = criar_tabela(["Posição", "Nome", "Sexo"], [[1, 2, 3], ["João", "Maria", "Pedro"], ["M", "F", "M"]]) 
print(table) 

#02 - Adicionar linha a tabela
print("\n02 - ADICIONANDO LINHA") 
nova_linha = {
                'Posição' :  4,
                'Nome' : "José", 
                'Sexo' : 'M' 
            }  
add_linha(table, nova_linha)
print(table) 

#03 - Remover linha da tabela
print("\n03 - REMOVENDO LINHA") 
indice_remocao = 3 
remover_linha(table, indice_remocao) 
print(table) 

#04 - Adicionar coluna a tabela
print("\n04 - ADICIONANDO COLUNA") 
nova_coluna = "Curso"
novo_valor = ["CDIA", "CC", "CDIA"] 
add_coluna(table, nova_coluna, novo_valor) 
print(table) 

#05 - Remover coluna da tabela
print("\n05 - REMOVENDO COLUNA")
coluna_remocao = 'Curso' 
remover_coluna(table, coluna_remocao) 
print(table)

#06 - Somar os valores das calunas 
print("\n06 - SOMANDO VALORES")
soma_valores(table) 
print(f"A soma dos valores presentes nas colunas é: {soma_valores(table)}")    

#07 - Média dos valores das colunas
print("\n07 - MÉDIA DOS VALORES")
media_valores(table)
print(f"A média dos valores presentes nas colunas é: {media_valores(table)}") 

#08 - Exibir tabela
print("\n08 - EXIBINDO TABELA")
exibir(table) 

#09 - Abrir arquivo CSV 
print("\n09 - CRIANDO NOVA TABELA COM ARQUIVO CSV")  
abrir_csv()  

#10 - Filtrar tabela  
print("\n10 - Filtrando da tabela apenas nomes de pessoas com sexo Feminino:")    
filtro(table) 