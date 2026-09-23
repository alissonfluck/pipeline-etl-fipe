import requests
import json
import time

print("Lendo o Data Lake local...")

with open("marcas_fipe.json", "r") as file:
    lista_marcas = json.load(file)

todos_modelos = []


print("Iniciando a extração da segunda camada (Modelos)...")
for marca in lista_marcas[:3]:
    codigo_marca = marca["valor"]
    nome_marca = marca["nome"]

    print(f"Buscando modelos da marca: {nome_marca}")

    url_modelos = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos"
    response = requests.get(url_modelos)

    if response.status_code == 200:
        dados_modelo = response.json()

        todos_modelos.append({
            "codigo_marca": codigo_marca,
            "marca": nome_marca,
            "modelos": dados_modelo["modelos"]
        })
    else:
        print(f"Erro na marca {nome_marca}. Status: {response.status_code}")

    time.sleep(1)


print("\nSalvando os dados consolidados...")
with open("modelos_fipe.json", "w") as arquivo_final:
    json.dump(todos_modelos, arquivo_final, indent=4)

print("Sucesso! Arquivo modelos_fipe.json gerado localmente.")