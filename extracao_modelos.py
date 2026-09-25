import requests
import json
import time

print("Lendo o Data Lake local...")

with open("data/marcas_fipe.json", "r") as file:
    lista_marcas = json.load(file)

todos_modelos = []

marcas_alvo = ["21", "22", "23", "59"]


print("Iniciando a extração em escala (Modelos Fiat, Ford, GM e VolksWagen)...")
for marca in lista_marcas:
    codigo_marca = marca["valor"]

    if codigo_marca in marcas_alvo:
        nome_marca = marca["nome"]
        print(f"Buscando portfólio completo da marca: {nome_marca}")

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
with open("data/modelos_fipe.json", "w") as arquivo_final:
    json.dump(todos_modelos, arquivo_final, indent=4)

print("Sucesso! Extração concluída.")