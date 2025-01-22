import psycopg2
from app.config import Config

class Database:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host=Config.DB_HOST,
                database=Config.DB_DATABASE,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                port=Config.DB_PORT
            )
            self.cursor = self.connection.cursor()
            print("Connection successful")
        except psycopg2.Error as e:
            print(f"Error: {e}")
            self.connection = None
            self.cursor = None

    def close(self):
        self.cursor.close()
        self.connection.close()

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS roles (id SERIAL PRIMARY KEY, email VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email VARCHAR(255) UNIQUE NOT NULL, password VARCHAR(255) NOT NULL, role_id INTEGER NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updatet_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (role_id) REFERENCES roles(id))""")
        self.connection.commit()
        self.cursor.close()
        self.close()
