from flask import Flask
from flask_restful import Api,Resource
from models import User,db

app = Flask(__name__)
api = Api(app)

password_pattern
email pattern

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