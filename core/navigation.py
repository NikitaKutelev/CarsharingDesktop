class NavigationManager:
    def __init__(self, main_window):
        self.main_window = main_window

    def navigate_to(self, page_name):
        pages = {
            "login": self.main_window.show_login_page,
            "register": self.main_window.show_register_page,
            "profile": self.main_window.show_user_profile_page,
            "car_list": self.main_window.show_car_list_page,
            "booking": self.main_window.show_booking_page,
            "payment": self.main_window.show_payment_page,
        }
        if page_name in pages:
            pages[page_name]()