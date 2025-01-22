from app.db import Database
from datetime import datetime

class User:
    def __init__(self, id=None, email=None, password=None, role_id=None, created_at=None, updated_at=None):
        self.id = id
        self.email = email
        self.password = password
        self.role_id = role_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def create_user(self, email, password, role_id=1):
        db = Database()
        db.cursor.execute("""INSERT INTO users (email, password, role_id) VALUES (%s, %s, %s) RETURNING id""", (email, password, role_id))
        user_id = db.cursor.fetchone()[0]
        db.connection.commit()
        db.close()
        return user_id

    def get_user_by_email(self, email):
        db = Database()
        query = "SELECT * FROM users WHERE email = %s"
        db.cursor.execute(query, (email,))
        user_data = db.cursor.fetchone()
        db.close()
        if user_data:
            return User(*user_data)
        return None

