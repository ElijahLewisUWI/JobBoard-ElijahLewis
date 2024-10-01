from App.database import db
from models.user import User
class Applicant(User):
    __tablename__ = 'applicant'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120),nullable=False)
    last_name = db.Column(db.String(120),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    location = db.Column(db.String(120),nullable=False)
  