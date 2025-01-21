import psycopg2
from config import Config

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=Config.DB_HOST,
            database=Config.DB_DATABASE,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            port=Config.DB_PORT
        )
        self.cursor = self.connection.cursor()
    
    def close(self):
        self.cursor.close()
        self.connection.close()