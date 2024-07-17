from flask_wtf import FlaskForm
from flask import current_app, request
from wtforms import (
    IntegerField, 
    StringField, 
    SubmitField, 
    DateField, 
    SelectField, 
    TextAreaField, 
    validators
)
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf.file import FileAllowed, MultipleFileField
from datetime import datetime
from .text_loaders import TextLoader

class StockForm(FlaskForm):
    title = StringField(validators=[])
    description = TextAreaField(validators=[Length(max=1000)])
    date = DateField(format='%Y-%m-%d', default=datetime.today )
    quantity = IntegerField(validators=[])
    quantity_type = SelectField(choices=[('set', 'Set'), ('ea', 'Ea'), ('roll', 'Roll')])
    serial_number = StringField()
    devision = SelectField(choices=[('ict', 'ICT'), ('radio-room', 'Radio Room'), ('csr', 'CSR')])
    sender_text = StringField()
    sender_select = SelectField(choices=[('irwan', 'Irwan'), ('suhendri', 'Suhendri')])
    receivery_select = SelectField(choices=[('irwan', 'Irwan'), ('suhendri', 'Suhendri')])
    receivery_text = StringField()
    remark = TextAreaField([validators.Length(max=500)])
    images = MultipleFileField(validators=[])
    submit = SubmitField()

    def __init__(self, page_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title.label.text = TextLoader.get_text('item_name')
        self.title.validators = [DataRequired(message=TextLoader.get_message('item_name_required'))]

        self.description.label.text = TextLoader.get_text('description')
        self.date.label.text = TextLoader.get_text('date')
        self.quantity.label.text = TextLoader.get_text('quantity')
        self.quantity.validators = [DataRequired(message=TextLoader.get_message('quantity_required'))]

        self.quantity_type.label.text = TextLoader.get_text('quantity_type')
        self.serial_number.label.text = TextLoader.get_text('serial_number')

        if page_type == 'incoming':
            self.devision.label.text = TextLoader.get_text('sending_division')
            self.sender_text.label.text = TextLoader.get_text('sender')
            self.sender_text.validators = [DataRequired(message=TextLoader.get_message('send_by_required'))]
            self.receivery_select.label.text = TextLoader.get_text('receiver')
        else:
            self.sender_select.label.text = TextLoader.get_text('sender')
            self.devision.label.text = TextLoader.get_text('receiving_division')
            self.receivery_text.label.text = TextLoader.get_text('receiver')
            self.receivery_text.validators = [DataRequired(message=TextLoader.get_message('send_by_required_outgoing'))]
            

        self.remark.label.text = TextLoader.get_text('remark')
        self.images.label.text = TextLoader.get_text('images')
        self.images.validators = [DataRequired(message=TextLoader.get_message('images_required'))]
        self.submit.label.text = TextLoader.get_text('submit')