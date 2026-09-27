import pandas as pd 
import sqlite3

print("Lendo os dados limpos...")
df = pd.read_csv("data/precos_limpos.csv", sep=";")

print("Conectando ao Banco de Dados...")
conexao = sqlite3.connect("data/fipe_banco.db")

print("Executando a carga...")
df.to_sql("precos_atuais", conexao, if_exists="replace", index=False)

conexao.close()
print("Sucesso! Carga concluída.")