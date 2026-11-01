from app import db

class Examiner_Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    contact_details = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)