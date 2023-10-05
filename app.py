import os

from flask import Flask

simple_app = Flask(__name__)

app_host = os.getenv("APP_HOST")
app_port = os.getenv("APP_PORT")


@simple_app.route("/")
def sayMyName():
    return "Hello there"


if __name__ == "__main__":
    simple_app.run(host=app_host, port=app_port)
