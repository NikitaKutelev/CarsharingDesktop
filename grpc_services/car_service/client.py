import grpc
from .car_service_pb2 import ListCarsRequest, FindCarsRequest, AddCarRequest, DeleteCarRequest, UpdateCarStatusRequest, GetCarDetailsRequest
from .car_service_pb2_grpc import CarServiceStub

class CarClient:
    def __init__(self, address="localhost:50059"):
        self.channel = grpc.insecure_channel(address)
        self.stub = CarServiceStub(self.channel)

    def list_cars(self):
        request = ListCarsRequest()
        return self.stub.ListCars(request)

    def find_cars(self, location, categories):
        request = FindCarsRequest(location=location, driver_license_categories=categories)
        return self.stub.FindCarsByLocationAndCategory(request)

    def add_car(self, gos_num, brand, model, price_per_hour, location, status, driver_license_category):
        request = AddCarRequest(
            gos_num=gos_num,
            brand=brand,
            model=model,
            price_per_hour=price_per_hour,
            location=location,
            status=status,
            driver_license_category=driver_license_category
        )
        return self.stub.AddCar(request)

    def delete_car(self, car_id):
        request = DeleteCarRequest(car_id=car_id)
        return self.stub.DeleteCar(request)

    def update_car_status(self, car_id, status):
        request = UpdateCarStatusRequest(car_id=car_id, status=status)
        return self.stub.UpdateCarStatus(request)
    
    def get_car_details(self, car_id):
        request = GetCarDetailsRequest(car_id=car_id)
        return self.stub.GetCarDetails(request)
