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
        self.showArticles()

    def refresh(self):
        self.load_articles(self.currentTopic)

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

        for i, button in enumerate(self.save_buttons):
            button.clicked.connect(partial(self.save_article, i))   

    def showSignInPage(self):
        self.stackedWidget.setCurrentWidget(self.registration_page)

    def showNewsPage(self):
        self.stackedWidget.setCurrentWidget(self.news_page)
        if self.currentTab == "Saved":
            self.showSavedArticles()
        else:
            self.articleWidget.setCurrentWidget(self.articles_page)
            self.load_articles(self.currentTab)

    def save_article(self, articleNo):
        if not self.signedIn:
            return

        if articleNo > len(self.articles):
            # Saved article being removed
            article = self.saved_articles[articleNo-15]
            remove_saved_article(self.user_id, article)
            print(f"Removed article {articleNo}")

        else:
            article = self.articles[articleNo]
            save_article(self.user_id, article)
            print(f"Saved article {articleNo}")

    def showSavedArticles(self):
        _translate = QtCore.QCoreApplication.translate
        self.stackedWidget.setCurrentWidget(self.savedArticles_page)
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

        if not self.signedIn:
            self.articleWidget.setCurrentWidget(self.text_page)
            self.no_saves_label.setText("Sign up to save articles here!")
        else:
            self.articleWidget.setCurrentWidget(self.savedArticles_page)
            self.saved_articles = get_saved_articles(self.user_id)
            print(len(self.saved_articles))
            if len(self.saved_articles) != 0:
                for i, widget in enumerate(self.saved_widgets):
                    if i < len(self.saved_articles):
                        art = self.saved_articles[i]
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

    def showArticles(self):
        _translate = QtCore.QCoreApplication.translate

        self.articleTitle_label_1.setText(_translate("MainWindow", self.articles[self.articleIndex]["title"]))
        self.articleAuthor_label_1.setText(_translate("MainWindow", self.articles[self.articleIndex]["author"]))
        self.articlePublishedAt_label_1.setText(_translate("MainWindow", self.articles[self.articleIndex]["publishedAt"]))
        self.articleDescription_label_1.setText(_translate("MainWindow", self.articles[self.articleIndex]["description"]))
        self.articleContent_label_1.setText(_translate("MainWindow", self.articles[self.articleIndex]["content"]))
        if self.signedIn:
            if is_article_saved(self.user_id, self.articles[self.articleIndex]):
                self.articleSave_button_1.setChecked(True)


        self.articleTitle_label_2.setText(_translate("MainWindow", self.articles[self.articleIndex+1]["title"]))
        self.articleAuthor_label_2.setText(_translate("MainWindow", self.articles[self.articleIndex+1]["author"]))
        self.articlePublishedAt_label_2.setText(_translate("MainWindow", self.articles[self.articleIndex+1]["publishedAt"]))
        self.articleDescription_label_2.setText(_translate("MainWindow", self.articles[self.articleIndex+1]["description"]))
        self.articleContent_label_2.setText(_translate("MainWindow", self.articles[self.articleIndex+1]["content"]))
        if self.signedIn:  
            if is_article_saved(self.user_id, self.articles[self.articleIndex+1]):
                self.articleSave_button_2.setChecked(True)

        self.articleTitle_label_3.setText(_translate("MainWindow", self.articles[self.articleIndex+2]["title"]))
        self.articleAuthor_label_3.setText(_translate("MainWindow", self.articles[self.articleIndex+2]["author"]))
        self.articlePublishedAt_label_3.setText(_translate("MainWindow", self.articles[self.articleIndex+2]["publishedAt"]))
        self.articleDescription_label_3.setText(_translate("MainWindow", self.articles[self.articleIndex+2]["description"]))
        self.articleContent_label_3.setText(_translate("MainWindow", self.articles[self.articleIndex+2]["content"]))
        if self.signedIn:
            if is_article_saved(self.user_id, self.articles[self.articleIndex+2]):
                self.articleSave_button_3.setChecked(True)

        self.articleTitle_label_4.setText(_translate("MainWindow", self.articles[self.articleIndex+3]["title"]))
        self.articleAuthor_label_4.setText(_translate("MainWindow", self.articles[self.articleIndex+3]["author"]))
        self.articlePublishedAt_label_4.setText(_translate("MainWindow", self.articles[self.articleIndex+3]["publishedAt"]))
        self.articleDescription_label_4.setText(_translate("MainWindow", self.articles[self.articleIndex+3]["description"]))
        self.articleContent_label_4.setText(_translate("MainWindow", self.articles[self.articleIndex+3]["content"]))
        if self.signedIn:
            if is_article_saved(self.user_id, self.articles[self.articleIndex+3]):
                self.articleSave_button_4.setChecked(True)

        self.articleTitle_label_5.setText(_translate("MainWindow", self.articles[self.articleIndex+4]["title"]))
        self.articleAuthor_label_5.setText(_translate("MainWindow", self.articles[self.articleIndex+4]["author"]))
        self.articlePublishedAt_label_5.setText(_translate("MainWindow", self.articles[self.articleIndex+4]["publishedAt"]))
        self.articleDescription_label_5.setText(_translate("MainWindow", self.articles[self.articleIndex+4]["description"]))
        self.articleContent_label_5.setText(_translate("MainWindow", self.articles[self.articleIndex+4]["content"]))
        if self.signedIn:
            if is_article_saved(self.user_id, self.articles[self.articleIndex+4]):
                self.articleSave_button_5.setChecked(True)

        self.articleTitle_label_6.setText(_translate("MainWindow", self.articles[self.articleIndex+5]["title"]))
        self.articleAuthor_label_6.setText(_translate("MainWindow", self.articles[self.articleIndex+5]["author"]))
        self.articlePublishedAt_label_6.setText(_translate("MainWindow", self.articles[self.articleIndex+5]["publishedAt"]))
        self.articleDescription_label_6.setText(_translate("MainWindow", self.articles[self.articleIndex+5]["description"]))
        self.articleContent_label_6.setText(_translate("MainWindow", self.articles[self.articleIndex+5]["content"]))
        if self.signedIn:
            if is_article_saved(self.user_id, self.articles[self.articleIndex+5]):
                self.articleSave_button_6.setChecked(True)

        self.articleTitle_label_7.setText(_translate("MainWindow", self.articles[self.articleIndex+6]["title"]))
        self.articleAuthor_label_7.setText(_translate("MainWindow", self.articles[self.articleIndex+6]["author"]))
        self.articlePublishedAt_label_7.setText(_translate("MainWindow", self.articles[self.articleIndex+6]["publishedAt"]))
        self.articleDescription_label_7.setText(_translate("MainWindow", self.articles[self.articleIndex+6]["description"]))
        self.articleContent_label_7.setText(_translate("MainWindow", self.articles[self.articleIndex+6]["content"]))
        if self.signedIn:
            if is_article_saved(self.user_id, self.articles[self.articleIndex+6]):
                self.articleSave_button_7.setChecked(True)

        self.articleTitle_label_8.setText(_translate("MainWindow", self.articles[self.articleIndex+7]["title"]))
        self.articleAuthor_label_8.setText(_translate("MainWindow", self.articles[self.articleIndex+7]["author"]))
        self.articlePublishedAt_label_8.setText(_translate("MainWindow", self.articles[self.articleIndex+7]["publishedAt"]))
        self.articleDescription_label_8.setText(_translate("MainWindow", self.articles[self.articleIndex+7]["description"]))
        self.articleContent_label_8.setText(_translate("MainWindow", self.articles[self.articleIndex+7]["content"]))
        if self.signedIn:
            if is_article_saved(self.user_id, self.articles[self.articleIndex+7]):
                self.articleSave_button_8.setChecked(True)

        self.articleTitle_label_9.setText(_translate("MainWindow", self.articles[self.articleIndex+8]["title"]))
        self.articleAuthor_label_9.setText(_translate("MainWindow", self.articles[self.articleIndex+8]["author"]))
        self.articlePublishedAt_label_9.setText(_translate("MainWindow", self.articles[self.articleIndex+8]["publishedAt"]))
        self.articleDescription_label_9.setText(_translate("MainWindow", self.articles[self.articleIndex+8]["description"]))
        self.articleContent_label_9.setText(_translate("MainWindow", self.articles[self.articleIndex+8]["content"]))
        if self.signedIn:
            if is_article_saved(self.user_id, self.articles[self.articleIndex+8]):
                self.articleSave_button_9.setChecked(True)

        self.articleTitle_label_10.setText(_translate("MainWindow", self.articles[self.articleIndex+9]["title"]))
        self.articleAuthor_label_10.setText(_translate("MainWindow", self.articles[self.articleIndex+9]["author"]))
        self.articlePublishedAt_label_10.setText(_translate("MainWindow", self.articles[self.articleIndex+9]["publishedAt"]))
        self.articleDescription_label_10.setText(_translate("MainWindow", self.articles[self.articleIndex+9]["description"]))
        self.articleContent_label_10.setText(_translate("MainWindow", self.articles[self.articleIndex+9]["content"]))
        if self.signedIn:
            if is_article_saved(self.user_id, self.articles[self.articleIndex+9]):
                self.articleSave_button_10.setChecked(True)

        if (len(self.articles)) > 10:
            self.articleBox_11.show()
            self.articleTitle_label_11.setText(_translate("MainWindow", self.articles[self.articleIndex+10]["title"]))
            self.articleAuthor_label_11.setText(_translate("MainWindow", self.articles[self.articleIndex+10]["author"]))
            self.articlePublishedAt_label_11.setText(_translate("MainWindow", self.articles[self.articleIndex+10]["publishedAt"]))
            self.articleDescription_label_11.setText(_translate("MainWindow", self.articles[self.articleIndex+10]["description"]))
            self.articleContent_label_11.setText(_translate("MainWindow", self.articles[self.articleIndex+10]["content"]))
            if self.signedIn:
                if is_article_saved(self.user_id, self.articles[self.articleIndex+10]):
                    self.articleSave_button_11.setChecked(True)
        else:
            self.articleBox_11.hide()

        if (len(self.articles)) > 11:
            self.articleBox_12.show()
            self.articleTitle_label_12.setText(_translate("MainWindow", self.articles[self.articleIndex+11]["title"]))
            self.articleAuthor_label_12.setText(_translate("MainWindow", self.articles[self.articleIndex+11]["author"]))
            self.articlePublishedAt_label_12.setText(_translate("MainWindow", self.articles[self.articleIndex+11]["publishedAt"]))
            self.articleDescription_label_12.setText(_translate("MainWindow", self.articles[self.articleIndex+11]["description"]))
            self.articleContent_label_12.setText(_translate("MainWindow", self.articles[self.articleIndex+11]["content"]))
            if self.signedIn:
                if is_article_saved(self.user_id, self.articles[self.articleIndex+11]):
                    self.articleSave_button_12.setChecked(True)
        else:
            self.articleBox_12.hide()

        if (len(self.articles)) > 12:
            self.articleBox_13.show()
            self.articleTitle_label_13.setText(_translate("MainWindow", self.articles[self.articleIndex+12]["title"]))
            self.articleAuthor_label_13.setText(_translate("MainWindow", self.articles[self.articleIndex+12]["author"]))
            self.articlePublishedAt_label_13.setText(_translate("MainWindow", self.articles[self.articleIndex+12]["publishedAt"]))
            self.articleDescription_label_13.setText(_translate("MainWindow", self.articles[self.articleIndex+12]["description"]))
            self.articleContent_label_13.setText(_translate("MainWindow", self.articles[self.articleIndex+12]["content"]))
            if self.signedIn:
                if is_article_saved(self.user_id, self.articles[self.articleIndex+12]):
                    self.articleSave_button_13.setChecked(True)
        else:
            self.articleBox_13.hide()

        if (len(self.articles)) > 13:
            self.articleBox_14.show()
            self.articleTitle_label_14.setText(_translate("MainWindow", self.articles[self.articleIndex+13]["title"]))
            self.articleAuthor_label_14.setText(_translate("MainWindow", self.articles[self.articleIndex+13]["author"]))
            self.articlePublishedAt_label_14.setText(_translate("MainWindow", self.articles[self.articleIndex+13]["publishedAt"]))
            self.articleDescription_label_14.setText(_translate("MainWindow", self.articles[self.articleIndex+13]["description"]))
            self.articleContent_label_14.setText(_translate("MainWindow", self.articles[self.articleIndex+13]["content"]))
            if self.signedIn:
                if is_article_saved(self.user_id, self.articles[self.articleIndex+13]):
                    self.articleSave_button_14.setChecked(True)
        else:
            self.articleBox_14.hide()

        if (len(self.articles)) > 14:
            self.articleBox_15.show()
            self.articleTitle_label_15.setText(_translate("MainWindow", self.articles[self.articleIndex+14]["title"]))
            self.articleAuthor_label_15.setText(_translate("MainWindow", self.articles[self.articleIndex+14]["author"]))
            self.articlePublishedAt_label_15.setText(_translate("MainWindow", self.articles[self.articleIndex+14]["publishedAt"]))
            self.articleDescription_label_15.setText(_translate("MainWindow", self.articles[self.articleIndex+14]["description"]))
            self.articleContent_label_15.setText(_translate("MainWindow", self.articles[self.articleIndex+14]["content"]))
            if self.signedIn:
                if is_article_saved(self.user_id, self.articles[self.articleIndex+14]):
                    self.articleSave_button_15.setChecked(True)
        else:
            self.articleBox_15.hide()

        self.articleBox_16.hide()
        self.articleBox_17.hide()
        self.articleBox_18.hide()
        self.articleBox_19.hide()
        self.articleBox_20.hide()
        self.articleBox_21.hide()
        
        self.results_label.setText("Results: " + str(self.results))

    def readMoreLink(self):
        self.articleLink_label.setText(f'<a href="{self.articles[self.articleIndex]['url']}">Read more')
        self.articleLink_label.setOpenExternalLinks(True)
        self.articleLink_label_2.setText(f'<a href="{self.articles[self.articleIndex+1]['url']}">Read more')
        self.articleLink_label_2.setOpenExternalLinks(True)
        self.articleLink_label_3.setText(f'<a href="{self.articles[self.articleIndex+2]['url']}">Read more')
        self.articleLink_label_3.setOpenExternalLinks(True)
        self.articleLink_label_4.setText(f'<a href="{self.articles[self.articleIndex+3]['url']}">Read more')
        self.articleLink_label_4.setOpenExternalLinks(True)
        self.articleLink_label_5.setText(f'<a href="{self.articles[self.articleIndex+4]['url']}">Read more')
        self.articleLink_label_5.setOpenExternalLinks(True)
        self.articleLink_label_6.setText(f'<a href="{self.articles[self.articleIndex+5]['url']}">Read more')
        self.articleLink_label_6.setOpenExternalLinks(True)
        self.articleLink_label_7.setText(f'<a href="{self.articles[self.articleIndex+6]['url']}">Read more')
        self.articleLink_label_7.setOpenExternalLinks(True)
        self.articleLink_label_8.setText(f'<a href="{self.articles[self.articleIndex+7]['url']}">Read more')
        self.articleLink_label_8.setOpenExternalLinks(True)
        self.articleLink_label_9.setText(f'<a href="{self.articles[self.articleIndex+8]['url']}">Read more')
        self.articleLink_label_9.setOpenExternalLinks(True)
        self.articleLink_label_10.setText(f'<a href="{self.articles[self.articleIndex+9]['url']}">Read more')
        self.articleLink_label_10.setOpenExternalLinks(True)
        if (len(self.articles)) > 10:
            self.articleLink_label_11.setText(f'<a href="{self.articles[self.articleIndex+10]['url']}">Read more')
            self.articleLink_label_11.setOpenExternalLinks(True)
        if (len(self.articles)) > 11:
            self.articleLink_label_12.setText(f'<a href="{self.articles[self.articleIndex+11]['url']}">Read more')
            self.articleLink_label_12.setOpenExternalLinks(True)
        if (len(self.articles)) > 12:
            self.articleLink_label_13.setText(f'<a href="{self.articles[self.articleIndex+12]['url']}">Read more')
            self.articleLink_label_13.setOpenExternalLinks(True)
        if (len(self.articles)) > 13:
            self.articleLink_label_14.setText(f'<a href="{self.articles[self.articleIndex+13]['url']}">Read more')
            self.articleLink_label_14.setOpenExternalLinks(True)
        if (len(self.articles)) > 14:
            self.articleLink_label_15.setText(f'<a href="{self.articles[self.articleIndex+14]['url']}">Read more')
            self.articleLink_label_15.setOpenExternalLinks(True)

    def showArticles2(self):
        _translate = QtCore.QCoreApplication.translate

        self.articleTitle_label_1.setText(_translate("MainWindow", self.articles[self.articleIndex]["title"]))
        self.articleAuthor_label_1.setText(_translate("MainWindow", self.articles[self.articleIndex]["author"]))
        self.articlePublishedAt_label_1.setText(_translate("MainWindow", self.articles[self.articleIndex]["publishedAt"]))
        self.articleDescription_label_1.setText(_translate("MainWindow", self.articles[self.articleIndex]["description"]))
        self.articleContent_label_1.setText(_translate("MainWindow", self.articles[self.articleIndex]["content"]))
        self.articleLink_label_1.setText(f'<a href="{self.articles[self.articleIndex+9]['url']}">Read more')
        self.articleLink_label_1.setOpenExternalLinks(True)

        max_articles = 16  # how many boxes you actually have in the UI

        for i in range(max_articles):
            article_index = self.articleIndex + i

            # dynamically get UI elements (e.g., self.articleTitle_label_1, self.articleBox_1, etc.)
            title_label = getattr(self, f"articleTitle_label_{i}", None)
            author_label = getattr(self, f"articleAuthor_label_{i}", None)
            published_label = getattr(self, f"articlePublishedAt_label_{i}", None)
            description_label = getattr(self, f"articleDescription_label_{i}", None)
            content_label = getattr(self, f"articleContent_label_{i}", None)
            box = getattr(self, f"articleBox_{i}", None)
            link_label = getattr(self, f"articleLink_label_{i}", None)
            if self.signedIn:
                if is_article_saved(self.user_id, self.articles[article_index]):
                    saved_article = getattr(self, f"articleSave_button_{i}", None)
                    saved_article.setChecked(True)
                else:
                    saved_article.setChecked(False)

            if article_index < len(self.articles):  
                article = self.articles[article_index]

                if title_label:
                    title_label.setText(_translate("MainWindow", article.get("title", "")))
                if author_label:
                    author_label.setText(_translate("MainWindow", article.get("author", "")))
                if published_label:
                    published_label.setText(_translate("MainWindow", article.get("publishedAt", "")))
                if description_label:
                    description_label.setText(_translate("MainWindow", article.get("description", "")))
                if content_label:
                    content_label.setText(_translate("MainWindow", article.get("content", "")))
                if link_label and "url" in article:
                    link_label.setText(f'<a href="{article["url"]}">Read more</a>')
                    link_label.setOpenExternalLinks(True)
                if box:
                    box.show()
            else:
                if box:
                    box.hide()

        self.results_label.setText("Results: " + str(self.results))
