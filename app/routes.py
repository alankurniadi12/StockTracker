from flask import flash, Blueprint, render_template, current_app, redirect, url_for, request
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
    page = request.args.get('page')
    return render_template("index.html", title="Stock Tracker")

@pages.route("/add", methods=["GET", "POST"])
def add_stock():
    page_type = request.args.get('type', 'incoming')
    form = StockForm(page_type=page_type)
    
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


        if page_type != 'incoming':
            stock = Stock(
            _id = uuid.uuid4().hex,
            is_in_coming = False,
            title = form.title.data,
            description = form.description.data,
            date = date,
            quantity = form.quantity.data,
            quantity_type = form.quantity_type.data,
            serial_number = form.serial_number.data,
            receivery = form.receivery.data,
            sender = form.sender.data,
            devision = form.devision.data,
            remark = form.remark.data,
            images = image_paths
            )
            current_app.db.stock.insert_one(stock.__dict__)
        else:
            stock = Stock(
            _id = uuid.uuid4().hex,
            is_in_coming = True,
            title = form.title.data,
            description = form.description.data,
            date = date,
            quantity = form.quantity.data,
            quantity_type = form.quantity_type.data,
            serial_number = form.serial_number.data,
            devision = form.devision.data,
            sender = form.sender.data,
            receivery = form.receivery.data,
            remark = form.remark.data,
            images = image_paths
            )
            current_app.db.stock.insert_one(stock.__dict__)

        return redirect(url_for(".index"))

    return render_template("add_stock.html", title="StockTracker - Tambah Barang", form=form, page_type=page_type)