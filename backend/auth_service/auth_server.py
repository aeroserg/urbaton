import os
from dotenv import load_dotenv
if os.path.exists('../../.env'):
    load_dotenv('../../.env')
else:
    load_dotenv('.env')

SERVICE_PORT = os.getenv("AUTH_SERVICE_PORT")

from concurrent import futures

import grpc
import auth_pb2
import auth_pb2_grpc

import datetime

from work_with_db import get_user, get_user_role, get_users_school, get_role, add_user, add_user_school
from password_generator import password_generator
from login_generator import generate_login
from send_greeting_email import send_greeting_email
from email_template import MESSAGE, SUBJECT


class AuthServiceServicer(auth_pb2_grpc.AuthServiceServicer):
    def Login(self, request, context):
        password = request.password
        login = request.login

        reply = auth_pb2.LoginResponse()

        user = get_user(login=login, password=password)

        if user:
            reply.first_name = user.first_name
            reply.role_id = user.role_id
        else:
            reply.first_name = None
            reply.role_id = None

        return reply

    def Header(self, request, context):
        login = request.login

        reply = auth_pb2.HeaderResponse()

        user = get_user(login=login)
        reply.user_name = user.first_name
        reply.role_id = user.role_id

        return reply

    def RegisterUser(self, request, context):
        first_name = request.first_name
        last_name = request.last_name
        email = request.email
        phone_number = request.phone_number
        role = request.role
        current_user = request.current_user

        reply = auth_pb2.RegisterUserResponse()

        user_role = get_user_role(login=current_user)

        if user_role.role != 'школа':
            reply.user_created = False
            reply.email_send_to_user = False

            return reply

        admin_user = get_user(login=current_user)
        admins_school = get_users_school(user_id=admin_user.id)

        login = generate_login(first_name=first_name, last_name=last_name)
        password = password_generator(10)

        role = get_role(role=role)

        user = add_user(
            email,
            password,
            first_name,
            last_name,
            phone_number,
            role.id,
            login
        )
        if user is not None:
            add_user_school(school_id=admins_school.school_id, user_id=user.id)

            greeting_success = send_greeting_email(
                message=MESSAGE.format(login=login, password=password),
                subject=SUBJECT,
                email_address_to=email
            )

            if not greeting_success:
                reply.user_created = True
                reply.email_send_to_user = False

                return reply

            reply.user_created = True
            reply.email_send_to_user = True

            return reply

        else:
            reply.user_created = False
            reply.email_send_to_user = False

            return reply

    # def RegisterSchool(self,  request, context):
    #     name = request.name
    #     email = request.email
    #     phone_number = request.phone_number
    #     address = request.address
    #     current_user = request.current_user
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


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthServiceServicer(), server)
    server.add_insecure_port(f'[::]:{SERVICE_PORT}')
    server.start()
    print(str(datetime.datetime.now()) + f"Server started, listening on port: {SERVICE_PORT}")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
