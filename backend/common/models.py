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


class ParentStudentRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class ParentStudentRelationshipOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer, nullable=False)
    name_group = db.Column(db.String, nullable=False)


class StudentGroupRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)


class TutorGroupRelationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class StudentsCourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)


class StudentMarks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    students_course = db.Column(db.Integer, db.ForeignKey('students_course.id'), nullable=False)
    mark = db.Column(db.Integer, nullable=False)


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


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # role1 = Role(id='642b6836-51f6-4ace-8e1e-8ff7b47e5719', role='школа')
        # role2 = Role(id='78c2d488-d982-4e5b-a4ef-d105f67e6935', role='родитель')
        # role3 = Role(id='2b618d72-cd4e-4f90-81d2-293599e50e5e', role='ученик')
        # role4 = Role(id='abfa64e6-78c7-40de-ab54-bb442554b117', role='преподаватель')
        # db.session.add_all(
        #     [role1, role2, role3, role4])
        # db.session.commit()
