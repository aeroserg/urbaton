# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import common_pb2 as common__pb2


class CommonServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Schools = channel.unary_unary(
                '/CommonService/Schools',
                request_serializer=common__pb2.SchoolsRequest.SerializeToString,
                response_deserializer=common__pb2.SchoolsResponse.FromString,
                )
        self.GetClass = channel.unary_unary(
                '/CommonService/GetClass',
                request_serializer=common__pb2.GetClassRequest.SerializeToString,
                response_deserializer=common__pb2.GetClassResponse.FromString,
                )
        self.GetEducationYear = channel.unary_unary(
                '/CommonService/GetEducationYear',
                request_serializer=common__pb2.GetEducationYearRequest.SerializeToString,
                response_deserializer=common__pb2.GetEducationYearResponse.FromString,
                )
        self.GetStudents = channel.unary_unary(
                '/CommonService/GetStudents',
                request_serializer=common__pb2.GetStudentsRequest.SerializeToString,
                response_deserializer=common__pb2.GetStudentsResponse.FromString,
                )
        self.GetTutor = channel.unary_unary(
                '/CommonService/GetTutor',
                request_serializer=common__pb2.GetTutorRequest.SerializeToString,
                response_deserializer=common__pb2.GetTutorResponse.FromString,
                )
        self.GetUser = channel.unary_unary(
                '/CommonService/GetUser',
                request_serializer=common__pb2.GetUsersRequest.SerializeToString,
                response_deserializer=common__pb2.GetUsersResponse.FromString,
                )
        self.GetTutorsStudent = channel.unary_unary(
                '/CommonService/GetTutorsStudent',
                request_serializer=common__pb2.GetTutorsStudentRequest.SerializeToString,
                response_deserializer=common__pb2.GetTutorsStudentResponse.FromString,
                )


class CommonServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Schools(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetClass(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEducationYear(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStudents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTutor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTutorsStudent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommonServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Schools': grpc.unary_unary_rpc_method_handler(
                    servicer.Schools,
                    request_deserializer=common__pb2.SchoolsRequest.FromString,
                    response_serializer=common__pb2.SchoolsResponse.SerializeToString,
            ),
            'GetClass': grpc.unary_unary_rpc_method_handler(
                    servicer.GetClass,
                    request_deserializer=common__pb2.GetClassRequest.FromString,
                    response_serializer=common__pb2.GetClassResponse.SerializeToString,
            ),
            'GetEducationYear': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEducationYear,
                    request_deserializer=common__pb2.GetEducationYearRequest.FromString,
                    response_serializer=common__pb2.GetEducationYearResponse.SerializeToString,
            ),
            'GetStudents': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStudents,
                    request_deserializer=common__pb2.GetStudentsRequest.FromString,
                    response_serializer=common__pb2.GetStudentsResponse.SerializeToString,
            ),
            'GetTutor': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTutor,
                    request_deserializer=common__pb2.GetTutorRequest.FromString,
                    response_serializer=common__pb2.GetTutorResponse.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=common__pb2.GetUsersRequest.FromString,
                    response_serializer=common__pb2.GetUsersResponse.SerializeToString,
            ),
            'GetTutorsStudent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTutorsStudent,
                    request_deserializer=common__pb2.GetTutorsStudentRequest.FromString,
                    response_serializer=common__pb2.GetTutorsStudentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CommonService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CommonService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Schools(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommonService/Schools',
            common__pb2.SchoolsRequest.SerializeToString,
            common__pb2.SchoolsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetClass(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommonService/GetClass',
            common__pb2.GetClassRequest.SerializeToString,
            common__pb2.GetClassResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEducationYear(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommonService/GetEducationYear',
            common__pb2.GetEducationYearRequest.SerializeToString,
            common__pb2.GetEducationYearResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStudents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommonService/GetStudents',
            common__pb2.GetStudentsRequest.SerializeToString,
            common__pb2.GetStudentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTutor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommonService/GetTutor',
            common__pb2.GetTutorRequest.SerializeToString,
            common__pb2.GetTutorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommonService/GetUser',
            common__pb2.GetUsersRequest.SerializeToString,
            common__pb2.GetUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTutorsStudent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommonService/GetTutorsStudent',
            common__pb2.GetTutorsStudentRequest.SerializeToString,
            common__pb2.GetTutorsStudentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
