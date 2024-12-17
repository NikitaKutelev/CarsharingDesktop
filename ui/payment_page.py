from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
import grpc

class PaymentPage(QWidget):
    def __init__(self, main_window, payment_client):
        super().__init__()
        self.main_window = main_window
        self.payment_client = payment_client

        self.layout = QVBoxLayout()
        self.label = QLabel("Payment")
        self.booking_id_input = QLineEdit()
        self.booking_id_input.setPlaceholderText("Booking ID")
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Amount")
        self.pay_button = QPushButton("Pay")
        self.back_button = QPushButton("Back to Profile")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.booking_id_input)
        self.layout.addWidget(self.amount_input)
        self.layout.addWidget(self.pay_button)
        self.layout.addWidget(self.back_button)
        self.setLayout(self.layout)

        self.pay_button.clicked.connect(self.pay)
        self.back_button.clicked.connect(self.go_to_user_profile)

    def pay(self):
        booking_id = self.booking_id_input.text().strip()
        amount = float(self.amount_input.text().strip())

        try:
            response = self.payment_client.process_payment("user_id_placeholder", amount, booking_id)
            if response.success:
                QMessageBox.information(self, "Success", "Payment processed successfully!")
                self.main_window.show_user_profile_page()
            else:
                QMessageBox.warning(self, "Failed", "Payment failed. Try again.")
        except grpc._channel._InactiveRpcError:
            QMessageBox.critical(self, "Error", "Failed to connect to the server.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def go_to_user_profile(self):
        self.main_window.show_user_profile_page()
