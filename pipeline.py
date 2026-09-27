from extract import extrair_dados_fipe
from transform import limpar_dados_fipe
from load import carregar_sqlite

# Parâmetros
ARQUIVO_MODELOS = "data/modelos_fipe.json"
ARQUIVO_JSON = "data/precos_fipe.json"
ARQUIVO_CSV = "data/precos_limpos.csv"
BANCO_DADOS = "data/fipe_banco.db"

if __name__ == "__main__":
    print("=== INÍCIO DO PIPELINE ETL ===")

    # Extract
    extrair_dados_fipe(ARQUIVO_MODELOS, ARQUIVO_JSON)

    # Transform
    limpar_dados_fipe(ARQUIVO_JSON, ARQUIVO_CSV)

    # Load
    carregar_sqlite(ARQUIVO_CSV, BANCO_DADOS)

    print("=== PIPELINE FINALIZADO COM SUCESSO! ===")