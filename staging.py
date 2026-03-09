import pandas as pd
import sqlite3

def carregar_staging(nome_banco="meu_data_warehouse.db"):
    """
    Lê os CSVs e os carrega para tabelas de Staging (stg_) no SQLite.
    O modo 'replace' garante que a Staging seja sempre um reflexo fiel e limpo 
    do arquivo mais recente.
    """
    try:
        # 1. Conexão com o banco
        conn = sqlite3.connect(nome_banco)
        
        print("--- Iniciando Carga para Staging Area ---")

        # 2. Carregar Produtos para stg_produtos
        df_produtos = pd.read_csv('produtos.csv')
        df_produtos.to_sql('stg_produtos', conn, if_exists='replace', index=False)
        print(f"✔️ {len(df_produtos)} registros movidos para 'stg_produtos'.")

        # 3. Carregar Clientes para stg_clientes
        df_clientes = pd.read_csv('clientes.csv')
        df_clientes.to_sql('stg_clientes', conn, if_exists='replace', index=False)
        print(f"✔️ {len(df_clientes)} registros movidos para 'stg_clientes'.")

        # 4. Validação rápida (Verificar as colunas criadas)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'stg_%'")
        tabelas = cursor.fetchall()
        
        print(f"\nCamada de Staging atualizada: {[t[0] for t in tabelas]}")
        
        conn.close()
        print("--- Ingestão em Staging Concluída ---")

    except Exception as e:
        print(f"❌ Erro ao carregar Staging: {e}")

if __name__ == "__main__":
    carregar_staging()