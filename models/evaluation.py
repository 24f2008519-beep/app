from app import db

class Evaluation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    