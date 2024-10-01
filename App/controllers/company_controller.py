from App import db
from App.models import Applicant, Application, Job, Company
from datetime import datetime

def post_job(company_id, title, description, location, remote_option):
    company = Company.query.get(company_id)
    if not company:
        print("Company not found!")
        return 
    
    new_job = Job(
        company_id=company_id,
        title=title,
        description=description,
        location=location,
        remote_option=remote_option,
        date_posted=datetime.now()
    )
    
    db.session.add(new_job)
    db.session.commit()

    print("Job posted succesfully")


def view_applications(job_id):
    job = Job.query.get(job_id)
    
    if not job:
        print("ID not found!")
        return  
    
    applications = Application.query.filter_by(job_id=job_id).all()
    
    if not applications:
        print("No applications found.")
        return  
    
    print("Applications for the job:")
    for app in applications:
        applicant = app.applicant 
        print(f"Applicant {applicant.name} applied on {app.date_applied}")
