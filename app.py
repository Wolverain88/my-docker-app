import os
import psycopg2
from flask import Flask

app = Flask(__name__)

DB_HOST = "db"
DB_NAME = "mydatabase"
DB_USER = "myuser"
DB_PASS = "mypassword"

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST
        )
        return "✅ Подключение к базе данных успешно!"
    except Exception as e:
        return f"❌ Ошибка подключения: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
