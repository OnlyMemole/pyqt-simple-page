from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
import sys

# Start the window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())