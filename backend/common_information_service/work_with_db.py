from backend.common.models import School, Class, app, db


def get_schools():
    with app.app_context():
        schools = School.query.all()

    return schools


def get_classes():
    with app.app_context():
        classes = Class.query.all()

    return classes
