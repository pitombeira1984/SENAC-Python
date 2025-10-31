import pandas as pd

salario = [2000, 2100, 2000, 2200, 2100, 15000]

df = pd.DataFrame(salario, columns=['Salario'])
#print(df.head())

#Calculando Mádia, Mediana e Moda
media = df['Salario'].mean().round(2)
mediana = df['Salario'].median()
moda = df['Salario'].mode().round(2)

#Imprimindo Tabela
tabela = pd.DataFrame({
    'Media':media,
    'Mediana':mediana,
    'Moda':moda
})
print(tabela)