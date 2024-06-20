from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, DateField
from wtforms.validators import DataRequired, InputRequired

class StockForm(FlaskForm):
    title = StringField("Nama Barang", validators=[DataRequired(message= "Tidak boleh kosong")])
    description = StringField("Keterangan")
    date = DateField("Tanggal", format='%Y-%m-%d', validators=[DataRequired()])
    quantity = IntegerField("Jumlah", validators=[DataRequired(message="Tidak boleh kosong")])
    quantity_type = StringField("Satuan")
    serial_number = StringField("Nomor Seri")
    to_devision = StringField("Devisi")
    send_by = StringField("Nama Pengirim")
    received_by = StringField("Nama Penerima")
    remark = StringField("Komentar")
    
    submit = SubmitField("Simpan")