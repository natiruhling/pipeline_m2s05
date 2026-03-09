import pandas as pd
import sqlite3
from datetime import datetime

def criar_infraestrutura_dw(nome_banco="loja_dw"):
    """
    Cria o banco de dados local e as tabelas dim_produtos e dim_clientes.
    """
    nome_arquivo = f"{nome_banco}.db"
    
    # 1. Conectar ao banco de dados (será criado se não existir)
    conn = sqlite3.connect(nome_arquivo)
    cursor = conn.cursor()

    print(f"--- Iniciando configuração do banco: {nome_arquivo} ---")

    # 2. Criar a tabela dim_produtos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dim_produtos (
        id_produto INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )
    """)
    print("Tabela 'dim_produtos' criada com sucesso.")

    # 3. Criar a tabela dim_clientes (com colunas de controle de versão)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dim_clientes (
        id_cliente INTEGER,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL,
        is_current BOOLEAN,
        dt_inicio TEXT,
        PRIMARY KEY (id_cliente, dt_inicio)
    )
    """)
    print("Tabela 'dim_clientes' criada com sucesso.")

    # Confirmar alterações e fechar conexão
    conn.commit()
    conn.close()
    print("--- Infraestrutura pronta para receber dados ---")

if __name__ == "__main__":
    # Você pode definir o [NOME] que desejar aqui
    nome_do_banco = "meu_data_warehouse"
    criar_infraestrutura_dw(nome_do_banco)