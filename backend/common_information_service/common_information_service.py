import os
from dotenv import load_dotenv
if os.path.exists('../../.env'):
    load_dotenv('../../.env')
else:
    load_dotenv('.env')

SERVICE_PORT = os.getenv("COMMON_SERVICE_PORT")

from concurrent import futures
import datetime

import grpc
import common_pb2_grpc
from common_pb2 import School, SchoolsResponse, GetClassResponse, Class

from work_with_db import get_schools, get_classes


class CommonServiceServicer(common_pb2_grpc.CommonServiceServicer):
    def Schools(self, request, context):
        schools = get_schools()

        response = []

        for school in schools:
            response.append(
                School(
                    id=school.id,
                    name=school.name,
                    email=school.email,
                    phone_number=school.phone_number,
                    address=school.address
                )
            )

        return SchoolsResponse(schools=response)

    def GetClass(self, request, context):
        classes = get_classes()

        response = []

        for class_name in classes:
            response.append(
                Class(
                    class_name=class_name.id
                )
            )

        return GetClassResponse(classes=response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    common_pb2_grpc.add_CommonServiceServicer_to_server(CommonServiceServicer(), server)
    server.add_insecure_port(f'[::]:{SERVICE_PORT}')
    server.start()
    print(str(datetime.datetime.now()) + f"Server started, listening on port: {SERVICE_PORT}")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
