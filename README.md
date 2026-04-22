# Pipeline de Dados com Staging e SCD Tipo 2

![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![Status](https://img.shields.io/badge/Status-Concluído-success)

---

## Visão Geral

Este projeto foi desenvolvido como exercício prático de aula para simular um pipeline de dados com:

- geração de arquivos CSV
- carga em banco SQLite
- uso de camada de staging
- atualização de dimensões
- controle de histórico com **SCD Tipo 2**

O objetivo é demonstrar, de forma simples, como funciona o fluxo de ingestão e versionamento de dados em um pequeno Data Warehouse local.

---

## Objetivo do Exercício

Construir um pipeline capaz de:

- gerar dados iniciais de produtos e clientes
- armazenar os dados em arquivos CSV
- carregar esses dados para uma camada de staging
- criar tabelas dimensionais no SQLite
- manter histórico de alterações de clientes com **Slowly Changing Dimension Type 2**

---

## Estrutura do Projeto

```bash
pipeline_m2s05/
│── banco_dados_local.py
│── gerador_dados.py
│── scd_2.py
│── staging.py
│── teste.py
│── .gitignore
```
## 📂 Descrição dos Arquivos

### `gerador_dados.py`
Gera os dados iniciais e simula alterações.

- Cria produtos e clientes
- Atualiza preço e endereço
- Adiciona novo cliente

---

### `banco_dados_local.py`
Cria o banco SQLite e as dimensões:

- `dim_produtos`
- `dim_clientes`

Controle de histórico:
- `is_current`
- `dt_inicio`

---

### `staging.py`
Carrega os CSVs para staging:

- `stg_produtos`
- `stg_clientes`

Carga com `replace` (sempre atualizada).

---

### `scd_2.py`
Implementa **SCD Tipo 2**:

- Desativa registros antigos (`is_current = 0`)
- Insere nova versão atualizada
- Mantém histórico de clientes

---

### `teste.py`
Executa o pipeline completo:

1. Cria banco
2. Gera dados
3. Carrega staging
4. Executa SCD2
5. Atualiza dados
6. Reprocessa pipeline
7. Mostra resultado final

---

## 🛠️ Tecnologias

- Python  
- Pandas  
- SQLite  

---

## 🧠 Conceitos

- ETL / ELT  
- Staging  
- Data Warehouse  
- SCD Tipo 2  
- Histórico de dados  

---

## 🚀 Como Executar

```bash
git clone https://github.com/natiruhling/pipeline_m2s05.git
cd pipeline_m2s05
pip install pandas
python teste.py
```

--- 

## ✅ Resultado Esperado

- Banco criado  
- Dados carregados  
- Alterações detectadas  
- Histórico preservado  
- Clientes com múltiplas versões  

---

## 📚 Aprendizados

- Organização de pipeline  
- Uso de staging  
- Aplicação de SCD Tipo 2  
- Versionamento de dados  

---

## 🔮 Melhorias Futuras

- requirements.txt  
- Logs  
- Automação do pipeline  
- Testes unitários  

---

## 👩‍💻 Autora

**Nathália Rühling Rocha**
