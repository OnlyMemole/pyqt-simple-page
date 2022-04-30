from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QGroupBox
from PyQt5 import QtCore

class SecondPage(QWidget):
    def __init__(self):
        super(SecondPage, self).__init__()

        # Create a label
        self.text = QLabel("Page changed!")

        # Create a container
        self.container = QGroupBox()
        self.container.setAlignment(QtCore.Qt.AlignCenter)

        # Create the page
        self.createPage()

        # Create layout and add the container to the main layout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.container)

        # Set the layout
        self.setLayout(self.mainLayout)

    # Create a layout and then add the label
    def createPage(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text)

        self.container.setLayout(layout)