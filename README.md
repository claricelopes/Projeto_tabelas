# Projeto CDIA

## 📋 Objetivo

O objetivo deste projeto é criar um módulo chamado **`table`**, que fornece funções para manipular e trabalhar com tabelas de maneira eficiente. O módulo permite criar, modificar e exibir tabelas utilizando operações comuns, como adicionar e remover linhas e colunas, realizar cálculos estatísticos e filtrar dados.

---

## 🛠️ Funcionalidades

O módulo **`table`** oferece as seguintes funcionalidades:

1. **Criar tabela**  
   Dada uma lista de nomes de colunas e uma matriz de valores, cria uma tabela na forma de um dicionário, onde:
   - As chaves representam os nomes das colunas.
   - Os valores são listas representando as linhas de cada coluna.

2. **Adicionar linha**  
   Adiciona uma nova linha à tabela, dado uma lista de valores. Os valores devem corresponder às colunas existentes.

3. **Remover linha**  
   Remove uma linha específica da tabela, dado o índice da linha.

4. **Adicionar coluna**  
   Adiciona uma nova coluna à tabela, dado o nome da coluna e uma lista de valores.

5. **Remover coluna**  
   Remove uma coluna da tabela, dado o nome da coluna.

6. **Soma**  
   Calcula a soma dos valores numéricos de cada coluna. Colunas com valores não numéricos são ignoradas.

7. **Média**  
   Calcula a média dos valores numéricos de cada coluna. Colunas com valores não numéricos são ignoradas.

8. **Exibir tabela**  
   Imprime a tabela no formato tabular no terminal.  
   Exemplo:

9. **Abrir CSV**  
Lê o arquivo CSV oscars.csv e cria uma nova tabela com base nos dados.

10. **Filtrar**  
 Filtra as linhas da tabela que satisfazem uma condição. Uma função é passada como parâmetro para definir a condição.  
 Exemplo: Filtrar linhas onde a idade é maior que 20.

---

## ⚙️ Estrutura de Dados

A tabela é representada como um dicionário no seguinte formato:

```python
tabela = {
 'nome': ['joão', 'maria', 'josé'],
 'idade': [20, 21, 19]
}
