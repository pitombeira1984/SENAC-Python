
# Etapa 1: Importar a biblioteca e criar os dados
import pandas as pd

vendas_lojas = [
    'RioMar', 'Iguatemi', 'Centro', 'RioMar', 'Iguatemi', 'Iguatemi', 'RioMar',
    'Centro', 'Iguatemi', 'RioMar', 'RioMar', 'Iguatemi', 'RioMar', 'Centro',
    'Iguatemi', 'Iguatemi', 'RioMar', 'RioMar', 'Centro', 'Iguatemi', 'RioMar',
    'Iguatemi', 'RioMar', 'RioMar', 'Centro', 'RioMar', 'Iguatemi', 'RioMar',
    'Iguatemi', 'Centro', 'Iguatemi', 'RioMar', 'RioMar', 'Iguatemi', 'Iguatemi',
    'Centro', 'RioMar', 'Iguatemi', 'Centro', 'RioMar'
]

# Etapa 2: Criar o DataFrame
df = pd.DataFrame(vendas_lojas, columns=['Loja'])
df.head()  # Mostra as primeiras linhas da tabela

# Frequência Absoluta
freq_abs = df['Loja'].value_counts()
print(freq_abs)

# Frequência Relativa
freq_rel = df['Loja'].value_counts(normalize=True) * 100
print(freq_rel)

# Tabela completa
tabela_frequencias = pd.DataFrame({
    'Frequência Absoluta': freq_abs,
    'Frequência Relativa (%)': freq_rel
})
print(tabela_frequencias)

#Com base na análise de frequência, observamos que a loja RioMar apresentou o maior número de vendas,
#seguida pela Iguatemi e pela Centro. Portanto, se fôssemos premiar a equipe com o melhor desempenho
#em volume de vendas, a loja RioMar seria a vencedora, pois teve o maior número de registros de
#vendas no período analisado.