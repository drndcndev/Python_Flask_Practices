from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

#Database Connection
DB_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:password@db:5432/flaskdb')


def get_db_connection():
    conn = psycopg2.connect(DB_URL)
    return conn

@app.route('/')
def Home():
    return "Hello from Flask with PostgreSQL & Docker Compose!"

@app.route('/users')
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)