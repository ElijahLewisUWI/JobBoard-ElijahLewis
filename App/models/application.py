from App.database import db
from models.applicant import Applicant
from models.job import Job

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True)

    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'), nullable=False)  
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)  
    applicant = db.relationship('Applicant', backref='applications', lazy=True)
    date_sent = db.Column(db.DateTime, nullable=False)
    job = db.relationship('Job', backref='applications', lazy=True)