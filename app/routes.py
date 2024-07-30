from flask import flash, Blueprint, render_template, current_app, redirect, url_for, request
from werkzeug.utils import secure_filename
from app.forms import StockForm
from app.models import Stock, User
import os
import uuid
from dataclasses import asdict
from datetime import datetime
import logging
import pymongo

pages = Blueprint(
    "pages", 
    __name__, 
    template_folder="templates", 
    static_folder="static"
)

@pages.route("/")
def index():
    page = request.args.get('page', 1, type= int)
    per_page = 3
    stock_collection = current_app.db.stock

    stocks = stock_collection.find().sort('date', pymongo.DESCENDING).skip((page - 1) * per_page).limit(per_page)
    total_stock = current_app.db.stock.count_documents({})

    return render_template(
        "index.html",
        title="Stock Tracker", 
        stocks= stocks,
        total_stock= total_stock,
        page= page,
        per_page= per_page
    )

@pages.route("/test_flash")
def test_flash():
    flash('Flash berhasil ditampilkan', 'message')
    return redirect(url_for(".index"))

@pages.route("/add", methods=["GET", "POST"])
def add_stock():
    page_type = request.args.get('type', 'incoming')
    form = StockForm(page_type=page_type)
    
    if form.validate_on_submit():
        date = datetime.combine(form.date.data, datetime.now().time())

        image_paths = []
        if form.images.data:
            upload_folder = os.path.join(current_app.root_path, 'static', 'media', 'images')
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            for file in form.images.data:
                filename = secure_filename(file.filename)
                unique_filename = f"{uuid.uuid4().hex}_{filename}"
                file.save(os.path.join(upload_folder, unique_filename))
                image_paths.append(unique_filename)

        stock_data = {
            "_id": uuid.uuid4().hex,
            "title": form.title.data,
            "description": form.description.data,
            "date": date,
            "quantity": form.quantity.data,
            "quantity_type": form.quantity_type.data,
            "serial_number": form.serial_number.data,
            "devision": form.devision.data,
            "sender": form.sender_text.data if page_type == 'incoming' else form.sender_select.data,
            "receivery": form.receivery_text.data if page_type != 'incoming' else form.receivery_select.data,
            "remark": form.remark.data,
            "images": image_paths,
            "is_in_coming": page_type == 'incoming'
        }

        try:
            current_app.db.stock.insert_one(stock_data)
            logging.debug("Stock data inserted successfully")
        except Exception as e:
            logging.error(f"Error inserting stock data into database: {e}")
            form.submit.errors.append("Error inserting data into database")
            return render_template("add_stock.html", title="StockTracker - Tambah Barang", form=form, page_type=page_type)

        return redirect(url_for(".index"))

    if form.errors:
        logging.debug("Form errors: %s", form.errors)

    return render_template("add_stock.html", title="StockTracker - Tambah Barang", form=form, page_type=page_type)


@pages.route("/stock/detail/<string:id>")
def stock_detail(id):
    logging.debug("ID at detail pege: %s", id)
    
    stock_detail = current_app.db.stock.find_one({"_id": id})
    logging.debug("Data get by ID: %s", stock_detail)
    return render_template("detail.html", stock=stock_detail)


@pages.route("/delete/detail/<string:id>")
def delete_stock(id):
    result_deleted = current_app.db.stock.delete_one({'_id': id})
    if result_deleted.deleted_count == 1:
        flash('Data berhasil dihapus')
        return redirect(url_for(".index"))
    else:
        flash('Data tidak berhasil dihapus', 'error')

    return redirect(url_for('pages.stock_detail', id = id))