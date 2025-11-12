# PARTE 1: CRIAÇÃO DA BASE DE DADOS (O TRABALHO MANUAL)
# Tarefa 1: Criar o Arquivo Excel

# O arquivo livraria_vendas.xlsx foi criado, e salvo na mesma pasta de LivrariaDev.py

# PARTE 2: CONFIGURAÇÃO E IMPORTAÇÃO (CÓDIGO COLAB)
# Tarefa 2: Importar Bibliotecas e Fazer Upload

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('d:/ESTUDOS/SENAC/Python/LivrariaDev/livraria_vendas.xlsx')

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

#print(top_categoria)

# A categoria Ficção Científica é a mais vendida.

# Tarefa 5: Análise de Valores (O Gasto)

media = df['Valor'].mean()
mediana = df['Valor'].median()
desvio_padrao = df['Valor'].std()
maior_gasto = df['Valor'].max()
menor_gasto = df['Valor'].min()

analise_gastos = pd.DataFrame([{
    "Média Gasto":media,
    "Mediana":mediana,
    "Desvio Padão":desvio_padrao,
    "Maior Gasto":maior_gasto,
    "Menor Gasto":menor_gasto
}]) 

#print(analise_gastos)

# Tarefa 6: Análise por Grupo (Aprofundando)

media_categoria = df.groupby('Categoria')['Valor'].mean()

#print(media_categoria)

# Resultado da Análise: A categoria Fantasia teve o maior valor médio de venda, diferente da Ficção Científica que é a mais vendida.

# PARTE 4: VISUALIZAÇÃO DE DADOS
# Tarefa 7: O Histograma (Distribuição dos Gastos)

#sns.histplot(df['Valor'], bins=10, kde=True)
#plt.title("Valor de Venda x Quantidade de Vendas")
#plt.xlabel("Valor de Venda")
#plt.ylabel("Quantidade de Vendas")
#plt.show()

# Tarefa 8: O Boxplot (Visão de Centro e Outliers)

#sns.boxplot(df['Valor'])
#plt.title("Boxplot — Identificação de Outliers (Livraria Dev)")
#plt.xlabel("Valor Total Venda (R$)")
#plt.show()

# Tarefa 9: Gráfico de Barras (Comparando Categorias)

#sns.barplot(x='Categoria', y='Valor', data=df)
#plt.title('Categiria x Valor')
#plt.show()

# PARTE 5: RELATÓRIO FINAL (A CONCLUSÃO DO ANALISTA)
# Tarefa 10: Escrevendo para o Gerente

# "Análise da Promoção da 'Livraria Dev'

# 1. Perfil de Gasto: O gasto médio por cliente foi de R$ 51.96. No entanto, a Mediana foi de R$ 45.00
# indicando que metade dos pedidos foi abaixo deste valor. O gasto foi bastante variável, com um Desvio Padrão de R$ 22.30,
# e os valores variaram de R$ 32.5 até R$ 120.00, como visto no Boxplot.

# 2. Desempenho por Categoria: A categoria Fantasia foi a que teve o maior valor médio de
# venda, com R$ 83.30. Curiosamente, a categoria mais vendida em quantidade foi Ficção Científica,
# mas seu ticket médio foi menor. O gráfico de barras ilustra bem essa diferença."