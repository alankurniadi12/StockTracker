from flask_wtf import FlaskForm
from flask import current_app
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

def get_text(key):
    return current_app.config['TEXTS']['forms'][key]
class StockForm(FlaskForm):

    title = StringField("Nama Barang", validators=[DataRequired(message= "Nama barang tidak boleh kosong")])
    description = TextAreaField("Keterangan", [validators.Length(max=1000)])
    date = DateField("Tanggal", format='%Y-%m-%d', default=datetime.today )
    quantity = IntegerField("Jumlah", validators=[DataRequired(message="Tentukan jumlah barang")])
    quantity_type = SelectField("Satuan", choices=[('set', 'Set'), ('ea', 'Ea'), ('roll', 'Roll')])
    serial_number = StringField("Nomor Seri")
    send_by = StringField("Nama Pengirim", validators=[DataRequired(message="Nama pengirim tidak boleh kosong")])
    received_by = StringField("Nama Penerima", validators=[DataRequired(message="Nama penerima tidak boleh kosong")])
    to_devision = SelectField("Divisi Penerima", choices=[('ict', 'ICT'), ('radio-room', 'Radio Room'), ('csr', 'CSR')])
    remark = TextAreaField("Komentar", [validators.Length(max=500)])
    images = MultipleFileField("Gambar Barang", validators=[DataRequired(message="Masukan gambar jpg/jpeg/png mininal 1 file")])
    
    submit = SubmitField("Simpan")