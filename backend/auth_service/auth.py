import os
from dotenv import load_dotenv
if os.path.exists('../../.env'):
    load_dotenv('../../.env')
else:
    load_dotenv('.env')

DB_POSTGRES_DBNAME = os.getenv("DB_POSTGRES_DBNAME")
DB_POSTGRES_USERNAME = os.getenv("DB_POSTGRES_USERNAME")
DB_POSTGRES_PASSWORD = os.getenv("DB_POSTGRES_PASSWORD")
DB_POSTGRES_HOST = os.getenv("DB_POSTGRES_HOST")
DB_POSTGRES_PORT = os.getenv("DB_POSTGRES_PORT")

from backend.common.models import (User, Role, db)
from flask import Flask, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS

from login_generator import generate_login
from password_generator import password_generator
from send_greeting_email import send_greeting_email
from email_template import MESSAGE, SUBJECT

app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{DB_POSTGRES_USERNAME}:{DB_POSTGRES_PASSWORD}@{DB_POSTGRES_HOST}:{DB_POSTGRES_PORT}/{DB_POSTGRES_DBNAME}"
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
jwt = JWTManager(app)

db.init_app(app)


@app.route('/register_user', methods=['POST'])
@jwt_required()
def registration():
    current_user = get_jwt_identity()
    user_role = db.session.query(User.role_id, Role.role).join(Role).filter(User.login == current_user).first()
    if user_role.role != 'школа':
        return {'user_created': True, 'email_send_to_user': False}, 200

    data = request.get_json()

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    phone_number = data.get('phone_number')
    role = data.get('role')
    login = generate_login(first_name=first_name, last_name=last_name)
    password = password_generator(10)

    role = Role.query.filter_by(role=role).first()

    try:
        user = User(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            role_id=role.id,
            login=login
        )
        db.session.add(user)
        db.session.commit()

        greeting_success = send_greeting_email(
            message=MESSAGE.format(login=login, password=password),
            subject=SUBJECT,
            email_address_to=email
        )

        if not greeting_success:
            return {'user_created': True, 'email_send_to_user': False}, 200

        return {'user_created': True, 'email_send_to_user': True}, 200

    except IntegrityError as ex:
        print(ex)
        db.session.rollback()
        return {'success': False, 'email_send_to_user': False}, 400


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    password = data.get('password')
    login = data.get('login')

    user = User.query.filter_by(login=login, password=password).first()
    if user:
        access_token = create_access_token(identity=login)

        return {
                'access_token': access_token,
                'role_id': user.role_id,
                'first_name': user.first_name
            }, 200
    return {'message': 'Invalid credentials'}, 401


@app.route('/header', methods=['GET'])
@jwt_required()
def get_header_info():
    current_user = get_jwt_identity()
    user = User.query.filter_by(login=current_user).first()

    return (
        {
            "user_name": user.first_name,
            "role_id": user.role_id
        }
    ), 200


@app.route('/new_order', methods=['POST'])
def new_order():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
