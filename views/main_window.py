from PyQt5 import QtCore, QtWidgets, QtGui
from ui.ui_mainwindow import Ui_MainWindow
from api.api_params import Api_params
from views.sign_in import SignInPage
from views.key_entry import KeyEntryPage
from views.profile import ProfilePage
from config_manager import load_config, is_first_run
from load_db import save_article, get_saved_articles, remove_saved_article, is_article_saved
from functools import partial
import random as r

# Class for the main GUI handling
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    MAX_NEWS_ARTICLES = 15
    MAX_SAVED_ARTICLES = 6

    # TODO: make a separate class for whenever data is inserted into the database
    # and for credential checking

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Initialise starting variables
        self.signedIn = False
        self.user_id = None
        self.email = None
        self.currentTab = "Top US"

        self.news_service = None
        self.articles = []
        self.saved_articles = []

        # Setup pages
        self.sign_in_page = SignInPage(self)
        self.key_entry_page = KeyEntryPage(self)
        self.user_profile_page = ProfilePage(self)

        self.createButtons()
        self.startUp()
    # Check if api key is entered
    def startUp(self):
        config = load_config()
        if is_first_run(config) or not config.get("api_key"):
            self.stackedWidget.setCurrentWidget(self.startUp_page)
        else:
            self.news_service = Api_params()
            self.showNewsPage()

    def createButtons(self):
        self.searchBar.returnPressed.connect(self.performSearch)
        self.signIn_button.clicked.connect(self.showSignInPage)
        self.profile_button.clicked.connect(self.showProfilePage)
        self.topUS_button.clicked.connect(lambda: self.load_articles("Top US"))
        self.WSJ_button.clicked.connect(lambda: self.load_articles("Wall Street Journal"))
        self.apple_button.clicked.connect(lambda: self.load_articles("Apple"))
        self.tesla_button.clicked.connect(lambda: self.load_articles("Tesla"))
        self.saved_button.clicked.connect(self.showSavedArticles)
        self.refresh_button.clicked.connect(self.refresh)

        # Collect all save buttons in order
        self.save_buttons = [
            getattr(self, f"articleSave_button_{i+1}") for i in range(21)
        ]

        # Connect all buttons dynamically to toggle function
        for i, btn in enumerate(self.save_buttons):
            btn.clicked.connect(partial(self.toggle_save, i))

    def showSignInPage(self):
        self.stackedWidget.setCurrentWidget(self.registration_page)

    def showNewsPage(self):
        self.stackedWidget.setCurrentWidget(self.news_page)
        if self.currentTab == "Saved":
            self.showSavedArticles()
        else:
            self.articleWidget.setCurrentWidget(self.articles_page)
            self.load_articles(self.currentTab)

    def showProfilePage(self):
        self.user_profile_page.updateData()
        self.stackedWidget.setCurrentWidget(self.profile_page)

    def load_articles(self, topic):
        self.currentTab = topic
        self.articleWidget.setCurrentWidget(self.articles_page)
        self.saved_button.setEnabled(True)

        # Fetch articles from API
        self.articles, self.results = self.news_service.fetch_articles(topic)

        # Enable/disable tab buttons
        self.topUS_button.setEnabled(topic != "Top US")
        self.WSJ_button.setEnabled(topic != "Wall Street Journal")
        self.apple_button.setEnabled(topic != "Apple")
        self.tesla_button.setEnabled(topic != "Tesla")

        self.populate_articles()

    def refresh(self):
        if self.currentTab != "Saved":
            self.load_articles(self.currentTab)
        
        r.shuffle(self.articles)
        self.populate_articles()
        self.status_label.setText("Refreshed")
        QtCore.QTimer.singleShot(3000, lambda: self.status_label.setText(""))

    def populate_articles(self):
        _translate = QtCore.QCoreApplication.translate
        max_display = min(len(self.articles), self.MAX_NEWS_ARTICLES)

        for i in range(self.MAX_NEWS_ARTICLES):
            # Dynamically get UI elements
            box = getattr(self, f"articleBox_{i+1}", None)
            title_label = getattr(self, f"articleTitle_label_{i+1}", None)
            author_label = getattr(self, f"articleAuthor_label_{i+1}", None)
            published_label = getattr(self, f"articlePublishedAt_label_{i+1}", None)
            description_label = getattr(self, f"articleDescription_label_{i+1}", None)
            content_label = getattr(self, f"articleContent_label_{i+1}", None)
            link_label = getattr(self, f"articleLink_label_{i+1}", None)
            save_button = self.save_buttons[i] if i < len(self.save_buttons) else None

            if i < max_display:
                article = self.articles[i]
                box.show() if box else None
                if title_label: title_label.setText(_translate("MainWindow", article.get("title", "")))
                if author_label: author_label.setText(_translate("MainWindow", article.get("author", "")))
                if published_label: published_label.setText(_translate("MainWindow", article.get("publishedAt", "")))
                if description_label: description_label.setText(_translate("MainWindow", article.get("description", "")))
                if content_label: content_label.setText(_translate("MainWindow", article.get("content", "")))
                if link_label and "url" in article:
                    link_label.setText(f'<a href="{article["url"]}">Read more</a>')
                    link_label.setOpenExternalLinks(True)
                if save_button and self.signedIn:
                    save_button.setChecked(is_article_saved(self.user_id, article))
            else:
                if box: box.hide()

        def format_results(n: int) -> str:
            if n >= 1_000_000:
                return f"{n/1_000_000:.1f}M"
            elif n >= 1_000:
                return f"{n/1_000:.1f}K"
            else:
                return str(n)

        self.results_label.setText(f"Results: {format_results(self.results)}")

    def toggle_save(self, index: int):
        # Buttons 0..14 => news list (MAX_NEWS_ARTICLES = 15)
        if index < self.MAX_NEWS_ARTICLES and index < len(self.articles) and self.currentTab != "Saved":
            article = self.articles[index]
            button = self.save_buttons[index]
            if not self.signedIn:
                self.status_label.setText("Sign in to save articles")
                QtCore.QTimer.singleShot(3000, lambda: self.status_label.setText(""))
                button.setChecked(False)
                return
            if is_article_saved(self.user_id, article):
                remove_saved_article(self.user_id, article)   # expects dict with "url"
                button.setChecked(False)
            else:
                saved_count = len(get_saved_articles(self.user_id))
                if saved_count >= 6:
                    self.status_label.setText("You have reached the limit of 6 articles saved.")
                    QtCore.QTimer.singleShot(3000, lambda: self.status_label.setText(""))
                    button.setChecked(False)
                else:
                    print("Happened")
                    save_article(self.user_id, article)           # expects dict with "url"
                    button.setChecked(True)

            # If the Saved page is open in another tab later, keep it fresh next time:
            # (Optional) self.saved_articles = get_saved_articles(self.user_id)

        else:
            # Buttons 15..20 => saved list (6 slots). Map to saved index.
            saved_idx = index - self.MAX_NEWS_ARTICLES
            if 0 <= saved_idx < len(self.saved_articles):
                # saved_articles rows come back as tuples:
                # (title, author, publishedAt, description, content, link)
                link = self.saved_articles[saved_idx][5]
                # remove using URL as identity
                remove_saved_article(self.user_id, {"url": link})

                # Uncheck the clicked saved button (16..21 => index+1 in object names)
                saved_btn = getattr(self, f"articleSave_button_{index+1}", None)
                if saved_btn:
                    saved_btn.setChecked(False)

                # Refresh the Saved section UI to reflect the removal
                self.showSavedArticles()

                # Also refresh news page save states (so its buttons re-check correctly)
                # Only if we currently have news articles loaded
                if self.articles:
                    self.populate_articles()

    def showSavedArticles(self):
        _translate = QtCore.QCoreApplication.translate
        self.currentTab = "Saved"
        self.stackedWidget.setCurrentWidget(self.savedArticles_page)
        self.topUS_button.setEnabled(True)
        self.WSJ_button.setEnabled(True)
        self.apple_button.setEnabled(True)
        self.tesla_button.setEnabled(True)
        self.saved_button.setEnabled(False)

        if not self.signedIn:
            self.articleWidget.setCurrentWidget(self.text_page)
            self.text_label.setText("Sign up to save articles here!")
            return

        self.saved_articles = get_saved_articles(self.user_id)
        if not self.saved_articles:
            self.articleWidget.setCurrentWidget(self.text_page)
            self.text_label.setText("You have 0/6 saved articles.")
            return

        self.articleWidget.setCurrentWidget(self.savedArticles_page)
        max_display = min(len(self.saved_articles), self.MAX_SAVED_ARTICLES)

        for i in range(self.MAX_SAVED_ARTICLES):
            widget_index = i + 16  # assuming your saved widgets start at box 16
            box = getattr(self, f"articleBox_{widget_index}", None)
            title_label = getattr(self, f"articleTitle_label_{widget_index}", None)
            author_label = getattr(self, f"articleAuthor_label_{widget_index}", None)
            published_label = getattr(self, f"articlePublishedAt_label_{widget_index}", None)
            description_label = getattr(self, f"articleDescription_label_{widget_index}", None)
            content_label = getattr(self, f"articleContent_label_{widget_index}", None)
            link_label = getattr(self, f"articleLink_label_{widget_index}", None)
            save_button = getattr(self, f"articleSave_button_{widget_index}", None)

            if i < max_display:
                art = self.saved_articles[i]
                if box: box.show()
                if title_label: title_label.setText(_translate("MainWindow", art[0]))
                if author_label: author_label.setText(_translate("MainWindow", art[1]))
                if published_label: published_label.setText(_translate("MainWindow", art[2]))
                if description_label: description_label.setText(_translate("MainWindow", art[3]))
                if content_label: content_label.setText(_translate("MainWindow", art[4]))
                if link_label:
                    link_label.setText(f'<a href="{art[5]}">Read more</a>')
                    link_label.setOpenExternalLinks(True)
                if save_button: save_button.setChecked(True)
            else:
                if box: box.hide()

    def performSearch(self):
        keyword = self.searchBar.text().strip()
        if not keyword:
            self.load_articles(self.currentTab)
            return
        if not self.news_service:
            self.news_service = Api_params()
        self.currentTab = keyword
        self.articleWidget.setCurrentWidget(self.articles_page)
        self.saved_button.setEnabled(True)
        self.topUS_button.setEnabled(True)
        self.WSJ_button.setEnabled(True)
        self.apple_button.setEnabled(True)
        self.tesla_button.setEnabled(True)

        try:    
            self.articles, self.results= self.news_service.fetch_articles(keyword)
        except Exception as e:
            # handle errors
            print("Search failed:", e)
            self.articles, self.results = [], 0
        
        if len(self.articles) == 0:
            self.articleWidget.setCurrentWidget(self.text_page)
            self.text_label.setText("No articles found")

        # repopulate the UI from the returned articles
        self.populate_articles()