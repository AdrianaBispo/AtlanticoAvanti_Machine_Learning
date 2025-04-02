import matplotlib.pyplot as plt
import numpy as np

'''
Questão 1:
Escreva uma função que receba uma lista de números e retorne outra lista
com os números ímpares.
'''

def numeros_impares(lista):
    retorno = []
    for i in lista:
        if(i % 2 != 0):
            retorno.append(i)
    return retorno


'''
Questão 2:
Escreva uma função que receba uma lista de números e retorne outra lista
com os números primos presentes.
'''
def verificacao(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos(numeros):
    return [num for num in numeros if verificacao(num)]


'''
Questão 3:
Escreva uma função que receba duas listas e retorne outra lista com os
elementos que estão presentes em apenas uma das listas
'''
def questao3(lista1, lista2):
    return list(set(lista1) ^ set(lista2))


'''
Questão 4:
Dada uma lista de números inteiros, escreva uma função para encontrar o
segundo maior valor na lista.
'''
def questao4(numeros):
    numeros.sort(reverse=True)  
    return numeros


'''
Questão 5:
Crie uma função que receba uma lista de tuplas, cada uma contendo o
nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das
pessoas em ordem alfabética.
'''
def ordenar(value):
    return sorted(value, key=lambda value: value[0])


'''
Questão 6:
'''
import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), layout="constrained")

for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                               transform=axs[row, col].transAxes,
                               ha='center', va='center', fontsize=18,
                               color='darkgrey')

fig.suptitle('plt.subplots()')
plt.show()


'''
Questão 7:
'''
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()


'''
Questão 8:
Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

R= Para visualizar as primeiras linhas de um arquivo .csv é necessario utilizar o metodo df.head(), segue exemplo
'''
import pandas as pd

df = pd.read_csv("movies.csv") 
print(df.head())


'''
Questão 9:
Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?
'''
df_filtrado = df[df["year"] > 2000] 
print(df_filtrado)

'''
Questão 10:
Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?
R= Pode ser utilizado o método "fillna(0)" que substituirá os valores NaN por 0
'''

print(df["gross"].fillna(0))