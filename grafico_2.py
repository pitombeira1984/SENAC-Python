import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

celular = {'marca':['apple','samsung','apple','motorola','samsung',
                          'samsung','apple','motorola','samsung','apple',
                          'xiaomi','sansung','apple','samsung','xiaomi'
                          ]
                }

df = pd.DataFrame(celular)
df.head()

freq_rel = df['marca'].value_counts(normalize=True) * 100
print(freq_rel.round(2))

# Gerando Gráfico Barra
sns.countplot(x='marca', data=df)

# Exibindo o gráfico
plt.title('Distribuição das Marcas')
plt.xlabel('Marcas')
plt.ylabel('Frequência')
plt.show()