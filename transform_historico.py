import pandas as pd
import json

print("Carregando o histórico do Data Lake...")
with open("data/historico_depreciacao.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data)

print("Iniciando a limpeza...")

# Remover R$
df["Valor"] = df["Valor"].str.replace("R$", "")
# Remover casa do milhar
df["Valor"] = df["Valor"].str.replace(".", "")
# Trocar vírgula centavos por ponto
df["Valor"] = df["Valor"].str.replace(",", ".")
# Converter string para float
df["Valor"] = df["Valor"].astype(float)

print("Visualizando os dados históricos limpos:")
print(df.head())

print("Salvando em CSV...")
df.to_csv("data/historico_limpo.csv", index=False, sep=";")

print("Secesso! Histórico pronto para análise.")