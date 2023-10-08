import os

import psycopg2
from flask import Flask

simple_app = Flask(__name__)

app_host = os.getenv("APP_HOST")
app_port = os.getenv("APP_PORT")

db_host = os.getenv("POSTGRES_HOST")
db_name = os.getenv("POSTGRES_DB")
db_user = os.getenv("POSTGRES_USER")


def db_connection():
    try:
        db_connection = psycopg2.connect(host=db_host, user=db_user, dbname=db_name)
        return db_connection
    except (Exception, psycopg2.Error) as error:
        print("Error:", error)
        return False


@simple_app.route("/")
def sayMyName():
    return "Hello there"


if __name__ == "__main__":
    simple_app.run(host=app_host, port=app_port)
