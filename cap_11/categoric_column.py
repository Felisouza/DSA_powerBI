import pandas as pd

df = pd.read_csv(r'C:\Users\feh_s\DSA_powerBI\DSA_powerBI\cap_11\data\dados_pacientes.csv')


df['estado_civil_n'] = pd.factorize(df['estado_civil'])[0] + 1
df['tipo_sanguineo_n'] = pd.factorize(df['tipo_sanguineo'])[0] + 1

# Exibindo o DataFrame após a transformação
df.to_csv(r'C:\Users\feh_s\DSA_powerBI\DSA_powerBI\cap_11\data\dados_pacientes.csv')
print(df)
