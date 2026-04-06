from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from scripts.kafka_producer import stream_kafka

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
}

with DAG('dag_auto_stream_data',
         default_args=default_args,
         start_date=datetime(2026, 1, 1),
         schedule_interval='@daily',
         catchup=False,
         tags=['streaming']) as dag:
    
    stream_data_task = PythonOperator(
        task_id='stream_data_event_game',
        python_callable=stream_kafka
    )