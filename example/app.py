
from os import getenv
from flask import Flask, Response, request
from psycopg import Connection

app = Flask(__name__)

with open('index.html') as f:
    index_page = f.read()

print("I'm a new version!")

@app.route("/")
def index():
    return Response(index_page, mimetype="text/html")

@app.route("/livez")
def livez():
    return "ok"

def connect_pg():
    return Connection.connect(user=getenv("DB_USERNAME"), password=getenv("DB_PASSWORD"), host=getenv("DB_HOST"), port=getenv("DB_PORT"), dbname=getenv("DB_DATABASE"))

@app.route("/readyz")
def readyz():
    with connect_pg() as connection:
        with connection.cursor() as cur:
            cur.execute("SELECT 1")
            return "ok"

@app.route("/time")
def time():
    with connect_pg() as connection:
        with connection.cursor() as cur:
            cur.execute("SELECT now()")
            return f"current time: {cur.fetchone()[0]}"


@app.route("/config")
def config():
    print(request.headers)
    return {
        "issuer": getenv("AUTH_KEYCLOAK_ISSUER"),
        "clientId": getenv("AUTH_KEYCLOAK_ID"),
    }
