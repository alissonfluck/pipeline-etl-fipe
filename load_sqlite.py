import pandas as pd
import sqlite3

print("Conectando ao Banco de Dados SQLite...")
conexao = sqlite3.connect("data/fipe_banco.db")

print("Lendo os dados limpos do Data Lake...")
df = pd.read_csv("data/fipe_dados_limpos.csv", sep=";")

print("Carregando os dados para a tabela o Banco de Dados SQLite...")
df.to_sql("precos_atuais", conexao, if_exists="replace", index=False)

print("Fechando a coenxão com o banco de dados...")
conexao.close()

print("Sucesso! Banco de dados fipe_banco.db criado.")

