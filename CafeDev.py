import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Tipos de Dados
# Lojas e Bebidas são considerados dados Qualitativos
# ID_Venda, Idade_Cliente, Valor_Total_Pedido, são considerados dados Quantitativos

dados = {
'ID_Venda': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
'Loja': [
'Iguatemi', 'RioMar', 'Centro', 'RioMar', 'Iguatemi', 'Iguatemi', 'RioMar',
'Centro', 'RioMar', 'Iguatemi',
'RioMar', 'Iguatemi', 'Centro', 'RioMar', 'Centro', 'Iguatemi', 'RioMar',
'RioMar', 'Centro', 'Iguatemi',
'RioMar', 'Iguatemi', 'Centro', 'RioMar', 'Iguatemi', 'Iguatemi', 'Centro',
'RioMar', 'Iguatemi', 'RioMar'
],
'Idade_Cliente': [
25, 31, 45, 29, 22, 28, 33, 51, 30, 26, 35, 24, 48, 32, 42, 27, 38, 36, 55,
23, 39, 28, 40, 95, 26, 28, 47, 34, 29, 37
],
'Valor_Total_Pedido': [
25.50, 31.00, 18.00, 29.00, 22.00, 28.50, 33.00, 20.00, 30.00, 26.00,
35.00, 24.00, 19.50, 32.00, 15.00,
27.00, 38.00, 36.00, 22.50, 23.00, 39.00, 28.00, 16.00, 41.00, 26.50,
28.00, 18.50, 34.00, 29.50, 37.00
],
'Bebida': [
'Espresso', 'Cappuccino', 'Espresso Tônico', 'Mocha', 'Latte',
'Espresso', 'Cappuccino', 'Chá Gelado', 'Espresso Tônico', 'Latte',
'Mocha', 'Espresso', 'Cappuccino', 'Chá Gelado', 'Mocha',
'Espresso Tônico', 'Latte', 'Espresso', 'Cappuccino', 'Chá Gelado',
'Espresso Tônico', 'Latte', 'Espresso', 'Cappuccino', 'Mocha', 'Espresso',
'Chá Gelado', 'Latte', 'Espresso Tônico', 'Cappuccino'
]
}

df = pd.DataFrame(dados)
#print(df.head())

# 2. Frequencia de Vendas(Geral)
freq_abs = df['Bebida'].value_counts()
freq_rel = df['Bebida'].value_counts(normalize=True).round(2)*100
freq_rel = freq_rel.astype(str) + '%'
# 2.1 Tabela Frequencia Geral
tabela_geral = pd.DataFrame({
    'Freq.Absolura':freq_abs,
    'Freq.Relativa':freq_rel
})
print('Tabela Geral\n', tabela_geral )
# 2.2 Tebela Frequencia por Loja
venda_bebida_loja = pd.crosstab(df['Loja'], df['Bebida'])
print('---Venda Bebida por Loja---\n', venda_bebida_loja)
venda_percentual = pd.crosstab(df['Loja'], df['Bebida'], normalize='index') * 100
venda_percentual = venda_percentual.round(2).astype(str) + '%'
print('---Venda Bebida por Loja(%)---\n', venda_percentual)
# A loja od Igratemi é a loja que vende mais Espresso Tônico, junto com a loja RioMar.
# Considerendo que Público mais jovem ou com maior poder aquisitivo, predisposto a experimentar bebidas modernas e refrescantes,
#geram um percentual de 18.18% na loja Iguatemi 

