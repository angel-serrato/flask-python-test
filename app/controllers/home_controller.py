from flask import render_template

class HomeController:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        @self.app.route('/')
        def index():
            return render_template("index.html")
        
        @self.app.route('/about')
        def about():
            return render_template("about.html")
        
        @self.app.route('/contact')
        def contact():
            return render_template("contact.html")
        
        @self.app.errorhandler(404)
        def page_not_found(e):
            return render_template("404.html"), 404