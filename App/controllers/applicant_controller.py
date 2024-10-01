from App import db
from App.models import Applicant, Application, Job, Company
from datetime import datetime


def apply_to_job(applicant_id, job_id):
    new_application = Application(
        date_sent=datetime.utcnow(),
        applicant_id=applicant_id,
        job_id=job_id
    )
    db.session.add(new_application)
    db.session.commit()
    print("Application submitted successfully.")


def view_jobs():
    jobs = Job.query.all() 
    job_list = []
    for job in jobs:
        j_list.append({
            'id': job.id,
            'title': job.title,
            'description': job.description,
            'location': job.location,
            'remote_option': job.remote_option,
            'date_posted': job.date_posted.strftime('%Y-%m-%d')  
        })
    
    return j_list
