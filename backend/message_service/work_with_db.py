from backend.common.models import (Message, User, app, db)


def send_message(id_to, id_from, text):
    with app.app_context():
        message = Message(id_to=id_to, id_from=id_from, text=text)

        db.session.add(message)
        db.session.commit()


def update_message_status(message_id):
    with app.app_context():
        message = Message.query.filter_by(id=message_id).first()
        message.delivered = True
        db.session.commit()


def get_message(id_to):
    with app.app_context():
        messages = db.session.query(Message, User.first_name, User.last_name). \
            join(User, Message.id_from == User.id). \
            filter(Message.id_to == id_to, Message.delivered == False).all()

        for message, _, _ in messages:
            update_message_status(message.id)

        return messages


def get_user(login):
    with app.app_context():
        user = User.query.filter_by(login=login).first()
        return user
