import os
from dotenv import load_dotenv
if os.path.exists('../../.env'):
    load_dotenv('../../.env')
else:
    load_dotenv('.env')

SERVICE_PORT = os.getenv("ORDERS_SERVICE_PORT")

from concurrent import futures

import grpc
import orders_pb2
import orders_pb2_grpc

import datetime

from work_with_db import add_order, order_school_relation, parent_student_order_relationship


class OrderServiceServicer(orders_pb2_grpc.OrderServiceServicer):
    def EducationOrder(self, request, context):
        parent = request.parent_order[0]
        student = request.student_order[0]

        parent_order = add_order(
            first_name=parent.first_name,
            last_name=parent.last_name,
            email=parent.email,
            phone_number=parent.phone_number
        )

        parent_order_school = order_school_relation(user_order_id=parent_order.id, user_school_id=parent.school_id)

        student_order = add_order(
            first_name=student.first_name,
            last_name=student.last_name,
            email=student.email,
            phone_number=student.phone_number
        )

        student_order_school = order_school_relation(user_order_id=student_order.id, user_school_id=student.school_id)

        parent_student_order_relationship(parent_order_id=parent_order.id, student_order_id=student_order.id)

        reply = orders_pb2.EducationOrderResponse()
        reply.success = True

        return reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orders_pb2_grpc.add_OrderServiceServicer_to_server(OrderServiceServicer(), server)
    server.add_insecure_port(f'[::]:{SERVICE_PORT}')
    server.start()
    print(str(datetime.datetime.now()) + f"Server started, listening on port: {SERVICE_PORT}")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()