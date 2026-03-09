import sqlite3
import pandas as pd
# Importando as funções dos seus arquivos agora renomeados
from gerador_dados import inicializar_arquivos, atualizar_dados
from banco_dados_local import criar_infraestrutura_dw
from staging import carregar_staging
from scd_2 import executar_scd_tipo2

def rodar_teste_completo():
    print("--- 🚀 INICIANDO TESTE DO PIPELINE END-TO-END ---")

    # 1. Setup do Banco
    # Certifique-se que o nome do banco aqui é o mesmo usado dentro dos seus outros scripts
    print("\n[1/5] Criando banco de dados e tabelas...")
    criar_infraestrutura_dw("meu_data_warehouse")

    # 2. Criar massa inicial
    print("[2/5] Gerando CSVs com 3 produtos e 3 clientes...")
    inicializar_arquivos()

    # 3. Primeira carga (Staging -> Dim)
    print("[3/5] Movendo dados iniciais para Staging e Dimensões...")
    carregar_staging()
    executar_scd_tipo2()

    print("\n--- 🛠 APLICANDO ALTERAÇÕES NOS ARQUIVOS ---")

    # 4. Alterar os CSVs (Onde a mágica do SCD-2 acontece)
    # Esta função deve mudar 1 preço, 1 endereço e adicionar 1 cliente novo
    atualizar_dados()

    # 5. Segunda carga (Sincronização)
    print("\n[4/5] Atualizando Staging com novos dados...")
    carregar_staging()
    
    print("[5/5] Executando lógica SCD Tipo 2 (Preservando histórico)...")
    executar_scd_tipo2()

    print("\n--- ✅ PIPELINE FINALIZADO COM SUCESSO ---")

    # Validação visual rápida
    try:
        conn = sqlite3.connect("meu_data_warehouse.db")
        print("\nVisualização da dim_clientes (Histórico):")
        df_final = pd.read_sql("SELECT * FROM dim_clientes ORDER BY id_cliente, dt_inicio", conn)
        print(df_final)
        conn.close()
    except Exception as e:
        print(f"Não foi possível exibir o resultado final: {e}")

if __name__ == "__main__":
    rodar_teste_completo()