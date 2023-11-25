from backend.common.models import User, Role, UsersSchool, app, db


def get_user(login=None, password=None):
    with app.app_context():
        if password is not None:
            user = User.query.filter_by(login=login, password=password).first()
        else:
            user = User.query.filter_by(login=login).first()
    return user


def get_user_role(login):
    with app.app_context():
        user_role = db.session.query(User.role_id, Role.role).join(Role).filter(User.login == login).first()

    return user_role


def get_users_school(user_id):
    with app.app_context():
        users_school = UsersSchool.query.filter_by(user_id=user_id).first()

    return users_school


def get_role(role):
    with app.app_context():
        role = Role.query.filter_by(role=role).first()

    return role


def add_user(
        email,
        password,
        first_name,
        last_name,
        phone_number,
        role_id,
        login
):
    with app.app_context():
        try:
            user = User(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                role_id=role_id,
                login=login
            )
            db.session.add(user)
            db.session.commit()
            print(user.id)
            return user
        except:
            db.session.rollback()
            return None


def add_user_school(school_id, user_id):
    with app.app_context():
        user_school = UsersSchool(school_id=school_id, user_id=user_id)
        db.session.add(user_school)
        db.session.commit()
