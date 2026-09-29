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
    df["price"] = df["price"].str.replace("R$", "")
    # Remover casa do milhar
    df["price"] = df["price"].str.replace(".", "")
    # Trocar vírgula centavos por ponto
    df["price"] = df["price"].str.replace(",", ".")
    # Converter string para float
    df["price"] = df["price"].astype(float)
    # Padronizando nomes das marcas
    df['Brand'] = df['Brand'].str.capitalize()
    df['Model'] = df['Model'].str.capitalize()

    # Enriquecimento
    dicionario_tipos_veiculo = {1: "Carro", 2: "Moto", 3: "Caminhão"}
    df["vehicleType"] = df["vehicleType"].replace(dicionario_tipos_veiculo)

    print(f"Salvando dados limpos na Camada Silver em {caminho_saida}...")
    df.to_csv(caminho_saida, index=False, sep=";")
    print("Sucesso! Transformação concluída.")




