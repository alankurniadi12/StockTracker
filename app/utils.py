import json
import os

def load_texts():
    with open(os.path.join(os.path.dirname(__file__), 'translations', 'texts.json'), 'r', encoding='utf-8') as f:
        texts = json.load(f)
    return texts