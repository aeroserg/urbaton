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

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{DB_POSTGRES_USERNAME}:{DB_POSTGRES_PASSWORD}@{DB_POSTGRES_HOST}:{DB_POSTGRES_PORT}/{DB_POSTGRES_DBNAME}"
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    login = db.Column(db.String(150), unique=True, nullable=False)
    phone_number = db.Column(db.String(100), nullable=True)
    role_id = db.Column(db.String, db.ForeignKey('role.id'), nullable=False)


class Role(db.Model):
    id = db.Column(db.String, primary_key=True)
    role = db.Column(db.String, unique=True, nullable=False)


class EmailSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String, unique=True, nullable=False)
    port = db.Column(db.String, unique=True, nullable=False)
    email_address_from = db.Column(db.String, unique=True, nullable=False)
    email_password = db.Column(db.String, unique=True, nullable=False)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(100), nullable=True)
    accepted = db.Column(db.Boolean, nullable=False, default=False)


class ParentStudentRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class ParentStudentRelationshipOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)


class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String, nullable=False)


class UsersSchool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class OrderSchoolRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)


# год обучения
class EducationYear(db.Model):
    id = db.Column(db.Integer, primary_key=True)


# на каком году обучения студент
class StudentEducationYearRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    education_year = db.Column(db.Integer, db.ForeignKey('education_year.id'), nullable=False)


# буква класса
class Class(db.Model):
    id = db.Column(db.String, primary_key=True)


# в каком классе ученик
class ClassStudentRelation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    class_id = db.Column(db.String, db.ForeignKey('class.id'), nullable=False)


# направление обучения общие
class CourseCommon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


# направление обучения индивидуальные
class CourseIndividual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


# общий курс преподавателя
class TutorCourseCommonRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tutor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course_common.id'), nullable=False)


# индивидуальный курс преподавателя
class TutorCourseIndividualRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tutor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course_individual.id'), nullable=False)


# общий курс студента
class StudentCourseCommon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course_common.id'), nullable=False)


# индивидуальный курс студента
class StudentsCourseIndividual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course_individual.id'), nullable=False)


# оценки ученика на индивидуальном курсе
class StudentMarksCourseIndividual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course_individual.id'), nullable=False)
    mark = db.Column(db.Integer, nullable=False)


# оценки ученика на общем курсе
class StudentMarksCourseCommon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course_common.id'), nullable=False)
    mark = db.Column(db.Integer, nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
