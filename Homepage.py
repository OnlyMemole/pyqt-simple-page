from PyQt5.QtWidgets import QWidget, QPushButton, QGroupBox, QVBoxLayout
from PyQt5 import QtCore


class Homepage(QWidget):
    def __init__(self):
        super(Homepage, self).__init__()

        # Create a container
        self.container = QGroupBox()
        self.container.setAlignment(QtCore.Qt.AlignCenter)

        # Create a simple button
        self.button = QPushButton("Change Content")
        
    
        # Create the page
        self.createPage()

        # Create layout and add the container to the main layout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.container)

        # Set the layout
        self.setLayout(self.mainLayout)
    
    # Create a layout and then add the button
    def createPage(self):
        layout = QVBoxLayout()
        layout.addWidget(self.button)

        self.container.setLayout(layout)
