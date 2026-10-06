from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def show_message():
    print("This is my firts DAG in Airflow")
    print("The task executed successfully")

with DAG(
    dag_id="firt_dag_example",
    start_date= datetime(2026,1,1),
    schedule=None,
    catchup=False,
) as dag:

    message_task = PythonOperator(
        task_id= "show_message",
        python_callable= show_message,
    )













