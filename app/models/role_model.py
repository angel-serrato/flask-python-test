from app.db import Database

class Role:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def get_all_roles():
        db = Database()
        db.cursor.execute("SELECT * FROM roles")
        roles = db.cursor.fetchall()
        db.close()
        return roles        
