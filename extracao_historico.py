import requests
import json
import time

codigo_marca = "1"
codigo_modelo = "1"

print(f"Buscando todos os anos disponíveis para o modelo {codigo_modelo}...")

url_anos = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos"
response_anos = requests.get(url_anos)

historico_precos = []

if response_anos.status_code == 200:
    lista_anos = response_anos.json()
    print(f"Encontrados {len(lista_anos)} anos diferentes. Iniciando extração...")

    for ano in lista_anos:
        codigo_ano = ano["codigo"]
        print(f"Buscando valor para o ano de referência: {codigo_ano}")

        url_valor = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos/{codigo_ano}"
        response_valor = requests.get(url_valor)

        if response_valor.status_code == 200:
            dados_ano = response_valor.json()
            historico_precos.append(dados_ano)

            time.sleep(1)

print("\nSalvando no Data Lake...")

with open("data/historico_depreciacao.json", "w") as file:
    json.dump(historico_precos, file, indent=4)

print("Sucesso! Histórico extraído.")
