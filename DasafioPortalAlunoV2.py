import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('TabDesafio.csv')

print(df.describe().round(2))

#count → quantidade de valores não nulos
#mean → média
#std → desvio padrão
#min → valor mínimo
#25%, 50%, 75% → quartis
#max → valor máximo