from flask import flash, Blueprint, render_template, current_app, redirect, url_for
from werkzeug.utils import secure_filename
from app.forms import StockForm
from app.models import Stock, User
import os
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

        date = datetime.combine(form.date.data, datetime.now().time())

        image_paths = []
        if form.images.data:
            upload_folder = os.path.join(current_app.instance_path, 'photos')
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            for file in form.images.data:
                filename = secure_filename(file.filename)
                unique_filename = f"{uuid.uuid4().hex}_{filename}"
                file.save(os.path.join(upload_folder, unique_filename))
                image_paths.append(unique_filename)

        stock = Stock(
            _id = uuid.uuid4().hex,
            title = form.title.data,
            description = form.description.data,
            date = date,
            quantity = form.quantity.data,
            quantity_type = form.quantity_type.data,
            serial_number = form.serial_number.data,
            to_devision = form.to_devision.data,
            send_by = form.send_by.data,
            received_by = form.received_by.data,
            remark = form.remark.data,
            images = image_paths
        )
        current_app.db.stock.insert_one(stock.__dict__)
        return redirect(url_for(".index"))

    return render_template("new_stock.html", title="StockTracker - Tambah Barang", form=form)
