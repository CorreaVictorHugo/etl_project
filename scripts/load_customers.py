# Este código se conecta a um banco de dados PostgreSQL, lê um arquivo CSV contendo dados de clientes, cria uma tabela "customers" no banco de dados (se ela não existir) e insere os dados do CSV nessa tabela. Por fim, ele fecha a conexão com o banco de dados.

import pandas as pd
import psycopg2

# ler o arquivo csv
df = pd.read_csv("C:/Users/Victor Hugo/Desktop/Incidium Academy/Módulo_08_Atividade_Pratica/data/customers.csv")

# conexão com banco destino
conn = psycopg2.connect(
    host="localhost",
    port=5434,
    database="postgres",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

# criar tabela no banco destino
create_table = """
CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT,
    company_name TEXT,
    contact_name TEXT,
    contact_title TEXT
);
"""

cursor.execute(create_table)

# inserir dados
for index, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO customers (customer_id, company_name, contact_name, contact_title)
        VALUES (%s, %s, %s, %s)
        """,
        (row["customer_id"], row["company_name"], row["contact_name"], row["contact_title"])
    )

conn.commit()

print("Dados carregados no banco de destino!")

cursor.close()
conn.close()