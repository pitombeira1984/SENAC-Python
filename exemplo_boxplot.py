import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

minutos = [5, 6, 2, 8, 7, 12, 9, 6, 4]

#df = pd.DataFrame(minutos)
#print(df.describe().round(2))

#-------OU-----------#

df = pd.Series(minutos)

dados = df.head()

Q1 = dados.quantile(0.25)
print(f'Q1 (Calculado): {Q1}')
Q2 = dados.quantile(0.50)
print(f'Q2 (Calculado): {Q2}')
Q3 = dados.quantile(0.75)
print(f'Q3 (Calculado): {Q3}')
IQR = Q3 - Q1
print(f'IQR (Calculado): {IQR}')

ax = sns.boxplot(data=dados, orient='v', width=0.3, palette="Set2")

ax.set_title('Boxplot dos Minutos', fontsize=16)
ax.set_ylabel('Minutos', fontsize=12)

plt.show()
