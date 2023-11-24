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

from backend.common.models import (User, Role, Order, ParentStudentRelationshipOrder, School, UsersSchool, db)
from flask import Flask, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{DB_POSTGRES_USERNAME}:{DB_POSTGRES_PASSWORD}@{DB_POSTGRES_HOST}:{DB_POSTGRES_PORT}/{DB_POSTGRES_DBNAME}"
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
jwt = JWTManager(app)

db.init_app(app)


@app.route('/all_schools', methods=['GET'])
def all_schools():
    response = {"schools": []}
    schools = School.query.all()

    for school in schools:
        response["schools"].append(
            {
                "id": school.id,
                "name": school.name,
                "email": school.email,
                "phone_number": school.phone_number,
                "address": school.address
            }
        )

    return response, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9002)
