import json
import time
import requests

def extrair_dados_fipe(caminho_modelos, caminho_precos, limite_modelos=50):
    print(f"Carregando os modelos de: {caminho_modelos}...")
    with open(caminho_modelos, "r") as arquivo:
        catalogo = json.load(arquivo)

    precos_atuais = []

    print("Iniciando extração...\n")
    for montadora in catalogo:
        codigo_marca = montadora["codigo_marca"]
        nome_montadora = montadora["marca"]
        print(f"\n=== Processando frota da {nome_montadora} ===")

        # Fatiamento
        modelos_amostra = montadora["modelos"][:limite_modelos]

        for modelo in modelos_amostra:
            codigo_modelo = modelo["codigo"]
            nome_modelo = modelo["nome"]

            try:
                url_anos = f"https://fipe.parallelum.com.br/api/v2/cars/brands/{codigo_marca}/models/{codigo_modelo}/years"
                resp_anos = requests.get(url_anos)

                if resp_anos.status_code == 200:
                    anos = resp_anos.json()

                    if len(anos) > 0:
                        codigo_ano_recente = anos[0]["code"]
                        time.sleep(1)

                        url_preco = f"https://fipe.parallelum.com.br/api/v2/cars/brands/{codigo_marca}/models/{codigo_modelo}/years/{codigo_ano_recente}"
                        resp_preco = requests.get(url_preco)

                        
                        if resp_preco.status_code == 200:
                            dados_preco = resp_preco.json()
                            precos_atuais.append(dados_preco)
                            print(f"Extraído: {nome_modelo} - {dados_preco['price']}")
                        else:
                            print(f"[ERRO] Código: {resp_preco.status_code}")
            except Exception as error:
                print(f"Falha no modelo {nome_modelo}. Motivo: {error}")
                
            time.sleep(2)

    print(f"\nSalvando a base de preços em: {caminho_precos}")
    with open(caminho_precos, "w") as arquivo_final:
        json.dump(precos_atuais, arquivo_final, indent=4)
    print("Sucesso! Extração concluída.")
