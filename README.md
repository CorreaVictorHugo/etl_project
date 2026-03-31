Pipeline ETL com Apache Airflow, Python e PostgreSQL

📌 Sobre o projeto

Este projeto tem como objetivo demonstrar, na prática, a construção de um pipeline de dados simples utilizando Python, PostgreSQL e Apache Airflow.

O fluxo implementado segue o processo de ETL (Extract, Transform, Load), onde os dados são extraídos de um banco de origem, armazenados em um arquivo intermediário e carregados em um banco de destino, com toda a execução orquestrada pelo Airflow.

🎯 Objetivo

Simular um cenário real de engenharia de dados, automatizando o fluxo de dados entre dois bancos PostgreSQL e garantindo:
execução ordenada das tarefas
controle de dependências
monitoramento do pipeline
reprocessamento em caso de falhas

⚙️ Tecnologias utilizadas

Python
PostgreSQL
Apache Airflow
Docker / Docker Compose
Astronomer CLI
Pandas
Psycopg2

🧠 Arquitetura do projeto

PostgreSQL (source_db)
        ↓
Extração (Python)
        ↓
Arquivo CSV
        ↓
Carga (Python)
        ↓
PostgreSQL (target_db)
        ↓
Orquestração (Airflow)

📁 Estrutura do projeto

etl_project/

│
├── dags/
│   └── etl_customers_dag.py
│
├── scripts/
│   ├── extract_customers.py
│   └── load_customers.py
│
├── data/
│   └── customers.csv
│
├── docker-compose.yml
├── requirements.txt
└── northwind.sql

🔄 Fluxo do pipeline

O pipeline é composto por duas tarefas principais:
extract_customers → load_customers

extract_customers: extrai dados da tabela customers do banco de origem e gera um arquivo CSV
load_customers: lê o CSV e insere os dados no banco de destino

▶️ Como executar o projeto

1. Subir os bancos PostgreSQL   
docker compose up -d

2. Importar base Northwind
Abrir o DBeaver
Conectar em localhost:5433
Executar o arquivo northwind.sql

3. Rodar ETL manual (opcional)
python scripts/extract_customers.py
python scripts/load_customers.py

4. Subir o Airflow
astro dev start

Acessar:
http://localhost:8080

Login:
admin / admin

5. Executar a DAG
   
Ativar etl_customers_pipeline
Clicar em Trigger DAG
Acompanhar execução em Graph


📊 Resultado esperado

Dados extraídos do banco de origem
Arquivo CSV gerado
Dados carregados no banco de destino
Execução controlada pelo Airflow


🧩 O que é o Apache Airflow

O Apache Airflow é uma ferramenta de orquestração de workflows que permite definir, agendar e monitorar pipelines de dados.
Neste projeto, ele foi responsável por:
organizar a execução das tarefas
garantir a ordem correta do fluxo
registrar logs
permitir monitoramento e reexecução

📸 Evidências do projeto
Execução da DAG com sucesso no Airflow
Dados carregados no banco PostgreSQL
Pipeline visual representado na interface


📚 Aprendizados

construção de pipelines ETL
integração Python + PostgreSQL
uso de Docker para ambientes isolados
orquestração com Apache Airflow
estruturação de projetos de dados


🏁 Conclusão

Este projeto demonstra, de forma prática, como construir um pipeline de dados automatizado, aplicando conceitos fundamentais de engenharia de dados.
Mesmo sendo um projeto simples, ele representa um fluxo real utilizado em ambientes profissionais, servindo como base para soluções mais complexas.
