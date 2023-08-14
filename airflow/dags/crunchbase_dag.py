import os

from airflow import DAG
from airflow.decorators import task
from airflow.models import Variable

from datetime import datetime
from roles import api_requests, database

crunchbase_api_key = Variable.get('crunchbase_api_key')


with DAG(
    dag_id="crunchbase_ingestion",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["API", "Ingestion"],
) as dag:
    @task(task_id='fetch_data')
    def fetch_data():
        return api_requests.request_organization(organization_id='konsus', crunchbase_api_key=crunchbase_api_key)
    
    @task(task_id='write_data')
    def write_data(data):
        database.write(data, path='/opt/airflow/logs/airflow_output.parquet')
    
    data = fetch_data()
    write_data(data)
