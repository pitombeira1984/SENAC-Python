
# Cenário: Você é o analista de dados da "Café Dev". A rede lançou uma nova bebida, o "Frappé Caramelo", e
# quer fazer uma análise completa dos 20 primeiros pedidos que incluíram esse item.
# O seu gerente de marketing pediu um relatório estatístico completo para responder a duas perguntas
# principais:
# 1. Qual é o perfil de gasto típico do cliente que compra essa bebida?
# 2. Esse gasto é consistente ou imprevisível?
# Sua Missão: Executar uma análise estatística completa no Google Colab, calculando todas as medidas
# solicitadas, visualizando os dados e escrevendo um relatório final.

#Parte 1: Configuração (Código Essencial)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados: O Valor Total do Pedido (em R$) dos 20 primeiros clientes

dados_vendas = [
28.00, 31.50, 12.00, 45.00, 28.00, 33.00, 25.50, 22.00, 30.00, 150.00,
28.00, 35.00, 40.00, 18.00, 26.00, 32.00, 29.00, 38.00, 24.50, 30.00
]           

df = pd.DataFrame(dados_vendas, columns=['Vlr_Total_Pedidos'] )
#print(df.head())

# Parte 2: Análise Descritiva Manual

# Tarefa 1: O Rol(Dados Ordenados)

# Rol(R$): 12.00, 18.00, 22.00, 24.50, 25.50, 26.00, 28.00, 28.00, 28.00, 29.00, 30.00, 30.00, 31.50, 32.00, 33.00, 35.00, 38.00, 40.00, 45.00, 150.00

rol = df.sort_values(by='Vlr_Total_Pedidos')
#print(rol)

# Tarefa 2: Tabela de Frequência

freq_abs = df['Vlr_Total_Pedidos'].value_counts()
#print(freq_abs)

# A tabela de frequência não é muito útil neste caso, pois a maioria dos valores é única (aparece apenas uma vez).
# Isso indica alta variabilidade nos pedidos, com poucos valores repetidos (somente R$28 e R$30 aparecem mais de uma vez).

# Parte 3: Medidas de Centro e Dispersão
# Tarefa 3: Cálculos Estatísticos

soma = df['Vlr_Total_Pedidos'].sum()
media = df['Vlr_Total_Pedidos'].mean()
mediana = df['Vlr_Total_Pedidos'].median()
moda = df['Vlr_Total_Pedidos'].mode()[0]
amplitude = df['Vlr_Total_Pedidos'].max() - df['Vlr_Total_Pedidos'].min()
desvio = df['Vlr_Total_Pedidos'].std()

#print(f"Média: R${media:.2f}")
#print(f"Mediana: R${mediana:.2f}")
#print(f"Moda: R${moda:.2f}")
#print(f"Amplitude: R${amplitude:.2f}")
#print(f"Desvio Padrão: R${desvio:.2f}")

tabela_estatistica = pd.DataFrame([{
    'Soma': soma,
    'Média': media,
    'Mediana': mediana,
    'Moda': moda,
    'Amplitude Total': amplitude,
    'Desvio Padão': desvio
}])
#print(tabela_estatistica)

# Parte 4: Visualização de Dados

# Tarefa 4: O Histograma (Visualizando a Frequência)

sns.histplot(df['Vlr_Total_Pedidos'], bins=10, kde=True)
plt.title("Distribuição dos Valores dos Pedidos — Frappé Caramelo")
plt.xlabel("Valor Total do Pedido (R$)")
plt.ylabel("Frequência")
#plt.show()

# Tarefa 5: O Boxplot (Visualizando o Outlier)

sns.boxplot(df['Vlr_Total_Pedidos'])
plt.title("Boxplot — Identificação de Outliers (Frappé Caramelo)")
plt.xlabel("Valor Total do Pedido (R$)")
plt.show()

# Parte 5 – Relatório Final (Texto para o Colab)
# Análise do Lançamento do "Frappé Caramelo"

# 1. O Gasto Típico:
# O gasto médio por cliente foi de R$36,33. No entanto, observei que a média foi puxada para cima por um único pedido de R$150,00, identificado claramente como outlier no Boxplot.
# Assim, a Mediana, de R$29,50, representa de forma mais justa o gasto típico do cliente.

# 2. Consistência dos Pedidos:
# O Desvio Padrão foi de R$29,44, indicando baixa consistência nos gastos, pois há grande variação entre os pedidos.
# Mesmo desconsiderando o outlier, a maioria dos valores se concentra entre R$20 e R$40, o que o Histograma confirma.
# Portanto, os gastos são moderadamente imprevisíveis, mas tendem a se agrupar nessa faixa intermediária — o que representa o perfil típico de consumo para o novo produto.


