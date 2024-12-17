import grpc
from pythonKurs.grpc_services.user_service.user_service_pb2 import LoginRequest, RegisterRequest, GeneralResponse, LoginResponse, GetUserDetailsRequest, GetUserDetailsResponse, UpdateUserDetailsRequest
from pythonKurs.grpc_services.user_service.user_service_pb2_grpc import UserServiceStub

class UserClient:
    def __init__(self, address="localhost:50051"):
        self.channel = grpc.insecure_channel(address)
        self.stub = UserServiceStub(self.channel)

    def login(self, credential, password):  # Вход
        request = LoginRequest(credential=credential, password=password)
        return self.stub.Login(request)

    def register(self, email, phone, name, password):  # Регистрация
        request = RegisterRequest(email=email, phone=phone, name=name, password=password)
        return self.stub.RegisterUser(request)

    def get_user_details(self, user_id):  # Получение данных о пользователе (email, телефон, паспорт, лицензия и другие данные)
        request = GetUserDetailsRequest(user_id=user_id)
        response = self.stub.GetUserDetails(request)
        return response

    def update_user_details(self, user_id, passport, license, driver_license_categories, password, location):
        # Обновление данных пользователя
        request = UpdateUserDetailsRequest(
            user_id=user_id,
            passport=passport,
            license=license,
            driver_license_categories=driver_license_categories,
            password=password,
            location=location
        )
        response = self.stub.UpdateUserDetails(request)
        return response
