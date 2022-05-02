from PyQt5.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QSizePolicy
from PyQt5 import QtCore
from FormWindow import FormWindow
from FormResult import FormResult

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

         # Set the window size (800x500)
        self.setGeometry(100, 100, 800,500)

        # Set the window name
        self.setWindowTitle("Example Form Window")

        # Set the window icon
        # self.setWindowIcon(QtGui.QIcon('path/of/the/file.png'))
        
        # Create a container for the element of the window
        self.container = QStackedWidget()
        self.container.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

        # Create the form layout object
        self.formPage = FormWindow()

        # Add function to the formPage.button
        self.formPage.button.clicked.connect(self.submitForm)

        # Add the homepage window into the main window
        self.container.addWidget(self.formPage)
        self.container.setCurrentWidget(self.formPage)

        # Create a layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.container)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        
        # Add layout to the window and then show the window
        self.setLayout(self.layout)
    
    # Submit the form and run it
    def submitForm(self):
        # Hide the old page
        self.formPage.hide()

        # Remove the homepage widget from the container
        self.container.removeWidget(self.formPage)
        
        # Get the input values
        name = self.formPage.name.text()
        surname = self.formPage.surname.text()

        # Create the second page object
        self.resultPage = FormResult(name, surname)

        # Add the second page to the container
        self.container.addWidget(self.resultPage)

        # Set the new widget as current
        self.container.setCurrentWidget(self.resultPage)

        # Show the page
        self.resultPage.show()

