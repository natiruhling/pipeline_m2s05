import sqlite3
from datetime import datetime

def executar_scd_tipo2(nome_banco="meu_data_warehouse.db"):
    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()
    data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"--- Iniciando Processamento SCD Tipo 2: {data_atual} ---")

    try:
        # 1. Identificar Mudanças e "Fechar" (UPDATE) os registros antigos
        # Procuramos clientes que estão na STG com endereço DIFERENTE da DIM onde is_current é True
        cursor.execute("""
            UPDATE dim_clientes
            SET is_current = 0
            WHERE id_cliente IN (
                SELECT stg.id_cliente
                FROM stg_clientes stg
                JOIN dim_clientes dim ON stg.id_cliente = dim.id_cliente
                WHERE dim.is_current = 1 
                  AND stg.endereco <> dim.endereco
            )
            AND is_current = 1
        """)
        print(f"✅ {cursor.rowcount} registros antigos foram desativados (is_current = 0).")

        # 2. Inserir Novos Registros (INSERT) para mudanças e novos clientes
        # Usamos um LEFT JOIN para encontrar quem não existe ou quem acabou de ser desativado
        cursor.execute("""
            INSERT INTO dim_clientes (id_cliente, nome, endereco, is_current, dt_inicio)
            SELECT 
                stg.id_cliente, 
                stg.nome, 
                stg.endereco, 
                1 as is_current, 
                ? as dt_inicio
            FROM stg_clientes stg
            LEFT JOIN dim_clientes dim 
                ON stg.id_cliente = dim.id_cliente 
                AND dim.is_current = 1
            WHERE dim.id_cliente IS NULL
        """, (data_atual,))
        print(f"✅ {cursor.rowcount} novos registros (novos clientes ou novos endereços) inseridos.")

        conn.commit()

    except Exception as e:
        print(f"❌ Erro no processamento SCD: {e}")
        conn.rollback()
    
    finally:
        conn.close()
        print("--- Processamento Concluído ---")

if __name__ == "__main__":
    executar_scd_tipo2()