from flask import jsonify, redirect
from models import Dog, db

def create_dog(breed, lifespan, miniature):
  miniature = bool(miniature)
  dog = Dog(breed=breed, lifespan=lifespan, miniature=miniature)
  db.session.add(dog)
  db.session.commit()
  return jsonify(dog.as_dict())

def get_all_dogs():
  all_dogs = Dog.query.all()
  if all_dogs:
    results = [dog.as_dict() for dog in all_dogs]
    return jsonify(results)
  else: return jsonify({ 'message': 'no dogs in database' })

def get_dog(id):
  dog = Dog.query.get(id)
  if dog:
    results = dog.as_dict()
    return jsonify(results)
  else: return jsonify({ 'message': f"no dog found by the id {id}" })

def update_dog(id, breed, lifespan, miniature):
  dog = Dog.query.get(id)
  if dog:
    dog.breed = breed or dog.breed
    dog.lifespan = lifespan or dog.lifespan
    dog.miniature = miniature or dog.miniature
    db.session.commit()
    return jsonify(dog.as_dict())
  else: return jsonify({ 'message': f"no dog found by the id {id}" })

def destroy_dog(id):
  dog = Dog.query.get(id)
  if dog:
    db.session.delete(dog)
    db.session.commit()
    return redirect('/dogs')
  else: return jsonify({ 'message': f"no dog found by the id {id}" })