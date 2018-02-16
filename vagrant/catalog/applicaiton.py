#!/usr/bin/env python3
from flask import (
    Flask, render_template, request, redirect, url_for,
    flash, jsonify
)
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
    categories = categoryList()
    items = session.query(Item).select_from(Item).join(Item.category)\
                    .order_by("item_id desc").limit(30)
    return render_template('category_root.html', categories=categories,
        items=items)


@app.route('/catalog/add_item', methods=['GET', 'POST'])
def newItem():
    if request.method == 'POST':
        newItem = Item(title=request.form['name'], 
            description=request.form['description'],
            category_id=request.form['category_id'])
        session.add(newItem)
        session.commit()
        flash("new item created")
        return redirect(url_for('showCatalog'))
    else:
        categories = categoryList()
        return render_template('newitem.html', categories=categories)


@app.route('/catalog/add_category', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCat = Category(title=request.form['name'])
        session.add(newCat)
        session.commit()
        flash("new category created")
        return redirect(url_for('showCatalog'))
    else:
        return render_template('newcategory.html')


@app.route('/catalog/<category_title>/items')
def categoryItems(category_title):
    categories = categoryList()
    items = session.query(Item).select_from(Category).join(Item.category)\
                .filter_by(title=category_title)
    return render_template('category_items.html', categories=categories,
        items=items)


@app.route('/catalog/<category_title>/<item_title>')
def showItem(category_title, item_title):
    item = session.query(Item).filter_by(title=item_title).one()
    return render_template("show_item.html", item=item,\
            category_title=category_title)


@app.route('/catalog/<category_title>/<item_title>/edit')
def editItem(category_title, item_title):
    if request.method == 'POST':
        newItem = Item(title=request.form['name'], 
            description=request.form['description'],
            category_id=request.form['category_id'])
        session.add(newItem)
        session.commit()
        flash("new item created")
        return redirect(url_for('showCatalog'))
    else:
        categories = categoryList()
        item = session.query(Item).select_from(Category).join(Item.category)\
                .filter_by(title=category_title)
        return render_template("edit_item.html", category_title=category_title, item_title=item_title)


@app.route('/catalog/<category_title>/<item_title>/delete')
def deleteItem(category_title, item_title):
    return render_template("delete_item.html", category_title=category_title, item_title=item_title)

# start api endpoints
@app.route('/catalog.json')
def catalogJSON():
    return "Implement and return jsonify of catalog."

def categoryList():
    return session.query(Category).all()


if __name__ == '__main__':
    # app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)