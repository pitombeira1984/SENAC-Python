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

print(df.head())
print(df.info())



