from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, articles, results):
        super().__init__()
        self.articles = articles
        self.results = results
        self.setupUi(self)
        self.createButtons()

    def createButtons(self):
        self.signIn_button.clicked.connect(self.showSignInPage)
        self.skip_button.clicked.connect(self.showNewsPage)

    def showSignInPage(self):
        self.stackedWidget.setCurrentWidget(self.registration_page)
    
    def showNewsPage(self):
        self.stackedWidget.setCurrentWidget(self.news_page)
