from app import db

class Examination_Rubric(db.Model):
    Rubic_id = db.Column(db.Integer, primary_key=True)
    Exam_id = db.Column(db.Integer, 
                        db.ForeignKey("Exam_id"), 
                        nullable=False)
    Criterion_Name = db.Column(db.String(120), nullable=False)
    Max_marks = db.Column(db.Float, nullable=False)
    Weightage = db.Column(db.Float, nullable=False)
    Description = db.Column(db.Text, nullable=True)
