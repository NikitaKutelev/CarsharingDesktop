# import sys
# import set_root_path
# from PyQt6.QtWidgets import QApplication
# from ui.main_window import MainWindow
# from core.grpc_client_manager import GRPCClientManager
# from core.navigation import NavigationManager

# def main():
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     grpc_manager = GRPCClientManager()
#     navigation = NavigationManager(main_window)
#     # Example: Connect components

#     main_window.grpc_manager = grpc_manager
#     main_window.navigation = navigation

#     main_window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


import sys
import set_root_path
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from core.grpc_client_manager import GRPCClientManager
from core.navigation import NavigationManager

def main():
    app = QApplication(sys.argv)

    # Initialize gRPC clients
    grpc_manager = GRPCClientManager()

    # Pass gRPC clients to MainWindow
    main_window = MainWindow(
        user_client=grpc_manager.user_client,
        car_client=grpc_manager.car_client,
        booking_client=grpc_manager.booking_client,
        payment_client=grpc_manager.payment_client
    )

    # Initialize navigation
    navigation = NavigationManager(main_window)
    main_window.navigation = navigation

    # Show the main window
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()