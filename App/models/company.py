from App.database import db
from models.user import User
class Company(User):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),nullable=False)
    location = db.Column(db.String(120), nullable = False)
    description = db.Column(db.String(500), nullable=True)
    