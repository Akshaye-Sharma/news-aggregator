from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ui_mainwindow import Ui_MainWindow
from api.api_params import Api_params
from views.sign_in import SignInPage
from views.key_entry import KeyEntryPage
from config_manager import load_config, is_first_run
from load_db import save_article, get_saved_articles, remove_saved_article, is_article_saved
from functools import partial

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createButtons()

        self.signedIn = False
        self.currentTab = "Top US"
        self.user_id = None

        self.sign_in_page = SignInPage(self)
        self.key_entry_page = KeyEntryPage(self)
        self.startUp()

    def startUp(self):

        config = load_config()
        if is_first_run(config) or not config.get("api_key"):
            self.stackedWidget.setCurrentWidget(self.startUp_page)
        else:
            self.stackedWidget.setCurrentWidget(self.news_page) # Forgot this line
            self.news_service = Api_params()
            self.load_articles(self.currentTab)

    def createButtons(self):
        self.signIn_button.clicked.connect(self.showSignInPage) 

        self.topUS_button.clicked.connect(lambda: self.load_articles("Top US"))
        self.WSJ_button.clicked.connect(lambda: self.load_articles("Wall Street Journal"))
        self.apple_button.clicked.connect(lambda: self.load_articles("Apple"))
        self.tesla_button.clicked.connect(lambda: self.load_articles("Tesla"))
        
        self.saved_button.clicked.connect(self.showSavedArticles)
        self.refresh_button.clicked.connect(self.refresh)

        self.save_buttons = [
        self.articleSave_button_1,
        self.articleSave_button_2,
        self.articleSave_button_3,
        self.articleSave_button_4,
        self.articleSave_button_5,
        self.articleSave_button_6,
        self.articleSave_button_7,
        self.articleSave_button_8,
        self.articleSave_button_9,
        self.articleSave_button_10,
        self.articleSave_button_11,
        self.articleSave_button_12,
        self.articleSave_button_13,
        self.articleSave_button_14,
        self.articleSave_button_15,
        self.articleSave_button_16,
        self.articleSave_button_17,
        self.articleSave_button_18,
        self.articleSave_button_19,
        self.articleSave_button_20,
        self.articleSave_button_21
        ]

        # for i, button in enumerate(self.save_buttons):
        #     button.clicked.connect(partial(self.save_article, i))  
