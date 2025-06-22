import sys
from PyQt6.QtWidgets import QApplication
from Views.Login import LoginView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginView()
    window.show()
    sys.exit(app.exec())