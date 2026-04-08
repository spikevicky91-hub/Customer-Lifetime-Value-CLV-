from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.pipeline import transform

with DAG('clv_pipeline',
         start_date=datetime(2024,1,1),
         schedule_interval='@daily',
         catchup=False) as dag:

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform
    )
