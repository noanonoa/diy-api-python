from api import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Dog(db.Model):
  __tablename__='dogs'

  id = db.Column(db.Integer, primary_key=True)
  breed = db.Column(db.String(50), nullable=False)
  lifespan = db.Column(db.String)
  miniature = db.Column(db.Boolean)

  def __repr__(self):
    return f"🐶 Dog\nid: {self.id} \nbreed: {self.breed} \nlifespan: {self.lifespan} \nminiature: {self.miniature}"