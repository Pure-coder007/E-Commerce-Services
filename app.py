from flask import Flask, Blueprint, jsonify, request
from email_validator import validate_email, EmailNotValidError
import mysql.connector
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import random
from passlib.hash import pbkdf2_sha256
# from flask_mail import Mail, Message
from decimal import Decimal
from models import  add_user, get_user_by_email, get_user_by_username

app = Flask(__name__)


jwt = JWTManager()
auth = Blueprint('auth', __name__)

app.config.from_pyfile('config.py')




def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = 'fdghjrgewqertyuykhjfdasfghjkhgdsertyu'
    jwt.init_app(app)
    app.register_blueprint(auth, url_prefix='/auth/v1')
    return app


def email_exists(email):
    user = get_user_by_email(email)
    return user is not None

def username_exists(username):
    user = get_user_by_username(username)
    return user is not None

def validate_email_address(email):
    try:
        validate_email(email)
        return True, None
    except EmailNotValidError as e:
        return False, str(e)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not first_name or not last_name or not username or not email or not password:
        return jsonify({'message': 'All fields are required'}), 400

    is_valid_email, email_error_message = validate_email_address(email)
    if not is_valid_email:
        return jsonify({'message': f'Invalid email address'}), 400

    if email_exists(email):
        return jsonify({'message': 'Email already exists'}), 409
    elif username_exists(username):
        return jsonify({'message': 'Username already taken, please use another'}), 409

    password_hash = pbkdf2_sha256.hash(password)
    add_user(first_name, last_name, email, username, password_hash, is_admin=False)

    return jsonify({'message': 'User created successfully'}), 201












if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
