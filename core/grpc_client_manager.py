# core/grpc_client_manager.py
import sys
sys.path.append('d:/pythonKurs')  # Добавляем путь к корню проекта

from grpc_services.user_service.client import UserClient
from grpc_services.car_service.client import CarClient
from grpc_services.booking_service.client import BookingClient
from grpc_services.payment_service.client import PaymentClient

class GRPCClientManager:
    def __init__(self):
        self.user_client = UserClient()
        self.car_client = CarClient()
        self.booking_client = BookingClient()
        self.payment_client = PaymentClient()
