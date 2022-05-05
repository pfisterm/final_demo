

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.chores_routes import chores_routes

def create_app():
    app = Flask(__name__)
    app.secret_key = "super secret key"
    app.register_blueprint(home_routes)
    app.register_blueprint(chores_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)