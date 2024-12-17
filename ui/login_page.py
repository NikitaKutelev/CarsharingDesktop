from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QHBoxLayout, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPalette, QColor
import grpc

class LoginPage(QWidget):
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
        container.setFixedSize(400, 400)
        container.setStyleSheet("background-color: white; border: 1px solid #D3D3D3; border-radius: 10px;")

        # Layout для содержимого контейнера
        self.layout = QVBoxLayout(container)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.setSpacing(15)

        # Заголовок
        self.label = QLabel("Login")
        self.label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.label.setStyleSheet("color: black;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Поле ввода логина
        self.credential_input = QLineEdit()
        self.credential_input.setPlaceholderText("Email or Phone")
        self.credential_input.setStyleSheet(self.input_style())

        # Поле ввода пароля
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(self.input_style())

        # Кнопка "Login"
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet(self.button_style())
        self.login_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Кнопка "Register"
        self.register_button = QPushButton("Register")
        self.register_button.setStyleSheet(self.button_style())
        self.register_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Добавление элементов в контейнер
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.credential_input)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.register_button)

        # Добавляем контейнер в центр основного layout
        main_layout.addWidget(container)

        # Сигналы для кнопок
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.go_to_register)

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

    def login(self):
        credential = self.credential_input.text().strip()
        password = self.password_input.text().strip()

        try:
            response = self.user_client.login(credential, password)
            if response.success:
                self.main_window.set_current_user(response.user_id)
                print(f"Setting current user ID LOGIN: {response.user_id}")
                self.main_window.show_user_profile_page()
            else:
                QMessageBox.warning(self, "Login Failed", response.message)
        except grpc._channel._InactiveRpcError as e:
            QMessageBox.warning(self, "Login Failed", "Invalid credentials. Please check your login details.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def go_to_register(self):
        self.main_window.show_register_page()
