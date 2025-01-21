from flask_sqlalchemy import SQLALCHEMY

db = SQLALCHEMY()

class Users(db.Model):
    "first_name": db.Column(db.String,VarChar(200),nullable=False)
    "last_name": db.Column(db.String,VarChar(200),nullable=False)
    "email": db.Column(db.String,Unique=True,nullable=False)
    "password": db.Column(db.String,nullable=False)