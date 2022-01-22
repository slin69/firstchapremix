from flask import *
from .views import *
from flask_socketio import *

def create_app():
    app=Flask(__name__)
    app.config["SECRET_KEY"]="shit"
    
    app.register_blueprint(views.bp)


    return app