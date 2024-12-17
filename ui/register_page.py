from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QHBoxLayout, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPalette, QColor
import grpc

class RegisterPage(QWidget):
    def __init__(self, main_window, user_client):
        super().__init__()
        self.main_window = main_window
        self.user_client = user_client

        # Установка светлого фона
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#FFFFFF"))
        self.setPalette(palette)

        # Основной layout для центрирования контейнера
        main_layout = QHBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Контейнер с фиксированной шириной
        container = QFrame()
        container.setFixedSize(400, 500)
        container.setStyleSheet("background-color: white; border: 1px solid #D3D3D3; border-radius: 10px;")

        # Layout для содержимого контейнера
        self.layout = QVBoxLayout(container)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.setSpacing(15)

        # Заголовок
        self.label = QLabel("Register")
        self.label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.label.setStyleSheet("color: black;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Поле ввода Email
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet(self.input_style())

        # Поле ввода Phone
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Phone")
        self.phone_input.setStyleSheet(self.input_style())

        # Поле ввода Name
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.name_input.setStyleSheet(self.input_style())

        # Поле ввода Password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(self.input_style())

        # Кнопка "Register"
        self.register_button = QPushButton("Register")
        self.register_button.setStyleSheet(self.button_style())
        self.register_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Кнопка "Back to Login"
        self.back_button = QPushButton("Back to Login")
        self.back_button.setStyleSheet(self.button_style())
        self.back_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Добавление элементов в контейнер
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.phone_input)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.register_button)
        self.layout.addWidget(self.back_button)

        # Добавляем контейнер в центр основного layout
        main_layout.addWidget(container)

        # Сигналы для кнопок
        self.register_button.clicked.connect(self.register)
        self.back_button.clicked.connect(self.go_to_login)

    def input_style(self):
        """Стиль для полей ввода"""
        return """
            QLineEdit {
                background-color: white;
                border: 1px solid #3637f8;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
                color: black;
            }
            QLineEdit:focus {
                border: 1px solid #5a5bf5;
            }
        """

    def button_style(self):
        """Стиль для кнопок"""
        return """
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
        """

    def register(self):
        email = self.email_input.text().strip()
        phone = self.phone_input.text().strip()
        name = self.name_input.text().strip()
        password = self.password_input.text().strip()

        try:
            response = self.user_client.register(email, phone, name, password)
            if response.success:
                QMessageBox.information(self, "Success", "Registration successful!")
                self.main_window.show_login_page()
            else:
                QMessageBox.warning(self, "Failed", response.message)
        except grpc._channel._InactiveRpcError:
            QMessageBox.critical(self, "Error", "Failed to connect to the server.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def go_to_login(self):
        self.main_window.show_login_page()
