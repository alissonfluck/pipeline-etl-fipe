import requests
import json

url_fipe = "https://brasilapi.com.br/api/fipe/marcas/v1/carros"

response = requests.get(url_fipe)

if response.status_code == 200:
    print("Conexão bem-sucedida! Extraindo dados...")

    data = response.json()

    with open("data/marcas_fipe.json", "w") as arquivo:
        json.dump(data, arquivo, indent=4)

    print("Ingestão concluída! Arquivo marcas_fipe.json gerado.")
else:
    print(f"Erro na requisição. Status: {response.status_code}")

