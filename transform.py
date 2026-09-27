import pandas as pd
import json

def limpar_dados_fipe(caminho_entrada, caminho_saida):
    print(f"Carregando os dados: {caminho_entrada}...")
    # Ler JSON da extração
    with open(caminho_entrada, "r") as arquivo:
        dados = json.load(arquivo)

    df = pd.DataFrame(dados)

    print("Iniciando limpeza de dados...")
    # Remover R$
    df["Valor"] = df["Valor"].str.replace("R$", "")
    # Remover casa do milhar
    df["Valor"] = df["Valor"].str.replace(".", "")
    # Trocar vírgula centavos por ponto
    df["Valor"] = df["Valor"].str.replace(",", ".")
    # Converter string para float
    df["Valor"] = df["Valor"].astype(float)

    print(f"Salvando dados limpos na Camada Silver em {caminho_saida}...")
    df.to_csv(caminho_saida, index=False, sep=";")
    print("Sucesso! Transformação concluída.")


