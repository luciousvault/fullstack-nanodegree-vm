#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalog_db_setup import Base, Category, Item


app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog')
def showCatalog():
    categories = session.query(Category).all()
    return render_template('category_root.html', categories=categories)


@app.route('/catalog/add_item')
def newItem():
    return "This page is the add item page"


@app.route('/catalog/add_category', methods=['GET', 'POST'])
def newCatagory():
    if request.method == 'POST':
        newCat = Category(name=request.form['name'])
        session.add(newCat)
        session.commit()
        flash("new category created")
        return redirect(url_for('showCatalog'));
    else:
        return render_template('newcategory.html')


@app.route('/catalog/<category_id>/items')
def catagoryItems(category_id):
    return "This page should is the category items list"


@app.route('/catalog/<category_id>/<item_title>')
def showItem(category_id, item_title):
    return "This page displays an item with discription"


@app.route('/catalog/<category_id>/<item_title>/edit')
def editItem(category_id, item_title):
    return "This page is for editing an item"


@app.route('/catalog/<category_id>/<item_title>/delete')
def deleteItem(category_id, item_title):
    return "This page is for deleting an item"

# start api endpoints
@app.route('/catalog.json')
def catalogJSON():
    return "Implement and return jsonify of catalog."


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)