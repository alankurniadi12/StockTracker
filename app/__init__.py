import os
import logging
from flask import Flask, session
from app.routes import pages
from dotenv import load_dotenv
from pymongo import MongoClient
from app.auth.routes import auth
from app.utils import load_texts

load_dotenv()

# Atur level logging dan formatnya (hanya perlu dilakukan sekali, bisa di file utama aplikasi)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

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