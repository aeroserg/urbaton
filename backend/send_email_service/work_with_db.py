from backend.common.models import EmailSettings, app


def get_email_credentials():
    with app.app_context():
        email_credentials = EmailSettings.query.first()

    return email_credentials
