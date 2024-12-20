# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_services.booking_service.booking_service_pb2  as booking__service__pb2


class BookingServiceStub(object):
    """Интерфейс BookingService
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBooking = channel.unary_unary(
                '/booking_service.BookingService/CreateBooking',
                request_serializer=booking__service__pb2.CreateBookingRequest.SerializeToString,
                response_deserializer=booking__service__pb2.CreateBookingResponse.FromString,
                )
        self.CheckAvailability = channel.unary_unary(
                '/booking_service.BookingService/CheckAvailability',
                request_serializer=booking__service__pb2.CheckAvailabilityRequest.SerializeToString,
                response_deserializer=booking__service__pb2.CheckAvailabilityResponse.FromString,
                )
        self.CancelBooking = channel.unary_unary(
                '/booking_service.BookingService/CancelBooking',
                request_serializer=booking__service__pb2.CancelBookingRequest.SerializeToString,
                response_deserializer=booking__service__pb2.GeneralResponse.FromString,
                )
        self.ProcessRequest = channel.unary_unary(
                '/booking_service.BookingService/ProcessRequest',
                request_serializer=booking__service__pb2.ThirdServiceRequest.SerializeToString,
                response_deserializer=booking__service__pb2.ThirdServiceResponse.FromString,
                )
        self.PaymentStarting = channel.unary_unary(
                '/booking_service.BookingService/PaymentStarting',
                request_serializer=booking__service__pb2.PaymentRequest.SerializeToString,
                response_deserializer=booking__service__pb2.PaymentResponse.FromString,
                )
        self.History = channel.unary_unary(
                '/booking_service.BookingService/History',
                request_serializer=booking__service__pb2.HistoryRequest.SerializeToString,
                response_deserializer=booking__service__pb2.HistoryResponse.FromString,
                )


class BookingServiceServicer(object):
    """Интерфейс BookingService
    """

    def CreateBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAvailability(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProcessRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PaymentStarting(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def History(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBooking': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBooking,
                    request_deserializer=booking__service__pb2.CreateBookingRequest.FromString,
                    response_serializer=booking__service__pb2.CreateBookingResponse.SerializeToString,
            ),
            'CheckAvailability': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAvailability,
                    request_deserializer=booking__service__pb2.CheckAvailabilityRequest.FromString,
                    response_serializer=booking__service__pb2.CheckAvailabilityResponse.SerializeToString,
            ),
            'CancelBooking': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelBooking,
                    request_deserializer=booking__service__pb2.CancelBookingRequest.FromString,
                    response_serializer=booking__service__pb2.GeneralResponse.SerializeToString,
            ),
            'ProcessRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessRequest,
                    request_deserializer=booking__service__pb2.ThirdServiceRequest.FromString,
                    response_serializer=booking__service__pb2.ThirdServiceResponse.SerializeToString,
            ),
            'PaymentStarting': grpc.unary_unary_rpc_method_handler(
                    servicer.PaymentStarting,
                    request_deserializer=booking__service__pb2.PaymentRequest.FromString,
                    response_serializer=booking__service__pb2.PaymentResponse.SerializeToString,
            ),
            'History': grpc.unary_unary_rpc_method_handler(
                    servicer.History,
                    request_deserializer=booking__service__pb2.HistoryRequest.FromString,
                    response_serializer=booking__service__pb2.HistoryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'booking_service.BookingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BookingService(object):
    """Интерфейс BookingService
    """

    @staticmethod
    def CreateBooking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/booking_service.BookingService/CreateBooking',
            booking__service__pb2.CreateBookingRequest.SerializeToString,
            booking__service__pb2.CreateBookingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAvailability(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/booking_service.BookingService/CheckAvailability',
            booking__service__pb2.CheckAvailabilityRequest.SerializeToString,
            booking__service__pb2.CheckAvailabilityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelBooking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/booking_service.BookingService/CancelBooking',
            booking__service__pb2.CancelBookingRequest.SerializeToString,
            booking__service__pb2.GeneralResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProcessRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/booking_service.BookingService/ProcessRequest',
            booking__service__pb2.ThirdServiceRequest.SerializeToString,
            booking__service__pb2.ThirdServiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PaymentStarting(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/booking_service.BookingService/PaymentStarting',
            booking__service__pb2.PaymentRequest.SerializeToString,
            booking__service__pb2.PaymentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def History(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/booking_service.BookingService/History',
            booking__service__pb2.HistoryRequest.SerializeToString,
            booking__service__pb2.HistoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
