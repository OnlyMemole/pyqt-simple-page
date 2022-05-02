from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QGroupBox, QFormLayout, QVBoxLayout
from PyQt5 import QtCore

class FormWindow(QWidget):
    def __init__(self):
        super(FormWindow, self).__init__()

        # Create a container
        self.container = QGroupBox()
        self.container.setAlignment(QtCore.Qt.AlignCenter)

        # Define the element of the form
        self.name = QLineEdit()
        self.surname = QLineEdit()

        self.button = QPushButton("Submit")

        self.createForm()

        # Create layout and add the container to the main layout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.container)

        # Set the layout
        self.setLayout(self.mainLayout)
    
    # Compose the form by instantiating and adding the various elements to the layout
    def createForm(self):
        layout = QFormLayout()
        title = QLabel("<h3>Sample Form</h3>")

        layout.addRow(title)
        
        layout.addRow(QLabel("Name"))
        layout.addRow(self.name)
        
        layout.addRow(QLabel("Surname"))
        layout.addRow(self.surname)
        
        layout.addRow(self.button)

        self.container.setLayout(layout)