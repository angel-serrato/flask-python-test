from flask import Flask
from app.db import Database
from app.controllers.home_controller import HomeController
from app.controllers.auth_controller import auth_bp

def create_app():
    app = Flask(__name__)
    db = Database()
    db.create_tables()
    HomeController(app)
    app.register_blueprint(auth_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
