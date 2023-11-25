from backend.common.models import (School, Class, EducationYear, User, UsersSchool, ClassStudentRelation,
                                   StudentEducationYearRelationship, app, db)


def get_schools():
    with app.app_context():
        schools = School.query.all()

    return schools


def get_classes():
    with app.app_context():
        classes = Class.query.all()

    return classes


def get_education_years():
    with app.app_context():
        education_years = EducationYear.query.all()

    return education_years


def get_students(login):
    with app.app_context():
        admin = User.query.filter_by(login=login).first()
        admins_school = UsersSchool.query.filter_by(user_id=admin.id).first()

        users_data = (
            db.session.query(User.first_name, User.last_name, User.id, ClassStudentRelation.class_id,
                             StudentEducationYearRelationship.education_year)
            .join(UsersSchool, User.id == UsersSchool.user_id)
            .outerjoin(ClassStudentRelation, User.id == ClassStudentRelation.student_id)
            .outerjoin(StudentEducationYearRelationship, User.id == StudentEducationYearRelationship.student_id)
            .filter(UsersSchool.school_id == admins_school.school_id)
            .all()
        )

        users_list = [
            {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'id': user.id,
                'class_name': user.class_id,
                'grade': user.education_year
            }
            for user in users_data if user.education_year is not None
        ]
        # response = transform_data(users_list)
        return users_list


