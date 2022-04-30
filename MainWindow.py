from PyQt5.QtWidgets import QWidget, QStackedWidget, QSizePolicy, QVBoxLayout, QApplication
from PyQt5 import QtCore
from Homepage import Homepage
from SecondPage import SecondPage
import sys

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set the window size (800x500)
        self.setGeometry(100, 100, 800,500)

        # Set the window name
        self.setWindowTitle("Example Window")

        # Set the window icon
        # self.setWindowIcon(QtGui.QIcon('path/of/the/file.png'))
        
        # Create the homepage object
        self.homepage = Homepage()
        
        # Add function to the homepage.button
        self.homepage.button.clicked.connect(self.changePage)

        # Create a container for the element of the window
        self.container = QStackedWidget()
        self.container.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

        # Add the homepage window into the main window
        self.container.addWidget(self.homepage)
        self.container.setCurrentWidget(self.homepage)

        # Create a layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.container)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        
        # Add layout to the window and then show the window
        self.setLayout(self.layout)
    
    def changePage(self):
        # Hide the old page
        self.homepage.hide()

        # Remove the homepage widget from the container
        self.container.removeWidget(self.homepage)

        # Create the second page object
        self.secondPage = SecondPage()

        # Add the second page to the container
        self.container.addWidget(self.secondPage)

        # Set the new widget as current
        self.container.setCurrentWidget(self.secondPage)

        # Show the page
        self.secondPage.show()




# Start the window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())