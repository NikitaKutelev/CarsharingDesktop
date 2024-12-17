import grpc
from .payment_service_pb2 import PaymentRequest, PayedRequest
from .payment_service_pb2_grpc import PaymentServiceStub

class PaymentClient:
    def __init__(self, address="localhost:8004"):
        self.channel = grpc.insecure_channel(address)
        self.stub = PaymentServiceStub(self.channel)

    def process_payment(self, user_id, amount, booking_id):
        """Обработка платежа (запуск процесса оплаты)"""
        request = PaymentRequest(user_id=user_id, amount=amount, booking_id=booking_id)
        return self.stub.ProcessPayment(request)

    def confirm_payment(self, transaction_id):
        """Подтверждение успешной оплаты"""
        request = PayedRequest(transaction_id=transaction_id)
        return self.stub.Payed(request)
