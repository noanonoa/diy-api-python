from flask import Flask, jsonify, request
app = Flask(__name__)

all_dogs = {
  "id": 12321,
  "breed": "Golden Retreiver",
  "lifespan": "10 - 12 years",
  "miniature": False
} 

@app.route('/')
def home():
  return "Hello World!"

@app.route('/dogs', methods=['GET', 'POST'])
def dogs():
  # list all dogs
  if request.method == 'GET':
    return jsonify(all_dogs)
  # add a dog
  if request.method == 'POST':
    return "CREATE new dog"

@app.route('/dogs/<dog_id>', methods=['GET', 'PUT', 'DELETE'])
def show(dog_id):
  if request.method == 'GET':
    return f"GET dog {dog_id}'s information"
  if request.method == 'PUT':
    return f"PUT (or UPDATE) dog {dog_id}'s information"
  if request.method == 'DELETE':
    return f"DELETE dog {dog_id}'s information'"