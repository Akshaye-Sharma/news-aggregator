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

        self.signed_in = False
        self.currentTab = None
        self.user_id = None

        self.startUp()
        self.createButtons()
        self.showNewsPage("Top US")

        #self.sign_in_page = SignInPage(self)
        #self.key_entry_page = KeyEntryPage(self)

    def startUp(self):
        config = load_config()
        if is_first_run(config) or not config.get("api_key"):
            self.stackedWidget.setCurrentWidget(self.startUp_page)
        else:
            self.stackedWidget.setCurrentWidget(self.news_page)
            self.news_service = Api_params()

    def createButtons(self):
        self.signIn_button.clicked.connect(self.showSignInPage) 

        self.topUS_button.clicked.connect(lambda: self.showNewsPage("Top US"))
        self.WSJ_button.clicked.connect(lambda: self.showNewsPage("Wall Street Journal"))
        self.apple_button.clicked.connect(lambda: self.showNewsPage("Apple"))
        self.tesla_button.clicked.connect(lambda: self.showNewsPage("Tesla"))
        
        self.saved_button.clicked.connect(self.showSavedArticles)
        self.saved_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.savedArticles_page))
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

    def load_articles(self, topic: str):
        # Generalized loader for all topics
        self.articleWidget.setCurrentWidget(self.articles_page)
        self.saved_button.setEnabled(True)
        self.currentTab = topic

        self.articles, self.results, self.articleIndex = self.news_service.fetch_articles(topic)        
        self.topUS_button.setEnabled(topic != "Top US")
        self.WSJ_button.setEnabled(topic != "Wall Street Journal")
        self.apple_button.setEnabled(topic != "Apple")
        self.tesla_button.setEnabled(topic != "Tesla")
        self.showArticles2()

    def showNewsPage(self, topic):
        self.currentTab = topic
        self.topUS_button.setEnabled(topic != "Top US")
        self.WSJ_button.setEnabled(topic != "Wall Street Journal")
        self.apple_button.setEnabled(topic != "Apple")
        self.tesla_button.setEnabled(topic != "Tesla")
        _translate = QtCore.QCoreApplication.translate
        
        self.articles, self.results, self.articleIndex = self.news_service.fetch_articles(self.currentTab)        
        
        self.stackedWidget.setCurrentWidget(self.news_page)
        # Group the widgets for each article in lists
        title_labels = [
            self.articleTitle_label_1, self.articleTitle_label_2, self.articleTitle_label_3,
            self.articleTitle_label_4, self.articleTitle_label_5, self.articleTitle_label_6,
            self.articleTitle_label_7, self.articleTitle_label_8, self.articleTitle_label_9,
            self.articleTitle_label_10, self.articleTitle_label_11, self.articleTitle_label_12,
            self.articleTitle_label_13, self.articleTitle_label_14, self.articleTitle_label_15
        ]
        author_labels = [
            self.articleAuthor_label_1, self.articleAuthor_label_2, self.articleAuthor_label_3,
            self.articleAuthor_label_4, self.articleAuthor_label_5, self.articleAuthor_label_6,
            self.articleAuthor_label_7, self.articleAuthor_label_8, self.articleAuthor_label_9,
            self.articleAuthor_label_10, self.articleAuthor_label_11, self.articleAuthor_label_12,
            self.articleAuthor_label_13, self.articleAuthor_label_14, self.articleAuthor_label_15
        ]
        published_labels = [
            self.articlePublishedAt_label_1, self.articlePublishedAt_label_2, self.articlePublishedAt_label_3,
            self.articlePublishedAt_label_4, self.articlePublishedAt_label_5, self.articlePublishedAt_label_6,
            self.articlePublishedAt_label_7, self.articlePublishedAt_label_8, self.articlePublishedAt_label_9,
            self.articlePublishedAt_label_10, self.articlePublishedAt_label_11, self.articlePublishedAt_label_12,
            self.articlePublishedAt_label_13, self.articlePublishedAt_label_14, self.articlePublishedAt_label_15
        ]
        description_labels = [
            self.articleDescription_label_1, self.articleDescription_label_2, self.articleDescription_label_3,
            self.articleDescription_label_4, self.articleDescription_label_5, self.articleDescription_label_6,
            self.articleDescription_label_7, self.articleDescription_label_8, self.articleDescription_label_9,
            self.articleDescription_label_10, self.articleDescription_label_11, self.articleDescription_label_12,
            self.articleDescription_label_13, self.articleDescription_label_14, self.articleDescription_label_15
        ]
        content_labels = [
            self.articleContent_label_1, self.articleContent_label_2, self.articleContent_label_3,
            self.articleContent_label_4, self.articleContent_label_5, self.articleContent_label_6,
            self.articleContent_label_7, self.articleContent_label_8, self.articleContent_label_9,
            self.articleContent_label_10, self.articleContent_label_11, self.articleContent_label_12,
            self.articleContent_label_13, self.articleContent_label_14, self.articleContent_label_15
        ]

        link_labels = [
            self.articleLink_label_1, self.articleLink_label_2, self.articleLink_label_3,
            self.articleLink_label_4, self.articleLink_label_5, self.articleLink_label_6,
            self.articleLink_label_7, self.articleLink_label_8, self.articleLink_label_9,
            self.articleLink_label_10, self.articleLink_label_11, self.articleLink_label_12,
            self.articleLink_label_13, self.articleLink_label_14, self.articleLink_label_15
        ]

        article_boxes = [
            None, None, None, None, None, None, None, None, None, None,  # boxes 1-10 always shown
            self.articleBox_11, self.articleBox_12, self.articleBox_13,
            self.articleBox_14, self.articleBox_15
        ]

        # Loop through up to 15 articles
        for i in range(len(title_labels)):
            article_idx = self.articleIndex + i
            if article_idx < len(self.articles):
                article = self.articles[article_idx]
                title_labels[i].setText(_translate("MainWindow", article["title"]))
                author_labels[i].setText(_translate("MainWindow", article["author"]))
                published_labels[i].setText(_translate("MainWindow", article["publishedAt"]))
                description_labels[i].setText(_translate("MainWindow", article["description"]))
                content_labels[i].setText(_translate("MainWindow", article["content"]))
                link_labels[i].setText(f'<a href="{self.articles[self.articleIndex]['url']}">Read more')
                # Only boxes 11–15 can be hidden
                if article_boxes[i] is not None:
                    article_boxes[i].show()
            else:
                # Hide if beyond article count (for 11–15)
                if article_boxes[i] is not None:
                    article_boxes[i].hide()

        # Always hide 16–21
        self.articleBox_16.hide()
        self.articleBox_17.hide()
        self.articleBox_18.hide()
        self.articleBox_19.hide()
        self.articleBox_20.hide()
        self.articleBox_21.hide()

        self.results_label.setText("Results: " + str(self.results))

    def showSavedArticles(self):
        _translate = QtCore.QCoreApplication.translate
        print("SHOWING SAVES")
        self.currentTab = "Saved"
        self.topUS_button.setEnabled(True)
        self.WSJ_button.setEnabled(True)
        self.apple_button.setEnabled(True)
        self.tesla_button.setEnabled(True)
        self.saved_button.setEnabled(False)

        self.saved_widgets = [
            {
                "box": self.articleBox_16,
                "title": self.articleTitle_label_16,
                "author": self.articleAuthor_label_16,
                "publishedAt": self.articlePublishedAt_label_16,
                "description": self.articleDescription_label_16,
                "content": self.articleContent_label_16,
                "link": self.articleLink_label_16,
                "save_button": self.articleSave_button_16
            }
            ,{
                "box": self.articleBox_17,
                "title": self.articleTitle_label_17,
                "author": self.articleAuthor_label_17,
                "publishedAt": self.articlePublishedAt_label_17,
                "description": self.articleDescription_label_17,
                "content": self.articleContent_label_17,
                "link": self.articleLink_label_17,
                "save_button": self.articleSave_button_17
            }
            ,{
                "box": self.articleBox_18,
                "title": self.articleTitle_label_18,
                "author": self.articleAuthor_label_18,
                "publishedAt": self.articlePublishedAt_label_18,
                "description": self.articleDescription_label_18,
                "content": self.articleContent_label_18,
                "link": self.articleLink_label_18,
                "save_button": self.articleSave_button_18
            }
            ,{
                "box": self.articleBox_19,
                "title": self.articleTitle_label_19,
                "author": self.articleAuthor_label_19,
                "publishedAt": self.articlePublishedAt_label_19,
                "description": self.articleDescription_label_19,
                "content": self.articleContent_label_19,
                "link": self.articleLink_label_19,
                "save_button": self.articleSave_button_19
            }
            ,{
                "box": self.articleBox_20,
                "title": self.articleTitle_label_20,
                "author": self.articleAuthor_label_20,
                "publishedAt": self.articlePublishedAt_label_20,
                "description": self.articleDescription_label_20,
                "content": self.articleContent_label_20,
                "link": self.articleLink_label_20,
                "save_button": self.articleSave_button_20
            }
            ,{
                "box": self.articleBox_21,
                "title": self.articleTitle_label_21,
                "author": self.articleAuthor_label_21,
                "publishedAt": self.articlePublishedAt_label_21,
                "description": self.articleDescription_label_21,
                "content": self.articleContent_label_21,
                "link": self.articleLink_label_21,
                "save_button": self.articleSave_button_21
            }
        ]

        if not self.signed_in:
            self.articleWidget.setCurrentWidget(self.text_page)
            self.no_saves_label.setText("Sign up to save articles here!")
        else:
            self.articleWidget.setCurrentWidget(self.savedArticles_page)
            articles = get_saved_articles(self.user_id)
            print(len(articles))
            if len(articles) != 0:
                for i, widget in enumerate(self.saved_widgets):
                    if i < len(articles):
                        art = articles[i]
                        widget["box"].show()
                        widget["title"].setText(_translate("MainWindow", art[0]))
                        widget["author"].setText(_translate("MainWindow", art[1]))
                        widget["publishedAt"].setText(_translate("MainWindow", art[2]))
                        widget["description"].setText(_translate("MainWindow", art[3]))
                        widget["content"].setText(_translate("MainWindow", art[4]))
                        widget["link"].setText(f'<a href="{art[5]}">Read more</a>')
                        widget["link"].setOpenExternalLinks(True)
                        widget["save_button"].setChecked(True)
                    else:
                        widget["box"].hide()
            else:
                self.articleWidget.setCurrentWidget(self.text_page)
                self.no_saves_label.setText("You have no saved articles")

    def refresh(self):
        self.load_articles(self.currentTab)

    def signedIn(self, name, user_id):
        self.signed_in = True
        self.name_label.setText(name)
        self.signIn_button.setEnabled(False)
        self.user_id = user_id

    def showSignInPage(self):
        print("Happened")
        self.stackedWidget.setCurrentWidget(self.registration_page)