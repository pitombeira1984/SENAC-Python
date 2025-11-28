import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('D:/ESTUDOS/SENAC/Python/Desafio_Portal_Aluno/TabDesafio.csv')

df["Soma"] = df.loc[:, "Questao 1":"Questao 17"].sum(axis=1)

df["Media"] = df.loc[:, "Questao 1":"Questao 17"].mean(axis=1)

print(df.head().round(2))

#df.loc[:, "Questao 1":"Questao 17"] → seleciona todas as colunas da Questão 1 até a 17
#.sum(axis=1) → soma em cada linha (por aluno)
#.mean(axis=1) → média em cada linha (por aluno)

# Variância de todas as colunas
variancia = df.var()
#print("Variância:\n", variancia.round(2))

# Desvio padrão de todas as colunas
desvio_padrao = df.std()
#print("\nDesvio padrão:\n", desvio_padrao.round(2))

variancia_DesvioPadao = pd.DataFrame({
    'Variancia': variancia,
    'Desvio Padrão': desvio_padrao
})
print(variancia_DesvioPadao)

