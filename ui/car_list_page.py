from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QListWidget, QLabel, QMessageBox, 
    QDialog, QFormLayout, QLineEdit, QDoubleSpinBox, QListWidgetItem
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor, QPalette


class CarListPage(QWidget):
    def __init__(self, main_window, car_client):
        super().__init__()
        self.main_window = main_window
        self.car_client = car_client

        # Установка светлого фона
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#F0F0F0"))
        self.setPalette(palette)

        # Главный layout
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.setContentsMargins(40, 20, 40, 20)

        # Заголовок
        self.label = QLabel("Available Cars")
        self.label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("color: #333333; margin-bottom: 20px;")

        # Список автомобилей
        self.car_list = QListWidget()
        self.car_list.setStyleSheet("""
            QListWidget {
                border: 1px solid #D3D3D3;
                border-radius: 5px;
                font-size: 14px;
                padding: 5px;
                background-color: #FFFFFF;
            }
        """)

        # Кнопки
        self.refresh_button = QPushButton("Refresh List")
        self.delete_button = QPushButton("Delete Selected Car")
        self.add_button = QPushButton("Add New Car")
        self.edit_button = QPushButton("Edit Selected Car")
        self.edit_details_button = QPushButton("Check Details")
        self.back_button = QPushButton("Back to Profile")

        # Стили для кнопок
        self.button_style()

        # Добавляем элементы в layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.car_list)
        self.layout.addWidget(self.refresh_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.edit_details_button)
        self.layout.addWidget(self.back_button)
        self.setLayout(self.layout)

        # Привязка сигналов
        self.refresh_button.clicked.connect(self.load_cars)
        self.delete_button.clicked.connect(self.delete_car)
        self.add_button.clicked.connect(self.add_car)
        self.edit_button.clicked.connect(self.edit_car)
        self.edit_details_button.clicked.connect(self.view_car_details)
        self.back_button.clicked.connect(self.go_to_user_profile)

        # Загрузка списка автомобилей
        self.load_cars()

    def button_style(self):
        """Применение стилей для кнопок."""
        buttons = [self.refresh_button, self.delete_button, self.add_button, 
                   self.edit_button, self.edit_details_button, self.back_button]
        for button in buttons:
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

    def go_to_user_profile(self):
        self.main_window.show_user_profile_page()

    def load_cars(self):
        try:
            response = self.car_client.list_cars()
            self.populate_car_list(response.cars)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load cars: {str(e)}")

    def populate_car_list(self, cars):
        self.car_list.clear()
        for car in cars:
            item = f"{car.brand} {car.model} - ${car.price_per_hour}/hour"
            list_item = QListWidgetItem(item)
            list_item.setData(Qt.ItemDataRole.UserRole, car.car_id)
            self.car_list.addItem(list_item)

    def delete_car(self):
        selected_item = self.car_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "No Selection", "Please select a car to delete.")
            return
        
        car_id = selected_item.data(Qt.ItemDataRole.UserRole)

        try:
            response = self.car_client.delete_car(car_id)
            if response.success:
                QMessageBox.information(self, "Success", "Car deleted successfully")
                self.load_cars()  # Перезагрузить список
            else:
                QMessageBox.critical(self, "Error", response.message)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to delete car: {str(e)}")

    def add_car(self):
        add_car_dialog = AddCarDialog(self.car_client)
        add_car_dialog.exec()

    def edit_car(self):
        selected_item = self.car_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "No Selection", "Please select a car to edit.")
            return

        car_id = selected_item.data(Qt.ItemDataRole.UserRole)
        edit_car_dialog = EditCarDialog(self.car_client, car_id)
        edit_car_dialog.exec()
        
    def view_car_details(self):
        selected_item = self.car_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "No Selection", "Please select a car to view details.")
            return

        car_id = selected_item.data(Qt.ItemDataRole.UserRole)

        try:
            response = self.car_client.get_car_details(car_id)
            car_details_dialog = CarDetailsDialog(response)
            car_details_dialog.exec()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load car details: {str(e)}")


class AddCarDialog(QDialog):
    def __init__(self, car_client):
        super().__init__()
        self.car_client = car_client
        self.setWindowTitle("Add New Car")

        # Основной layout
        self.layout = QFormLayout()

        # Поля ввода
        self.gos_num_input = QLineEdit()
        self.brand_input = QLineEdit()
        self.model_input = QLineEdit()
        self.price_input = QDoubleSpinBox()
        self.location_input = QLineEdit()
        self.status_input = QLineEdit()
        self.driver_license_input = QLineEdit()

        # Добавляем поля в форму
        self.layout.addRow("Gos Number", self.gos_num_input)
        self.layout.addRow("Brand", self.brand_input)
        self.layout.addRow("Model", self.model_input)
        self.layout.addRow("Price per Hour", self.price_input)
        self.layout.addRow("Location", self.location_input)
        self.layout.addRow("Status", self.status_input)
        self.layout.addRow("Driver License Category", self.driver_license_input)

        # Кнопка добавления
        self.add_button = QPushButton("Add Car")
        self.layout.addWidget(self.add_button)

        # Применяем стиль
        self.button_style()

        # Подключаем сигнал
        self.add_button.clicked.connect(self.add_car)

        self.setLayout(self.layout)

    def button_style(self):
        """Применение стилей для кнопок."""
        self.add_button.setStyleSheet("""
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

    def add_car(self):
        gos_num = self.gos_num_input.text()
        brand = self.brand_input.text()
        model = self.model_input.text()
        price_per_hour = self.price_input.value()
        location = self.location_input.text()
        status = self.status_input.text()
        driver_license_category = self.driver_license_input.text()

        try:
            response = self.car_client.add_car(gos_num, brand, model, price_per_hour, location, status, driver_license_category)
            if response.success:
                QMessageBox.information(self, "Success", "Car added successfully")
                self.accept()
            else:
                QMessageBox.critical(self, "Error", response.message)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add car: {str(e)}")


class EditCarDialog(QDialog):
    def __init__(self, car_client, car_id):
        super().__init__()
        self.car_client = car_client
        self.car_id = car_id
        self.setWindowTitle("Edit Car Details")

        # Основной layout
        self.layout = QFormLayout()

        # Поле для статуса
        self.status_input = QLineEdit()

        self.layout.addRow("Status", self.status_input)

        # Кнопка обновления
        self.update_button = QPushButton("Update Car Status")
        self.layout.addWidget(self.update_button)

        # Применяем стиль
        self.button_style()

        # Подключаем сигнал
        self.update_button.clicked.connect(self.update_car)

        self.setLayout(self.layout)

    def button_style(self):
        """Применение стилей для кнопок."""
        self.update_button.setStyleSheet("""
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

    def update_car(self):
        status = self.status_input.text()

        try:
            response = self.car_client.update_car_status(self.car_id, status)
            if response.success:
                QMessageBox.information(self, "Success", "Car status updated successfully")
                self.accept()
            else:
                QMessageBox.critical(self, "Error", response.message)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update car: {str(e)}")


class CarDetailsDialog(QDialog):
    def __init__(self, car_details):
        super().__init__()
        self.setWindowTitle("Car Details")

        # Основной layout
        self.layout = QFormLayout()

        # Поля для отображения информации
        self.gos_num_input = QLineEdit(car_details.gos_num)
        self.brand_input = QLineEdit(car_details.brand)
        self.model_input = QLineEdit(car_details.model)
        self.price_input = QDoubleSpinBox()
        self.price_input.setValue(car_details.price_per_hour)
        self.location_input = QLineEdit(car_details.location)
        self.status_input = QLineEdit(car_details.status)
        self.driver_license_input = QLineEdit(car_details.driver_license_category)

        # Устанавливаем поля как только для чтения
        self.gos_num_input.setReadOnly(True)
        self.brand_input.setReadOnly(True)
        self.model_input.setReadOnly(True)
        self.price_input.setReadOnly(True)
        self.location_input.setReadOnly(True)
        self.status_input.setReadOnly(True)
        self.driver_license_input.setReadOnly(True)

        # Добавляем поля в форму
        self.layout.addRow("Gos Number", self.gos_num_input)
        self.layout.addRow("Brand", self.brand_input)
        self.layout.addRow("Model", self.model_input)
        self.layout.addRow("Price per Hour", self.price_input)
        self.layout.addRow("Location", self.location_input)
        self.layout.addRow("Status", self.status_input)
        self.layout.addRow("Driver License Category", self.driver_license_input)

        self.setLayout(self.layout)

