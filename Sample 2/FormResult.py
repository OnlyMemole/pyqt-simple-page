from tkinter.tix import Form
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QGroupBox, QFormLayout, QVBoxLayout
from PyQt5 import QtCore

class FormResult(QWidget):
    def __init__(self, name, surname):
        super(FormResult, self).__init__()

        # Create a result label which the form value
        self.result = QLabel("Name: " + name + "\nSurname: " + surname)

        # Create a container
        self.container = QGroupBox()
        self.container.setAlignment(QtCore.Qt.AlignCenter)

        self.createPage()

        # Create layout and add the container to the main layout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.container)

        # Set the layout
        self.setLayout(self.mainLayout)

    # Create a layout and then add the label
    def createPage(self):
        layout = QVBoxLayout()
        layout.addWidget(self.result)

        self.container.setLayout(layout)