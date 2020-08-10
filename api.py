from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/diy-api-python'

# IMPORT CRUD AFTER DATABASE IS SET UP
from dog_crud import *

# ROUTES
@app.route('/')
def home():
  return "Hello World!"

@app.route('/dogs', methods=['GET', 'POST'])
def dogs():
  # list all dogs
  if request.method == 'GET':
    return get_all_dogs()
  # add a dog
  if request.method == 'POST':
    create_dog(request.form['breed'], request.form['lifespan'], request.form['miniature'])
    return redirect('/dogs')

@app.route('/dogs/<id>', methods=['GET', 'PUT', 'DELETE'])
def show(id):
  if request.method == 'GET':
    return get_dog(id)
  if request.method == 'PUT':
    return udpate_dog((id, request.form['breed'], request.form['lifespan'], request.form['miniature']))
  if request.method == 'DELETE':
    return destroy_dog(id)