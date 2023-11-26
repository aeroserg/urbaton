import os
from collections import defaultdict

from dotenv import load_dotenv
if os.path.exists('../../.env'):
    load_dotenv('../../.env')
else:
    load_dotenv('.env')

SERVICE_PORT = os.getenv("MESSAGE_SERVICE_PORT")

from concurrent import futures
import datetime

import grpc
import message_pb2_grpc
import message_pb2
from message_pb2 import GetMessageResponse, Message

from work_with_db import send_message, get_message, get_user


class MessageServiceServicer(message_pb2_grpc.MessageServiceServicer):
    def SendMessage(self, request, context):
        text = request.text
        login_from = request.login_from
        id_to = request.id_to

        user = get_user(login=login_from)

        send_message(id_from=user.id, id_to=id_to, text=text)

        reply = message_pb2.SendMessageResponse()
        reply.success = True

        return reply

    def GetMessage(self, request, context):
        login = request.login

        user = get_user(login=login)
        messages = get_message(id_to=user.id)

        response = []

        for message, first_name, last_name in messages:
            response.append(
                Message(
                    text=message.text,
                    first_name_from=first_name,
                    last_name_from=last_name
                )
            )

        return GetMessageResponse(messages=response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_MessageServiceServicer_to_server(MessageServiceServicer(), server)
    server.add_insecure_port(f'[::]:{SERVICE_PORT}')
    server.start()
    print(str(datetime.datetime.now()) + f"Server started, listening on port: {SERVICE_PORT}")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
