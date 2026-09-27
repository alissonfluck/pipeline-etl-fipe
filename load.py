import pandas as pd 
import sqlite3

def carregar_sqlite(caminho_csv, caminho_banco):
    print(f"Lendo os dados limpos de {caminho_csv}...")
    df = pd.read_csv(caminho_csv, sep=";")

    print("Conectando ao Banco de Dados...")
    conexao = sqlite3.connect(caminho_banco)

    print("Executando a carga...")
    df.to_sql("precos_atuais", conexao, if_exists="replace", index=False)

    conexao.close()
    print("Sucesso! Carga concluída.")

    