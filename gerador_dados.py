import pandas as pd
import os

def inicializar_arquivos():
    # Dados iniciais de produtos
    produtos = pd.DataFrame({
        'id_produto': [1, 2, 3],
        'nome': ['Shampoo', 'Condicionador', 'Sabonete'],
        'preco': [25.00, 27.00, 5.60]
    })
    
    # Dados iniciais de clientes
    clientes = pd.DataFrame({
        'id_cliente': [101, 102, 103],
        'nome': ['Roberto Silva', 'Bruno Souza', 'Carla Dias'],
        'endereco': ['Rua Sibipiruna, 10', 'Av. dos Ipês, 20', 'Rua Campeche, 30']
    })
    
    produtos.to_csv('produtos.csv', index=False)
    clientes.to_csv('clientes.csv', index=False)
    print("✅ Arquivos CSV iniciais criados.")

def atualizar_dados():
    # Lendo arquivos atuais
    df_p = pd.read_csv('produtos.csv')
    df_c = pd.read_csv('clientes.csv')

    # 1. Alterar o preço de um produto 
    df_p.loc[df_p['id_produto'] == 2, 'preco'] = 29.00

    # 2. Mudar o endereço de um cliente 
    df_c.loc[df_c['id_cliente'] == 101, 'endereco'] = 'Alameda Nova, 500'

    # 3. Adicionar um cliente novo
    novo_cliente = pd.DataFrame({
        'id_cliente': [104],
        'nome': ['Diego Rock'],
        'endereco': ['Rua do Rock, 99']
    })
    df_c = pd.concat([df_c, novo_cliente], ignore_index=True)

    # Salvando as alterações
    df_p.to_csv('produtos.csv', index=False)
    df_c.to_csv('clientes.csv', index=False)
    print("🔄 Dados atualizados: Preço alterado, Endereço mudado e Novo cliente adicionado.")

if __name__ == "__main__":
    if not os.path.exists('produtos.csv'):
        inicializar_arquivos()
    else:
        atualizar_dados()
        

