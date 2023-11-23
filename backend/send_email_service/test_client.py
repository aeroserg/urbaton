import grpc
import send_email_pb2
import send_email_pb2_grpc

HOST = 'localhost'
PORT = '9001'

with grpc.insecure_channel(HOST + ':' + PORT) as channel:
    stub = send_email_pb2_grpc.SendEmailServiceStub(channel)
    response = stub.SendEmail(
        send_email_pb2.SendEmailRequest(
            message='ты пидор',
            subject='пидорское письмо',
            email_address_to='1308267@gmail.com'
        )
    )

    print(response)
