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

count_marca = df['marca'].value_counts()

labels = count_marca.index
sizes = count_marca.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title('Preferecia de Marcas de Celular')
plt.axis('equal')
plt.show()
