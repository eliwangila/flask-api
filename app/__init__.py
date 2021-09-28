from flask import Flask
from .auth.v2 import version_2_auth
from .auth.v2.models.db_models import Bball_Db
from app.config import app_config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    with app.app_context():
        Bball_Db.init_db(app.config.get('DB_NAME'),app.config.get('DB_HOST'),app.config.get('DB_PASSWORD'),app.config.get('DB_USER'))
        Bball_Db.build_tables()

    app.register_blueprint(version_2_auth)
    
    return app