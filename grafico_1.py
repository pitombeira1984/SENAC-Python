import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = {'idade':[22,25,30,45,51,23,28,32,35,
                  40,42,50,21,29,33,38,41,26,
                  24,31,36,48
                  ]
        }

df = pd.DataFrame(dados, columns=['idade'])
df.head()

freq_abs = df['idade'].value_counts().sort_index()
print(f'{freq_abs}')

freq_rel = df['idade'].value_counts(normalize=True).sort_index() * 100
freq_rel = freq_rel.round(2).astype(str) + '%'
print(freq_rel)

# Tabela completa
tabela_frequencias = pd.DataFrame({
    'Frequência Absoluta': freq_abs,
    'Frequência Relativa (%)': freq_rel
})
print(tabela_frequencias)

# Gerando o histograma
sns.histplot(x='idade', data=df, bins=7, kde=True, color='skyblue')

# Exibindo o gráfico
plt.title('Distribuição das Idades')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()