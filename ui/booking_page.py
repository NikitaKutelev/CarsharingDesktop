from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QTextEdit, QDialog, QDialogButtonBox
)
from PyQt6.QtCore import QDateTime
import grpc

class BookingPage(QWidget):
    def __init__(self, main_window, booking_client, payment_client):
        super().__init__()
        self.main_window = main_window
        self.booking_client = booking_client
        self.payment_client = payment_client

        self.booking_id = None  # Изначально нет активного бронирования
        # Layout
        self.layout = QVBoxLayout()
        self.label = QLabel("Booking")
        self.available_cars_label = QLabel("Available Cars:")
        self.available_cars_text = QTextEdit()
        self.available_cars_text.setReadOnly(True)

        self.car_id_input = QLineEdit()
        self.car_id_input.setPlaceholderText("Car ID")

        # Поле для времени аренды
        self.duration_label = QLabel("Rental Duration (Hours):")
        self.duration_input = QLineEdit()
        self.duration_input.setPlaceholderText("Enter duration in hours")

        # Кнопки
        self.load_cars_button = QPushButton("Load Available Cars")
        self.book_button = QPushButton("Book")
        self.finish_booking_button = QPushButton("Finish Booking and Pay")
        self.back_button = QPushButton("Back to Profile")
        self.view_history_button = QPushButton("View Booking History")

        # Применение стилей
        self.button_style(self.load_cars_button)
        self.button_style(self.book_button)
        self.button_style(self.finish_booking_button)
        self.button_style(self.back_button)
        self.button_style(self.view_history_button)

        # Добавление виджетов в layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.available_cars_label)
        self.layout.addWidget(self.available_cars_text)
        self.layout.addWidget(self.load_cars_button)
        self.layout.addWidget(self.car_id_input)
        self.layout.addWidget(self.duration_label)
        self.layout.addWidget(self.duration_input)
        self.layout.addWidget(self.book_button)
        self.layout.addWidget(self.finish_booking_button)
        self.layout.addWidget(self.view_history_button)
        self.layout.addWidget(self.back_button)
        self.setLayout(self.layout)

        # Соединение сигналов с методами
        self.load_cars_button.clicked.connect(self.load_available_cars)
        self.book_button.clicked.connect(self.book)
        self.finish_booking_button.clicked.connect(self.finish_booking)
        self.back_button.clicked.connect(self.go_to_profile)
        self.view_history_button.clicked.connect(self.view_history)

        # Изначально кнопка "Finish Booking" не доступна
        self.finish_booking_button.setEnabled(False)

    def button_style(self, button):
        """Применение стилей к кнопкам"""
        button.setStyleSheet("""
            QPushButton {
                background-color: #3637f8;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #5a5bf5;
            }
            QPushButton:pressed {
                background-color: #2c2ed0;
            }
        """)

    def load_available_cars(self):
        """Получает и выводит список доступных автомобилей"""
        user_id = self.main_window.get_current_user()
        try:
            response = self.booking_client.get_available_cars(user_id)
            if response.cars:
                cars_info = [
                    f"ID: {car.car_id}, Brand: {car.brand}, Model: {car.model}, "
                    f"Price per Hour: {car.price_per_hour}, Number: {car.gos_num}"
                    for car in response.cars
                ]
                self.available_cars_text.setText("\n".join(cars_info))
            else:
                self.available_cars_text.setText("No cars available at the moment.")
        except grpc._channel._InactiveRpcError:
            QMessageBox.critical(self, "Error", "Failed to connect to the server.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def book(self):
        """Создание бронирования автомобиля с автоматическим временем старта"""
        car_id = self.car_id_input.text().strip()
        duration = self.duration_input.text().strip()
        user_id = self.main_window.get_current_user()

        # Проверка корректности времени аренды
        if not duration.isdigit() or int(duration) <= 0:
            QMessageBox.warning(self, "Input Error", "Rental duration must be a positive number.")
            return

        # Получаем текущее время и рассчитываем конец аренды
        start_time = QDateTime.currentDateTime()
        duration_hours = int(duration)
        end_time = start_time.addSecs(duration_hours * 3600)

        start_time_str = start_time.toString("yyyy-MM-dd HH:mm:ss")
        end_time_str = end_time.toString("yyyy-MM-dd HH:mm:ss")

        try:
            response = self.booking_client.create_booking(user_id, car_id, start_time_str, end_time_str)
            if response.success:
                QMessageBox.information(self, "Success", f"Booking created: {response.booking_id}\n"
                                                         f"Start Time: {start_time_str}\n"
                                                         f"End Time: {end_time_str}")
                self.booking_id = response.booking_id
                self.finish_booking_button.setEnabled(True)  # Активируем кнопку "Finish Booking"
                self.book_button.setEnabled(False)  # Делаем кнопку "Book" недоступной
            else:
                QMessageBox.warning(self, "Failed", response.message)
        except grpc._channel._InactiveRpcError:
            QMessageBox.critical(self, "Error", "Failed to connect to the server.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def finish_booking(self):
        """Завершение бронирования и переход к оплате"""
        booking_id = self.booking_id  # Установите актуальный ID бронирования
        try:
            # Запуск процесса оплаты
            response = self.booking_client.start_payment(booking_id)
            if response.success:
                self.finish_booking_button.setEnabled(False) 
                self.book_button.setEnabled(True)  
                self.show_payment_dialog(booking_id, response.message)
            else:
                QMessageBox.warning(self, "Payment Error", "Failed to start payment process.")
        except grpc._channel._InactiveRpcError:
            QMessageBox.critical(self, "Error", "Failed to connect to the server.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def show_payment_dialog(self, booking_id, message):
        """Показать диалоговое окно для ввода платежных данных"""
        dialog = PaymentDialog(self.payment_client, booking_id, message)
        dialog.exec()

    def go_to_profile(self):
        """Переход к странице профиля"""
        self.main_window.show_user_profile_page()

    def view_history(self):
        """Открытие диалогового окна для просмотра истории заказов"""
        user_id = self.main_window.get_current_user()
        try:
            response = self.booking_client.get_booking_history(user_id)
            dialog = HistoryDialog(response)
            dialog.exec()
        except grpc._channel._InactiveRpcError:
            QMessageBox.critical(self, "Error", "Failed to connect to the server.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")


class HistoryDialog(QDialog):
    def __init__(self, history_data):
        super().__init__()
        self.setWindowTitle("Booking History")
        self.setGeometry(100, 100, 400, 300)

        # Layout for history dialog
        layout = QVBoxLayout()

        self.history_text = QTextEdit(self)
        self.history_text.setReadOnly(True)
        if history_data:
            history_info = [
                f"Car: {entry.car}, Date: {entry.date}, Full Payment: {entry.full_payment}"
                for entry in history_data
            ]
            self.history_text.setText("\n".join(history_info))
        else:
            self.history_text.setText("No booking history found.")

        layout.addWidget(self.history_text)

        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)

        self.setLayout(layout)


class PaymentDialog(QDialog):
    def __init__(self, payment_client, booking_id=None, message=""):
        super().__init__()
        self.payment_client = payment_client
        self.booking_id = booking_id
        self.message = message

        self.setWindowTitle("Оплата аренды")
        self.setGeometry(100, 100, 300, 200)

        # Layout for payment dialog
        self.layout = QVBoxLayout()

        self.card_input = QLineEdit(self)
        self.card_input.setPlaceholderText("Введите номер карты")
        self.layout.addWidget(self.card_input)

        self.pay_button = QPushButton("Оплатить")
        self.pay_button.clicked.connect(self.process_payment)
        self.button_style(self.pay_button)
        self.layout.addWidget(self.pay_button)

        self.setLayout(self.layout)

    def button_style(self, button):
        """Применение стилей к кнопкам"""
        button.setStyleSheet("""
            QPushButton {
                background-color: #3637f8;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #5a5bf5;
            }
            QPushButton:pressed {
                background-color: #2c2ed0;
            }
        """)

    def process_payment(self):
        """Обработка платежа"""
        card_info = self.card_input.text()
        if card_info:  # Если введены данные карты
            try:
                transaction_id = self.message.split('/')[-1]
                self.confirm_payment(transaction_id)
            except grpc._channel._InactiveRpcError:
                QMessageBox.critical(self, "Error", "Failed to connect to the payment server.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def confirm_payment(self, transaction_id):
        """Подтверждение успешной оплаты"""
        response = self.payment_client.confirm_payment(transaction_id)
        if response.success:
            QMessageBox.information(self, "Success", "Payment successful!")
            self.accept()  # Закрыть окно оплаты
        else:
            QMessageBox.warning(self, "Payment Error", "Payment confirmation failed.")
