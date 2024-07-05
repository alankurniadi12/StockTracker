import os
from flask import Flask
from app.routes import pages
from dotenv import load_dotenv
from pymongo import MongoClient
from app.auth.routes import auth
from app.utils import load_texts

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.db = MongoClient(app.config["MONGODB_URI"]).get_default_database()

    texts = load_texts()
    app.config['TEXTS'] = texts

    # Suapaya bisa panggil texts kedalam html
    @app.context_processor
    def inject_text():
        return dict(texts=texts)
    
    app.register_blueprint(pages)
    app.register_blueprint(auth, url_prefix='/auth')
    return app