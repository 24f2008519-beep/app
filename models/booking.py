from app import db
from datetime import datetime

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
#This retreves id's info
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"), nullable=False)
    slot_id = db.Column(db.Integer, db.ForeignKey("slot.id"), nullable=False)
    Student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
#this retreves the status of the booking, when it was booked and when it was cancelled
    Status = db.Column(db.String(20), default = "Booked", nullable=False)
    Booked_at = db.Column(db.DateTime, default = datetime.utcnow)
    cancelled_at = db.Column(db.DateTime)
#this works as a constraint for duplicate bookings for the same exam, slot, and student combination
    __table_args__ = (db.UniqueConstraint('exam_id', 'slot_id', 'Student_id',
                                           name='unique_booking'),)
        
        