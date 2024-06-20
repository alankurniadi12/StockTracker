from flask import flash, Blueprint, render_template, current_app, redirect, url_for
from app.forms import StockForm
from app.models import Stock, User
import uuid
from dataclasses import asdict
from datetime import datetime

pages = Blueprint(
    "pages", 
    __name__, 
    template_folder="templates", 
    static_folder="static"
)

@pages.route("/")
def index():
    return render_template("index.html", title="Stock Tracker")

@pages.route("/add", methods=["GET", "POST"])
def add_stock():
    form = StockForm()
    
    if form.validate_on_submit():
        stock = Stock(
            _id = uuid.uuid4().hex,
            title = form.title.data,
            description= form.description.data,
            # date= datetime.combine(form.date.data, datetime.min.time()),
            date=int(datetime.combine(form.date.data, datetime.min.time()).timestamp()),
            quantity= form.quantity.data,
            quantity_type= form.quantity_type.data,
            serial_number= form.serial_number,
            to_devision= form.to_devision.data,
            send_by= form.send_by.data,
            received_by= form.received_by.data,
            remark= form.remark.data
        )
        # asdict = as dictionory (convert dataclass menjadi format psangan nilai-kunci seperti data dari json)
        current_app.db.stock.insert_one(asdict(stock))
        return redirect(url_for(".detail_stock", _id=stock._id))

    return render_template("new_stock.html", title="StockTracker - Tambah Barang", form=form)
