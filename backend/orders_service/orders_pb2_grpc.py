# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import orders_pb2 as orders__pb2


class OrderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EducationOrder = channel.unary_unary(
                '/OrderService/EducationOrder',
                request_serializer=orders__pb2.EducationOrderRequest.SerializeToString,
                response_deserializer=orders__pb2.EducationOrderResponse.FromString,
                )
        self.GetOrder = channel.unary_unary(
                '/OrderService/GetOrder',
                request_serializer=orders__pb2.GetOrderRequest.SerializeToString,
                response_deserializer=orders__pb2.GetOrderResponse.FromString,
                )


class OrderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def EducationOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EducationOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.EducationOrder,
                    request_deserializer=orders__pb2.EducationOrderRequest.FromString,
                    response_serializer=orders__pb2.EducationOrderResponse.SerializeToString,
            ),
            'GetOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrder,
                    request_deserializer=orders__pb2.GetOrderRequest.FromString,
                    response_serializer=orders__pb2.GetOrderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'OrderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def EducationOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrderService/EducationOrder',
            orders__pb2.EducationOrderRequest.SerializeToString,
            orders__pb2.EducationOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrderService/GetOrder',
            orders__pb2.GetOrderRequest.SerializeToString,
            orders__pb2.GetOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)