import json
import requests
import time

print("Carregando os modelos do Data Lake...")
with open("modelos_fipe.json", "r") as file:
    dados_modelos = json.load(file)

frota_atual = []

print("Inicinado extração de preços mais recentes...\n")
for marca in dados_modelos[:2]:
    codigo_marca = marca["codigo_marca"]
    nome_marca = marca["marca"]
    print(f"=== Explorando a marca: {nome_marca} ===")

    for modelo in marca["modelos"][:3]:
        codigo_modelo = modelo["codigo"]

        # Anos disponíveis para esse carro
        url_anos = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos"
        resp_anos = requests.get(url_anos)

        if resp_anos.status_code == 200:
            lista_anos = resp_anos.json()
            codigo_anos = lista_anos[0]["codigo"]

            url_valor = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos/{codigo_anos}"
            resp_valor = requests.get(url_valor)

            if resp_valor.status_code == 200:
                dados_veiculo = resp_valor.json()
                frota_atual.append(dados_veiculo)

            time.sleep(1)

print("\nSalvando dados...")
with open("data/precos_fipe.json", "w") as final_file:
    json.dump(frota_atual, final_file, indent=4)

print("Sucesso! Arquivo precos_fipe.json gerado.")
