from flask import current_app

class TextLoader:
    @staticmethod
    def get_text(key):
        return current_app.config['TEXTS']['forms'][key]

    @staticmethod
    def get_message(key):
        return current_app.config['TEXTS']['messages'][key]