from datetime import datetime
from typing import NewType, Optional
from peewee import Model, AutoField, TextField, IntegerField, PostgresqlDatabase


DATABASE = "ToDo"
USER = "postgres"
PASSWORD = "postgres"
HOST = "127.0.0.1"
PORT = 5432


class BaseModel(Model):
    class Meta:
        database = PostgresqlDatabase(database=DATABASE,
                                      user=USER,
                                      password=PASSWORD,
                                      host=HOST,
                                      port=PORT)


class Task(BaseModel):
    task_id = AutoField(column_name="id")
    summary = TextField(column_name="summary", null=False)
    priority = IntegerField(column_name="priority", null=False)

    class Meta:
        table_name = "tasks"


