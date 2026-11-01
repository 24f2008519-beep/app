from app import db
# This stores the information about the courses offered 
# in the examination management portal. Each course has a unique code, 
# a name, a description, and an active status indicating 
# whether the course is currently available for enrollment or not.
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.text, nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
