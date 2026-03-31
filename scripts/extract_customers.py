import pandas as pd # Biblioteca usada para manipular dados em formato de tabela.
import psycopg2 #Biblioteca usada para conectar Python ao PostgreSQL

# parâmetros de conexão
host = "localhost"
port = 5433
database = "postgres"
user = "postgres"
password = "postgres"

# conexão com o banco
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

# consulta SQL
query = "SELECT * FROM customers" # Consulta SQL para selecionar todos os dados da tabela "customers".

# carregar dados em dataframe
df = pd.read_sql(query, conn)

# salvar arquivo local
df.to_csv("../data/customers.csv", index=False)

print("Arquivo customers.csv criado com sucesso!")

# fechar conexão
conn.close()