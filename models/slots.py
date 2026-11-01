from app import db

class Slot(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    exam_id = db.Column(db.Integer, db.ForeignKey("exam_id"), nullable = False)
    examiner_id = db.Column(db.Integer, db.ForeignKey("examiner_id"), nullable = False)

    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    capacity = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.boolean, default=True, nullable=False)