import os
from dotenv import load_dotenv
if os.path.exists('../../.env'):
    load_dotenv('../../.env')
else:
    load_dotenv('.env')

AUTH_SERVICE_HOST = os.getenv("AUTH_SERVICE_HOST")
AUTH_SERVICE_PORT = os.getenv("AUTH_SERVICE_PORT")
COMMON_SERVICE_HOST = os.getenv("COMMON_SERVICE_HOST")
COMMON_SERVICE_PORT = os.getenv("COMMON_SERVICE_PORT")
ORDER_SERVICE_HOST = os.getenv("ORDERS_SERVICE_HOST")
ORDER_SERVICE_PORT = os.getenv("ORDERS_SERVICE_PORT")

from flask import Flask, request
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from flask_cors import CORS

import grpc
import auth_pb2
import auth_pb2_grpc
import common_pb2
import common_pb2_grpc
import orders_pb2
from orders_pb2 import EducationOrderParent, EducationOrderStudent
import orders_pb2_grpc

app = Flask(__name__)
cors = CORS(app)

app.config['JWT_SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
jwt = JWTManager(app)


# @app.route('/register_school', methods=['POST'])
# @jwt_required()
# def register_school():
#     current_user = get_jwt_identity()
#     data = request.get_json()
#     name = data.get('name')
#     email = data.get('email')
#     phone_number = data.get('phone_number')
#     address = data.get('address')
#
#     try:
#         school = School(
#             name=name,
#             email=email,
#             phone_number=phone_number,
#             address=address
#         )
#
#         db.session.add(school)
#         db.session.commit()
#
#         role = Role.query.filter_by(role='школа').first()
#
#         school_password = password_generator(10)
#         school_login = generate_login(first_name=name, last_name=name)
#
#         user = User(
#             email=email,
#             password=school_password,
#             first_name=name,
#             last_name=name,
#             phone_number=phone_number,
#             role_id=role.id,
#             login=school_login
#         )
#         db.session.add(user)
#         db.session.commit()
#
#         user_school = UsersSchool(school_id=school.id, user_id=user.id)
#         db.session.add(user_school)
#         db.session.commit()
#
#         greeting_success = send_greeting_email(
#             message=MESSAGE.format(login=school_login, password=school_password),
#             subject=SUBJECT,
#             email_address_to=email
#         )
#
#         if not greeting_success:
#             return {'school_created': True, 'email_send_to_school': False}, 200
#
#         return {'school_created': True, 'email_send_to_school': True}, 200
#
#     except IntegrityError as ex:
#         print(ex)
#         db.session.rollback()
#         return {'school_created': False, 'email_send_to_school': False}, 400
#
#
@app.route('/register_user', methods=['POST'])
@jwt_required()
def registration():
    current_user = get_jwt_identity()

    data = request.get_json()

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    phone_number = data.get('phone_number')
    role = data.get('role')

    with grpc.insecure_channel(AUTH_SERVICE_HOST + ':' + AUTH_SERVICE_PORT) as channel:
        stub = auth_pb2_grpc.AuthServiceStub(channel)
        response = stub.RegisterUser(
            auth_pb2.RegisterUserRequest(
                current_user=current_user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                role=role
            )
        )

    return {'user_created': response.user_created, 'email_send_to_user': response.email_send_to_user}, 200


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    password = data.get('password')
    login = data.get('login')

    with grpc.insecure_channel(AUTH_SERVICE_HOST + ':' + AUTH_SERVICE_PORT) as channel:
        stub = auth_pb2_grpc.AuthServiceStub(channel)
        response = stub.Login(
            auth_pb2.LoginRequest(
                password=password,
                login=login
            )
        )

    if response.role_id is not None:
        access_token = create_access_token(identity=login)
        return {
                'access_token': access_token,
                'role_id': response.role_id,
                'first_name': response.first_name
            }, 200
    return {'message': 'Invalid credentials'}, 401


@app.route('/header', methods=['GET'])
@jwt_required()
def get_header_info():
    current_user = get_jwt_identity()

    with grpc.insecure_channel(AUTH_SERVICE_HOST + ':' + AUTH_SERVICE_PORT) as channel:
        stub = auth_pb2_grpc.AuthServiceStub(channel)
        response = stub.Header(
            auth_pb2.HeaderRequest(
                login=current_user
            )
        )

    return (
        {
            "user_name": response.user_name,
            "role_id": response.role_id
        }
    ), 200


@app.route('/new_order', methods=['POST'])
def new_order():
    data = request.get_json()

    parent = data.get('parent')
    student = data.get('student')

    with grpc.insecure_channel(ORDER_SERVICE_HOST + ':' + ORDER_SERVICE_PORT) as channel:
        stub = orders_pb2_grpc.OrderServiceStub(channel)
        response = stub.EducationOrder(
            orders_pb2.EducationOrderRequest(
                parent_order=[
                    EducationOrderParent(
                        first_name=parent['first_name'],
                        last_name=parent['last_name'],
                        email=parent['email'],
                        phone_number=parent['phone_number'],
                        school_id=parent['school_id']
                    )
                ],
                student_order=[
                    EducationOrderStudent(
                        first_name=student['first_name'],
                        last_name=student['last_name'],
                        email=student['email'],
                        phone_number=student['phone_number'],
                        school_id=student['school_id']
                    )
                ]
            )
        )

    return {'user_created': response.success}, 200


@app.route('/all_schools', methods=['GET'])
def all_schools():
    response = {"schools": []}

    with grpc.insecure_channel(COMMON_SERVICE_HOST + ':' + COMMON_SERVICE_PORT) as channel:
        stub = common_pb2_grpc.CommonServiceStub(channel)
        schools = stub.Schools(
            common_pb2.SchoolsRequest()
        )

    for school in schools.schools:
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


@app.route('/orders', methods=['GET'])
@jwt_required()
def get_orders():
    current_user = get_jwt_identity()
    response = {"orders": []}
    with grpc.insecure_channel(ORDER_SERVICE_HOST + ':' + ORDER_SERVICE_PORT) as channel:
        stub = orders_pb2_grpc.OrderServiceStub(channel)
        orders = stub.GetOrder(
            orders_pb2.GetOrderRequest(
                login=current_user
            ))

    for order in orders.orders:
        response["orders"].append(
            {
                "id": order.id,
                "first_name": order.first_name,
                "last_name": order.last_name,
                "email": order.email,
                "phone_number": order.phone_number
            }
        )

    return response, 200


@app.route('/classes', methods=['GET'])
@jwt_required()
def get_classes():
    response = {"classes": []}

    with grpc.insecure_channel(COMMON_SERVICE_HOST + ':' + COMMON_SERVICE_PORT) as channel:
        stub = common_pb2_grpc.CommonServiceStub(channel)
        classes = stub.GetClass(
            common_pb2.GetClassRequest()
        )

    for class_name in classes.classes:
        response["classes"].append(
            {
                "class_name": class_name.class_name,
            }
        )

    return response, 200


@app.route('/grade', methods=['GET'])
@jwt_required()
def get_grade():
    response = {"grades": []}

    with grpc.insecure_channel(COMMON_SERVICE_HOST + ':' + COMMON_SERVICE_PORT) as channel:
        stub = common_pb2_grpc.CommonServiceStub(channel)
        grades = stub.GetEducationYear(
            common_pb2.GetEducationYearRequest()
        )

    for grade in grades.education_years:
        response["grades"].append(
            {
                "grade": grade.education_year,
            }
        )

    return response, 200


def transform_data(input_data):
    result = {"grades": {}}

    for entry in input_data:
        grade = entry.get("grade")
        class_name = entry.get("class_name")

        if grade not in result["grades"]:
            result["grades"][grade] = {}

        if class_name not in result["grades"][grade]:
            result["grades"][grade][class_name] = []

        student_info = {"first_name": entry["first_name"], "id": entry["id"]}
        result["grades"][grade][class_name].append(student_info)

    return result


@app.route('/students_for_timetable', methods=['GET'])
@jwt_required()
def get_students_for_timetable():
    current_user = get_jwt_identity()

    with grpc.insecure_channel(COMMON_SERVICE_HOST + ':' + COMMON_SERVICE_PORT) as channel:
        stub = common_pb2_grpc.CommonServiceStub(channel)
        response = stub.GetStudents(
            common_pb2.GetStudentsRequest(
                login=str(current_user)
            ))

    result = []

    for grade_info in response.grades[0].grade_full_info:
        grade = grade_info.grade
        for class_info in grade_info.classes:
            class_name = class_info.class_name
            students = class_info.students

            for student_info in students:
                entry = {
                    'grade': grade,
                    'class_name': class_name,
                    'first_name': student_info.first_name,
                    'last_name': student_info.last_name,
                    'id': student_info.id
                }
                result.append(entry)

    return transform_data(result), 200


@app.route('/tutors_for_timetable', methods=['GET'])
@jwt_required()
def get_tutors_for_timetable():
    current_user = get_jwt_identity()

    with grpc.insecure_channel(COMMON_SERVICE_HOST + ':' + COMMON_SERVICE_PORT) as channel:
        stub = common_pb2_grpc.CommonServiceStub(channel)
        response = stub.GetTutor(
            common_pb2.GetTutorRequest(
                login=str(current_user)
            ))

    result = []
    for tutor in response.tutors:
        result.append({
            'first_name': tutor.first_name,
            'last_name': tutor.last_name,
            'individual_course_name': tutor.individual_course_name,
            'common_course_name': tutor.common_course_name
        })

    return {"tutors": result}, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
