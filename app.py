from flask import Flask, request
from flask_restful import Api,Resource
from flask_jwt_extended import JWTManager, create_access_token
from marshmallow import ValidationError
from models import User,db
from schemas import UserSchema
from utils import error_response, success_response
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)


class Signup(Resource):
    @jwt_required
    def signup(post):
        id = get_jwt_identity()
        email = User.query.filter_by(email=email).first()
        if email:
            return (error,'email already exists'),500
        else:
            new_user = User(
                'first_name':first_name,
                'last_name': last_name,
                'email':email
                'password':password
            )
            db.add(new_user)
            db.commit(new_user)

if __name__=='__main__':
    app.run(port=5000,debug=True)