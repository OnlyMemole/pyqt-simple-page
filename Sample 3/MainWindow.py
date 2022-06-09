from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set the window name
        self.setWindowTitle("WebView")

        # Create WebView widget
        self.createWebView()

        # Set widget into the frame at the center
        self.setCentralWidget(self.browser)

        # Set the frame as fullscreen
        self.showMaximized()


    def createWebView(self):
        # Creating the webview object
        self.browser = QWebEngineView()

        # Set the webview url, in my case I will use github as an example
        self.browser.setUrl(QUrl("https://github.com/"))

        # Remember: this will work yes as a webview, but the various tools (back, forward, reload) 
        # are not present, so, you will have to create them yourself.
        # Instead, you can use the window as if you were browsing in your favorite browser, 
        # without any (I think) limitations.


