from backend.common.models import School, app, db


def get_schools():
    with app.app_context():
        schools = School.query.all()

    return schools
