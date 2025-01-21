from flask_sqlalchemy import SQLALCHEMY
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLALCHEMY()

class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password_hash = db.Column(db.String(200),nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)