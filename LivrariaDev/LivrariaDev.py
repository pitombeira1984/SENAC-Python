# PARTE 1: CRIAÇÃO DA BASE DE DADOS (O TRABALHO MANUAL)
# Tarefa 1: Criar o Arquivo Excel

# O arquivo livraria_vendas.xlsx foi criado, e salvo na mesma pasta de LivrariaDev.py

# PARTE 2: CONFIGURAÇÃO E IMPORTAÇÃO (CÓDIGO COLAB)
# Tarefa 2: Importar Bibliotecas e Fazer Upload

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('livraria_vendas.xlsx')

# Tarefa 3: Primeira Verificação

#print(df.head())
#print(df.info())

# PARTE 3: ANÁLISE DESCRITIVA
# Tarefa 4: Análise de Categorias

freq_abs = df['Categoria'].value_counts()
freq_rel = df['Categoria'].value_counts(normalize=True). round(2) * 100

top_categoria = pd.DataFrame({
    'Mais Vendidos':freq_abs,
    'Mais Vendidos(%)':freq_rel
})

print(top_categoria)

# A categoria Ficção Científica é a mais vendida.


