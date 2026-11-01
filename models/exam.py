from app import db
from datetime import datetime

class Exam(db.Model):
    #this stores basic info of Exam
    id =  db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    #this stores the foreign key of course and runric table
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    runric_id = db.Column(db.Integer, db.ForeignKey('runric.id'), nullable=False)
    #this stores the booking details of the exam, including the start and end times 
    booking_start = db.Column(db.DateTime, nullable=False)
    booking_end = db.Column(db.DateTime, nullable=False)
    #this has slot info
    slot_creation_start = db.Column(db.DateTime, nullable=False)
    slot_creation_end = db.Column(db.DateTime, nullable=False)
    #and this is time and date info
    duration_minutes = db.Column(db.Integer, nullable=False)
    is_published = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
