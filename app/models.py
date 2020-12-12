from datetime import datetime

from app import db

class Request(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    log       = db.Column(db.String, nullable=False)
    datestamp = db.Column(db.DateTime, default=datetime.now)
