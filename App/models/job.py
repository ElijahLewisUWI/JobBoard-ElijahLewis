from App.database import db
from models.company import Company
from datetime import datetime
class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)  
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(120), nullable=True)
    remote_option = db.Column(db.Boolean,nullable = False)
    date_posted = db.Column(db.DateTime, nullable=False)
    company = db.relationship('Company', backref='jobs', lazy=True)