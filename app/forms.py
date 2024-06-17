from flask import FlaskForm
from wtforms import IntegerField, StringField, SubmitField

class StockForm(FlaskForm):
    title = StringField("Title")
    description = StringField("Description")