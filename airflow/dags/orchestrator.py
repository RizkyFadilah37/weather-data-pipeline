from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

sys.path.append('/opt/airflow/api-request')

def insert_weather_data():
    from insert_records import main
    main()

default_args = {
    'description': 'DAG to orchestrate weather data insertion',
    'start_date': datetime(2025, 1, 1),
    'catchup': False,
}

dag = DAG(
    'test_orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=1)
)

with dag:
    task1 = PythonOperator(
        task_id='insert_weather_data',
        python_callable=insert_weather_data
    )