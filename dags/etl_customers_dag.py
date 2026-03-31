from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2


def extract_customers():

    conn = psycopg2.connect(
        host="host.docker.internal",
        port=5433,
        database="postgres",
        user="postgres",
        password="postgres"
    )

    query = "SELECT * FROM customers"
    df = pd.read_sql(query, conn)

    df.to_csv("/usr/local/airflow/data/customers.csv", index=False)

    conn.close()

    print("Extração concluída")


def load_customers():

    df = pd.read_csv("/usr/local/airflow/data/customers.csv")

    conn = psycopg2.connect(
        host="host.docker.internal",
        port=5434,
        database="postgres",
        user="postgres",
        password="postgres"
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id TEXT,
        company_name TEXT,
        contact_name TEXT,
        contact_title TEXT
    )
    """)

    cursor.execute("DELETE FROM customers")

    for _, row in df.iterrows():
        cursor.execute("""
        INSERT INTO customers (customer_id, company_name, contact_name, contact_title)
        VALUES (%s,%s,%s,%s)
        """,
        (
            row["customer_id"],
            row["company_name"],
            row["contact_name"],
            row["contact_title"]
        ))

    conn.commit()

    cursor.close()
    conn.close()

    print("Carga concluída")


with DAG(
    dag_id="etl_customers_pipeline",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id="extract_customers",
        python_callable=extract_customers
    )

    load_task = PythonOperator(
        task_id="load_customers",
        python_callable=load_customers
    )

    extract_task >> load_task