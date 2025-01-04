# Clarice Lopes Costa - 20230014256

# 01
def criar_tabela(colunas, linhas):
    tabela = {}
    for i in range(len(colunas)):
        coluna = colunas[i]
        linha = linhas[i]
        tabela[coluna] = linha
    return tabela

# 02 
def add_linha(tabela, n): 
    for coluna, valor in n.items(): 
      tabela[coluna].append(valor) 

    return tabela

# 03
def remover_linha(tabela, r): 
    for coluna in tabela: 
        tabela[coluna].pop(r)  

    return tabela 

# 04
def add_coluna(tabela, n, v):
    tabela[n] = v

    return tabela

# 05
def remover_coluna(tabela, n):
    if n in tabela:
        del tabela[n] 
    
    return tabela 

# 06
def soma_valores(tabela):
  soma = 0
  for i in tabela.values(): 
    for j in i:
      if type(j) == str: 
         pass
      else:
         soma += int(j) 

  return soma 

# 07
def media_valores(tabela):
  soma = 0
  cont = 0
  for i in tabela.values():
    for j in i:
      if type(j) == str:
        pass
      else:
        soma += int(j)
        cont += 1

  media = soma/cont
  return media

# 08
def exibir(tabela):
  print(tabela.keys()) 
  tamanho = len(list(tabela.values())[0]) 

  for i in range(tamanho):
    for j in tabela.keys():
      print(tabela[j][i], end=' ') 
    print() 

  return exibir

# 09 
def abrir_csv():  
  nova = {}
  colunas = ["name", "age"]

  for coluna in colunas:
    nova[coluna] = []
  with open("oscars.csv", "r") as arqCSV:
    arqCSV.readline()

    for linha in arqCSV:
      linha = linha.strip().split(",")
      nova['name'].append(linha[3])
      nova['age'].append(linha[5])

    return exibir(nova) 

# 10
def filtro(tabela):
  posicoes = []
  for i in tabela.values():
    cont = 0
    for j in i:
      if j == 'F':
        posicoes.append(cont)
      cont += 1

  for j in posicoes:
    print(tabela["Nome"][j]) 