import os
from dotenv import load_dotenv
if os.path.exists('../../.env'):
    load_dotenv('../../.env')
else:
    load_dotenv('.env')

SERVICE_PORT = os.getenv("SEND_EMAIL_SERVICE_PORT")

from concurrent import futures

import grpc
import send_email_pb2
import send_email_pb2_grpc

import datetime

from work_with_db import get_email_credentials
from send_mail import SendMail


class SendEmailServiceServicer(send_email_pb2_grpc.SendEmailServiceServicer):
    def SendEmail(self, request, context):
        message = request.message
        subject = request.subject
        email_address_to = request.email_address_to
        email_credentials = get_email_credentials()

        email_sender = SendMail(
            message=message,
            subject=subject,
            email_address_to=email_address_to,
            host=email_credentials.host,
            port=email_credentials.port,
            email_address_from=email_credentials.email_address_from,
            email_password=email_credentials.email_password
        )
        send_email_success = email_sender.send_email()

        reply = send_email_pb2.SendEmailResponse()
        reply.success = send_email_success

        return reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    send_email_pb2_grpc.add_SendEmailServiceServicer_to_server(SendEmailServiceServicer(), server)
    server.add_insecure_port(f'[::]:{SERVICE_PORT}')
    server.start()
    print(str(datetime.datetime.now()) + f"Server started, listening on port: {SERVICE_PORT}")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

