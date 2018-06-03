from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import *
from database_setup import Base, Category, Item
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Empty the tables
session.query(Category).delete()
session.query(Item).delete()

# Add categories
sample_categories = ['guitars', 'pianos', 'drums',
                     'accessories', 'books']

for category_name in sample_categories:
    category = Category()
    category.name = category_name
    session.add(category)
session.commit()

# First index is for the item
# Second index is for title,category_id respectively
items = [['cort g110 stratocaster', 1],
         ['Yamaha P155 Contemporary Piano', 2],
         ['Riot PODRT522BK 5-Piece Drum Set', 3],
         ['Guitar capo', 4],
         ['Fingerstyle & Slide guitar in open tunings', 5]]


for i in range(0, 4):
    itemm = Item()
    itemm.name = items[i][0]
    itemm.description = 'description'
    itemm.category_id = items[i][1]
    session.add(itemm)
session.commit()
