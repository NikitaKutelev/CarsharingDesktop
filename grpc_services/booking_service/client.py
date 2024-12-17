import grpc
from .booking_service_pb2 import (
    CreateBookingRequest, CheckAvailabilityRequest, ThirdServiceRequest, HistoryRequest, PaymentRequest
)
from .booking_service_pb2_grpc import BookingServiceStub

class BookingClient:
    def __init__(self, address="localhost:8002"):
        self.channel = grpc.insecure_channel(address)
        self.stub = BookingServiceStub(self.channel)

    def create_booking(self, user_id, car_id, start_time, end_time):
        """Создание бронирования автомобиля"""
        request = CreateBookingRequest(user_id=user_id, car_id=car_id, start_time=start_time, end_time=end_time)
        return self.stub.CreateBooking(request)

    def get_available_cars(self, user_id):
        """Получение списка доступных автомобилей для пользователя"""
        request = ThirdServiceRequest(user_id=user_id)
        return self.stub.ProcessRequest(request)

    def start_payment(self, booking_id):
        """Запуск процесса оплаты после завершения аренды"""
        request = PaymentRequest(booking_id=booking_id)
        return self.stub.PaymentStarting(request)
    
    def get_booking_history(self, user_id):
        """Получение истории заказов для пользователя"""
        request = HistoryRequest(user_id=user_id)
        response = self.stub.History(request)
        
        if response.books:
            return response.books  # Возвращаем список заказов (Books)
        else:
            return "Нет истории заказов для этого пользователя."