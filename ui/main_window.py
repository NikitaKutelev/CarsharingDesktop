from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from ui.login_page import LoginPage
from ui.register_page import RegisterPage
from ui.booking_page import BookingPage
from ui.car_list_page import CarListPage
from ui.payment_page import PaymentPage
from ui.user_profile_page import UserProfilePage

class MainWindow(QMainWindow):
    def __init__(self, user_client, car_client, booking_client, payment_client):
        super().__init__()

        self.user_client = user_client
        self.car_client = car_client
        self.booking_client = booking_client
        self.payment_client = payment_client
        self.current_user_id = None

        self.setWindowTitle("Car Rental Service")
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_page = LoginPage(self, self.user_client)
        self.register_page = RegisterPage(self, self.user_client)
        self.booking_page = BookingPage(self, self.booking_client, self.payment_client)
        self.car_list_page = CarListPage(self, self.car_client)
        self.payment_page = PaymentPage(self, self.payment_client)
        self.user_profile_page = UserProfilePage(self, self.user_client)

        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.register_page)
        self.stacked_widget.addWidget(self.booking_page)
        self.stacked_widget.addWidget(self.car_list_page)
        self.stacked_widget.addWidget(self.payment_page)
        self.stacked_widget.addWidget(self.user_profile_page)
        self.show_login_page()

    def set_current_user(self, user_id):
        self.current_user_id = user_id

    def get_current_user(self):
        return self.current_user_id

    def show_login_page(self):
        self.stacked_widget.setCurrentWidget(self.login_page)

    def show_register_page(self):
        self.stacked_widget.setCurrentWidget(self.register_page)

    def show_booking_page(self):
        self.stacked_widget.setCurrentWidget(self.booking_page)

    def show_car_list_page(self):
        self.stacked_widget.setCurrentWidget(self.car_list_page)

    def show_payment_page(self):
        self.stacked_widget.setCurrentWidget(self.payment_page)

    def show_user_profile_page(self):
        self.user_profile_page.update_user_info()
        self.stacked_widget.setCurrentWidget(self.user_profile_page)