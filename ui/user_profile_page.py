from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout, QMessageBox, QSpacerItem, QSizePolicy, QDialog, QLineEdit, QFormLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor, QPalette


class UserProfilePage(QWidget):
    def __init__(self, main_window, user_client):
        super().__init__()
        self.main_window = main_window
        self.user_client = user_client

        # Установка светлого фона
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#FFFFFF"))
        self.setPalette(palette)

        # Главный layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.setContentsMargins(50, 30, 50, 30)

        # Заголовок
        self.label = QLabel("User Profile")
        self.label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("color: black; margin-bottom: 20px;")

        # GridLayout для информации о пользователе
        self.info_layout = QGridLayout()
        self.info_layout.setSpacing(10)

        # Метки для информации пользователя
        self.email_label = QLabel("Email: Not Available")
        self.phone_label = QLabel("Phone: Not Available")
        self.name_label = QLabel("Name: Not Available")
        self.passport_label = QLabel("Passport: Not Available")
        self.license_label = QLabel("License: Not Available")
        self.location_label = QLabel("Location: Not Available")
        self.license_category_label = QLabel("Driver License Categories: Not Available")
        self.approved_label = QLabel("Approved: Not Available")

        # Добавление меток в таблицу
        self.add_info_row("Email:", self.email_label, 0)
        self.add_info_row("Phone:", self.phone_label, 1)
        self.add_info_row("Name:", self.name_label, 2)
        self.add_info_row("Passport:", self.passport_label, 3)
        self.add_info_row("License:", self.license_label, 4)
        self.add_info_row("Location:", self.location_label, 5)
        self.add_info_row("Driver License Categories:", self.license_category_label, 6)
        self.add_info_row("Approved:", self.approved_label, 7)

        # Создание кнопок
        self.update_button = QPushButton("Update Details")
        self.logout_button = QPushButton("Logout")
        self.view_bookings_button = QPushButton("View Bookings")
        self.view_cars_button = QPushButton("View Available Cars")  # Видна только администратору

        # Применяем стили кнопок
        buttons = [self.update_button, self.logout_button, self.view_bookings_button, self.view_cars_button]
        for button in buttons:
            button.setStyleSheet(self.button_style())

        # GridLayout для кнопок
        self.button_layout = QGridLayout()
        self.button_layout.setSpacing(15)

        # Добавляем кнопки в сетку
        self.button_layout.addWidget(self.update_button, 0, 0)
        self.button_layout.addWidget(self.logout_button, 0, 1)
        self.button_layout.addWidget(self.view_bookings_button, 1, 0)
        self.button_layout.addWidget(self.view_cars_button, 1, 1)

        # Добавляем всё в главный layout
        self.main_layout.addWidget(self.label)
        self.main_layout.addLayout(self.info_layout)
        self.main_layout.addSpacing(20)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addStretch()
        self.setLayout(self.main_layout)

        # Привязка сигналов
        self.update_button.clicked.connect(self.open_update_dialog)
        self.logout_button.clicked.connect(self.logout)
        self.view_bookings_button.clicked.connect(self.go_to_booking)
        self.view_cars_button.clicked.connect(self.go_to_car_list)

        # Обновление информации пользователя
        self.update_user_info()

    def add_info_row(self, label_text, value_label, row):
        """Добавляет строку с информацией в таблицу."""
        label = QLabel(label_text)
        label.setStyleSheet("color: black; font-weight: bold;")
        value_label.setStyleSheet("color: black;")
        self.info_layout.addWidget(label, row, 0)
        self.info_layout.addWidget(value_label, row, 1)

    def button_style(self):
        """Стиль для кнопок."""
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

    def update_user_info(self):
        """Обновляет информацию пользователя и скрывает кнопку для обычных пользователей."""
        user_id = self.main_window.get_current_user()
        if user_id:
            response = self.user_client.get_user_details(user_id)

            # Функция для проверки и отображения данных
            def get_display_value(value):
                return value if value and value != "None" else "Not Available"

            self.label.setText(f"User Profile (ID: {user_id})")
            self.email_label.setText(get_display_value(response.email))
            self.phone_label.setText(get_display_value(response.phone))
            self.name_label.setText(get_display_value(response.name))
            self.passport_label.setText(get_display_value(response.passport))
            self.license_label.setText(get_display_value(response.license))
            self.location_label.setText(get_display_value(response.location))

            driver_license_categories = ', '.join(response.driver_license_categories) if response.driver_license_categories else "Not Available"
            self.license_category_label.setText(driver_license_categories)

            approved = "Confirmed" if response.approved == "True" else "Not Confirmed"
            self.approved_label.setText(approved)

            # Показываем или скрываем кнопку просмотра машин
            self.view_cars_button.setVisible(int(user_id) == 4)
        else:
            #QMessageBox.warning(self, "Error", "No user ID found!")
            print("hi")

    def go_to_car_list(self):
        self.main_window.show_car_list_page()

    def go_to_booking(self):
        self.main_window.show_booking_page()

    def open_update_dialog(self):
        user_id = self.main_window.get_current_user()
        if user_id:
            dialog = UpdateUserDialog(self, user_id)
            dialog.exec()
        else:
            QMessageBox.warning(self, "Error", "No user ID found!")

    def logout(self):
        self.main_window.set_current_user(None)
        self.main_window.show_login_page()



class UpdateUserDialog(QDialog):
    def __init__(self, parent, user_id):
        super().__init__(parent)
        self.parent = parent
        self.user_id = user_id
        self.setWindowTitle("Update User Details")

        self.layout = QFormLayout()

        # Поля ввода
        self.passport_input = QLineEdit()
        self.license_input = QLineEdit()
        self.location_input = QLineEdit()
        self.driver_license_categories_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Добавление полей
        self.layout.addRow("Passport:", self.passport_input)
        self.layout.addRow("License:", self.license_input)
        self.layout.addRow("Location:", self.location_input)
        self.layout.addRow("Driver License Categories:", self.driver_license_categories_input)
        self.layout.addRow("Password (for verification):", self.password_input)

        # Кнопка обновления
        self.update_button = QPushButton("Update")
        self.update_button.setStyleSheet(parent.button_style())
        self.update_button.clicked.connect(self.update_user_details)
        self.layout.addWidget(self.update_button)

        self.setLayout(self.layout)

    def update_user_details(self):
        passport = self.passport_input.text()
        license = self.license_input.text()
        location = self.location_input.text()
        driver_license_categories = [c.strip() for c in self.driver_license_categories_input.text().split(",")]
        password = self.password_input.text()

        response = self.parent.user_client.update_user_details(
            self.user_id, passport, license, driver_license_categories, password, location
        )

        if response.success:
            QMessageBox.information(self, "Success", "User details updated successfully!")
            self.accept()
            self.parent.update_user_info()
        else:
            QMessageBox.warning(self, "Error", f"Failed to update details: {response.message}")
