import requests

url_fipe = "https://brasilapi.com.br/api/fipe/marcas/v1/carros"

response = requests.get(url_fipe)
print("O status da conexão foi:", response.status_code)

