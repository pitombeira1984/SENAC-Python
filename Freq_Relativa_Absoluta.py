
import pandas as pd

dados = {'idade':[22,21,23,22,24,21,22,25,23,22,24,23,22,21,24,25,23,22,24,23]}
df = pd.DataFrame(dados)

freq_abs = df['idade'].value_counts().sort_index()
print(freq_abs)

freq_rel = df['idade'].value_counts(normalize=True).sort_index() * 100
print(freq_rel)