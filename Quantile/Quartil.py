import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dias = [5, 6, 2, 8, 7, 20, 9, 6, 4]
df = pd.DataFrame({'Dias':dias})
print(df)


q1 = df['Dias'].quantile(0.25)
#print(f"Primeiro Quartil: {q1}")

q2 = df['Dias'].quantile(0.5)
#print(f"Segundo Quartil(Mediana): {q2}")

q3 = df['Dias'].quantile(0.75)
#print(f"Terceiro Quartil: {q3}")

resultado = pd.DataFrame([{
    "Primeiro Quartil":q1,
    "Segundo Quartil(Mediana)":q2,
    "Terceiro Quartil":q3
}])

print(resultado)

plt.figure(figsize=(8,6))
sns.set_theme(style="whitegrid")
ax = sns.boxenplot(data=df, orient='v', width=0.4, palette='Spectral')

ax.set_title('Boxplot dos minutos', fontsize=16)
ax.set_ylabel('Minutos', fontsize=12)
plt.show()