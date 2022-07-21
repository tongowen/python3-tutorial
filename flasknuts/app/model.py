from app import db


class User(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pwd  = db.Column(db.String(20))


class Photo(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(60))
    date  = db.Column(db.String(4))


class Book(db.Model):
	id = db.Column(db.Integer, primary_key = True )
	book = db.Column(db.String(30))
	date = db.Column(db.String(30))
