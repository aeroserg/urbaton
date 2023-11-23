import os
from dotenv import load_dotenv
load_dotenv('../../.env')

HOST = os.getenv("SERVICE_HOST")
SERVICE_PORT = os.getenv("SEND_EMAIL_SERVICE_PORT")

import grpc
import send_email_pb2
import send_email_pb2_grpc


def send_greeting_email(message, subject, email_address_to):
    with grpc.insecure_channel(HOST + ':' + SERVICE_PORT) as channel:
        stub = send_email_pb2_grpc.SendEmailServiceStub(channel)
        response = stub.SendEmail(
            send_email_pb2.SendEmailRequest(
                message=message,
                subject=subject,
                email_address_to=email_address_to
            )
        )

    return response
