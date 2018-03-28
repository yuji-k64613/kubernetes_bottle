import os
import psycopg2
from bottle import route, run

@route("/")
def hello_world():
        host = os.environ['POSTGRES_SVC_PORT_5432_TCP_ADDR']
        DATABASE_URL = "postgresql://postgres:postgres@%s:/postgres" % host
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT * FROM person;")
        data = cur.fetchone()
        name1 = data[1]
        return "Hello World! " + str(name1);

run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
