from app import db

class Rubric(db.Model):
    id =db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

class RubricCriterion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rubric_id = db.Column(db.Integer, db.ForeignKey('rubric.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    max_score = db.Column(db.Float, nullable=False)

