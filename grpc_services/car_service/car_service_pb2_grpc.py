# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_services.car_service.car_service_pb2 as car__service__pb2


class CarServiceStub(object):
    """Определение сервиса CarService
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddCar = channel.unary_unary(
                '/car_service.CarService/AddCar',
                request_serializer=car__service__pb2.AddCarRequest.SerializeToString,
                response_deserializer=car__service__pb2.AddCarResponse.FromString,
                )
        self.ListCars = channel.unary_unary(
                '/car_service.CarService/ListCars',
                request_serializer=car__service__pb2.ListCarsRequest.SerializeToString,
                response_deserializer=car__service__pb2.ListCarsResponse.FromString,
                )
        self.UpdateCarStatus = channel.unary_unary(
                '/car_service.CarService/UpdateCarStatus',
                request_serializer=car__service__pb2.UpdateCarStatusRequest.SerializeToString,
                response_deserializer=car__service__pb2.UpdateCarStatusResponse.FromString,
                )
        self.GetCarDetails = channel.unary_unary(
                '/car_service.CarService/GetCarDetails',
                request_serializer=car__service__pb2.GetCarDetailsRequest.SerializeToString,
                response_deserializer=car__service__pb2.GetCarDetailsResponse.FromString,
                )
        self.DeleteCar = channel.unary_unary(
                '/car_service.CarService/DeleteCar',
                request_serializer=car__service__pb2.DeleteCarRequest.SerializeToString,
                response_deserializer=car__service__pb2.DeleteCarResponse.FromString,
                )
        self.FindCarsByLocationAndCategory = channel.unary_unary(
                '/car_service.CarService/FindCarsByLocationAndCategory',
                request_serializer=car__service__pb2.FindCarsRequest.SerializeToString,
                response_deserializer=car__service__pb2.FindCarsResponse.FromString,
                )


class CarServiceServicer(object):
    """Определение сервиса CarService
    """

    def AddCar(self, request, context):
        """Добавить автомобиль
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCars(self, request, context):
        """Получить список всех автомобилей
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCarStatus(self, request, context):
        """Обновить статус автомобиля
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCarDetails(self, request, context):
        """Получить детали автомобиля
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCar(self, request, context):
        """Удалить автомобиль
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindCarsByLocationAndCategory(self, request, context):
        """Поиск автомобилей по локации и категории прав
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CarServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddCar': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCar,
                    request_deserializer=car__service__pb2.AddCarRequest.FromString,
                    response_serializer=car__service__pb2.AddCarResponse.SerializeToString,
            ),
            'ListCars': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCars,
                    request_deserializer=car__service__pb2.ListCarsRequest.FromString,
                    response_serializer=car__service__pb2.ListCarsResponse.SerializeToString,
            ),
            'UpdateCarStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCarStatus,
                    request_deserializer=car__service__pb2.UpdateCarStatusRequest.FromString,
                    response_serializer=car__service__pb2.UpdateCarStatusResponse.SerializeToString,
            ),
            'GetCarDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCarDetails,
                    request_deserializer=car__service__pb2.GetCarDetailsRequest.FromString,
                    response_serializer=car__service__pb2.GetCarDetailsResponse.SerializeToString,
            ),
            'DeleteCar': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCar,
                    request_deserializer=car__service__pb2.DeleteCarRequest.FromString,
                    response_serializer=car__service__pb2.DeleteCarResponse.SerializeToString,
            ),
            'FindCarsByLocationAndCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.FindCarsByLocationAndCategory,
                    request_deserializer=car__service__pb2.FindCarsRequest.FromString,
                    response_serializer=car__service__pb2.FindCarsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'car_service.CarService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CarService(object):
    """Определение сервиса CarService
    """

    @staticmethod
    def AddCar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/car_service.CarService/AddCar',
            car__service__pb2.AddCarRequest.SerializeToString,
            car__service__pb2.AddCarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCars(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/car_service.CarService/ListCars',
            car__service__pb2.ListCarsRequest.SerializeToString,
            car__service__pb2.ListCarsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCarStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/car_service.CarService/UpdateCarStatus',
            car__service__pb2.UpdateCarStatusRequest.SerializeToString,
            car__service__pb2.UpdateCarStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCarDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/car_service.CarService/GetCarDetails',
            car__service__pb2.GetCarDetailsRequest.SerializeToString,
            car__service__pb2.GetCarDetailsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/car_service.CarService/DeleteCar',
            car__service__pb2.DeleteCarRequest.SerializeToString,
            car__service__pb2.DeleteCarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindCarsByLocationAndCategory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/car_service.CarService/FindCarsByLocationAndCategory',
            car__service__pb2.FindCarsRequest.SerializeToString,
            car__service__pb2.FindCarsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
