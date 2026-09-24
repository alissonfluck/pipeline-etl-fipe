import pandas as pd
import json

print("Carregando os dados do Data Lake...")
# Ler JSON da extração
with open("precos_fipe.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data)

print("Iniciando limpeza de dados...")
# Remover R$
df["Valor"] = df["Valor"].str.replace("R$", "")
# Remover casa do milhar
df["Valor"] = df["Valor"].str.replace(".", "")
# Trocar vírgula centavos por ponto
df["Valor"] = df["Valor"].str.replace(",", ".")
# Converter string para float
df["Valor"] = df["Valor"].astype(float)

print("Visualizando as primeiras linhas após a limpeza:")
print(df.head())

print("\nSalvando em CSV...")
df.to_csv("data/fipe_dados_limpos.csv", index=False, sep=";")
print("Pipeline concluído! Arquivo fipe_dados_limpos.csv gerado.")

