import pandas as pd
import json

print("Carregando os dados do Data Lake...")
# Ler JSON da extração
with open("data/precos_fipe.json", "r") as file:
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

print("Salvando dados limpos na Camada Silver...")
df.to_csv("data/precos_limpos.csv", index=False, sep=";")
print("Sucesso! Transformação concluída.")


