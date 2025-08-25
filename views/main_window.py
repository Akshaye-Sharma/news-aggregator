from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ui_mainwindow import Ui_MainWindow
from api_params import Api_params
from views.sign_in import SignInPage       

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createButtons()
        self.news_service = Api_params()
        self.sign_in_page = SignInPage(self)

        self.currentTopic = None
        self.load_articles("Top US")
    
    def load_articles(self, topic: str):
        # Generalized loader for all topics
        self.currentTopic = topic

        self.articles, self.results, self.articleIndex = self.news_service.fetch_articles(topic)        
        self.topUS_button.setEnabled(topic != "Top US")
        self.WSJ_button.setEnabled(topic != "Wall Street Journal")
        self.apple_button.setEnabled(topic != "Apple")
        self.tesla_button.setEnabled(topic != "Tesla")
        self.showArticles()
        self.readMoreLink()

    def refresh(self):
        self.load_articles(self.currentTopic)

    def createButtons(self):
        self.signIn_button.clicked.connect(self.showSignInPage) 
        self.news_page_button.clicked.connect(self.showNewsPage)

        self.topUS_button.clicked.connect(lambda: self.load_articles("Top US"))
        self.WSJ_button.clicked.connect(lambda: self.load_articles("Wall Street Journal"))
        self.apple_button.clicked.connect(lambda: self.load_articles("Apple"))
        self.tesla_button.clicked.connect(lambda: self.load_articles("Tesla"))

        self.refresh_button.clicked.connect(self.refresh)

    def showSignInPage(self):
        self.stackedWidget.setCurrentWidget(self.registration_page)
    
    def showNewsPage(self):
        self.stackedWidget.setCurrentWidget(self.news_page)

    def showArticles(self):
        _translate = QtCore.QCoreApplication.translate

        self.label_73.setText(_translate("MainWindow", self.articles[self.articleIndex]["title"]))
        self.label_74.setText(_translate("MainWindow", self.articles[self.articleIndex]["author"]))
        self.label_75.setText(_translate("MainWindow", self.articles[self.articleIndex]["publishedAt"]))
        self.label_76.setText(_translate("MainWindow", self.articles[self.articleIndex]["description"]))
        self.label_77.setText(_translate("MainWindow", self.articles[self.articleIndex]["content"]))

        self.label_78.setText(_translate("MainWindow", self.articles[self.articleIndex+1]["title"]))
        self.label_79.setText(_translate("MainWindow", self.articles[self.articleIndex+1]["author"]))
        self.label_80.setText(_translate("MainWindow", self.articles[self.articleIndex+1]["publishedAt"]))
        self.label_81.setText(_translate("MainWindow", self.articles[self.articleIndex+1]["description"]))
        self.label_82.setText(_translate("MainWindow", self.articles[self.articleIndex+1]["content"]))

        self.label_123.setText(_translate("MainWindow", self.articles[self.articleIndex+2]["title"]))
        self.label_124.setText(_translate("MainWindow", self.articles[self.articleIndex+2]["author"]))
        self.label_125.setText(_translate("MainWindow", self.articles[self.articleIndex+2]["publishedAt"]))
        self.label_126.setText(_translate("MainWindow", self.articles[self.articleIndex+2]["description"]))
        self.label_127.setText(_translate("MainWindow", self.articles[self.articleIndex+2]["content"]))

        self.label_128.setText(_translate("MainWindow", self.articles[self.articleIndex+3]["title"]))
        self.label_129.setText(_translate("MainWindow", self.articles[self.articleIndex+3]["author"]))
        self.label_130.setText(_translate("MainWindow", self.articles[self.articleIndex+3]["publishedAt"]))
        self.label_131.setText(_translate("MainWindow", self.articles[self.articleIndex+3]["description"]))
        self.label_132.setText(_translate("MainWindow", self.articles[self.articleIndex+3]["content"]))

        self.label_133.setText(_translate("MainWindow", self.articles[self.articleIndex+4]["title"]))
        self.label_134.setText(_translate("MainWindow", self.articles[self.articleIndex+4]["author"]))
        self.label_135.setText(_translate("MainWindow", self.articles[self.articleIndex+4]["publishedAt"]))
        self.label_136.setText(_translate("MainWindow", self.articles[self.articleIndex+4]["description"]))
        self.label_137.setText(_translate("MainWindow", self.articles[self.articleIndex+4]["content"]))

        self.label_138.setText(_translate("MainWindow", self.articles[self.articleIndex+5]["title"]))
        self.label_139.setText(_translate("MainWindow", self.articles[self.articleIndex+5]["author"]))
        self.label_140.setText(_translate("MainWindow", self.articles[self.articleIndex+5]["publishedAt"]))
        self.label_141.setText(_translate("MainWindow", self.articles[self.articleIndex+5]["description"]))
        self.label_142.setText(_translate("MainWindow", self.articles[self.articleIndex+5]["content"]))

        self.label_143.setText(_translate("MainWindow", self.articles[self.articleIndex+6]["title"]))
        self.label_144.setText(_translate("MainWindow", self.articles[self.articleIndex+6]["author"]))
        self.label_145.setText(_translate("MainWindow", self.articles[self.articleIndex+6]["publishedAt"]))
        self.label_146.setText(_translate("MainWindow", self.articles[self.articleIndex+6]["description"]))
        self.label_147.setText(_translate("MainWindow", self.articles[self.articleIndex+6]["content"]))

        self.label_148.setText(_translate("MainWindow", self.articles[self.articleIndex+7]["title"]))
        self.label_149.setText(_translate("MainWindow", self.articles[self.articleIndex+7]["author"]))
        self.label_150.setText(_translate("MainWindow", self.articles[self.articleIndex+7]["publishedAt"]))
        self.label_151.setText(_translate("MainWindow", self.articles[self.articleIndex+7]["description"]))
        self.label_152.setText(_translate("MainWindow", self.articles[self.articleIndex+7]["content"]))

        self.label_153.setText(_translate("MainWindow", self.articles[self.articleIndex+8]["title"]))
        self.label_154.setText(_translate("MainWindow", self.articles[self.articleIndex+8]["author"]))
        self.label_155.setText(_translate("MainWindow", self.articles[self.articleIndex+8]["publishedAt"]))
        self.label_156.setText(_translate("MainWindow", self.articles[self.articleIndex+8]["description"]))
        self.label_157.setText(_translate("MainWindow", self.articles[self.articleIndex+8]["content"]))

        self.label_158.setText(_translate("MainWindow", self.articles[self.articleIndex+9]["title"]))
        self.label_159.setText(_translate("MainWindow", self.articles[self.articleIndex+9]["author"]))
        self.label_160.setText(_translate("MainWindow", self.articles[self.articleIndex+9]["publishedAt"]))
        self.label_161.setText(_translate("MainWindow", self.articles[self.articleIndex+9]["description"]))
        self.label_162.setText(_translate("MainWindow", self.articles[self.articleIndex+9]["content"]))
        if (len(self.articles)) > 10:
            self.label_163.setText(_translate("MainWindow", self.articles[self.articleIndex+10]["title"]))
            self.label_164.setText(_translate("MainWindow", self.articles[self.articleIndex+10]["author"]))
            self.label_165.setText(_translate("MainWindow", self.articles[self.articleIndex+10]["publishedAt"]))
            self.label_166.setText(_translate("MainWindow", self.articles[self.articleIndex+10]["description"]))
            self.label_167.setText(_translate("MainWindow", self.articles[self.articleIndex+10]["content"]))

        if (len(self.articles)) > 11:
            self.label_168.setText(_translate("MainWindow", self.articles[self.articleIndex+11]["title"]))
            self.label_169.setText(_translate("MainWindow", self.articles[self.articleIndex+11]["author"]))
            self.label_170.setText(_translate("MainWindow", self.articles[self.articleIndex+11]["publishedAt"]))
            self.label_171.setText(_translate("MainWindow", self.articles[self.articleIndex+11]["description"]))
            self.label_172.setText(_translate("MainWindow", self.articles[self.articleIndex+11]["content"]))

        if (len(self.articles)) > 12:
            self.label_173.setText(_translate("MainWindow", self.articles[self.articleIndex+12]["title"]))
            self.label_174.setText(_translate("MainWindow", self.articles[self.articleIndex+12]["author"]))
            self.label_175.setText(_translate("MainWindow", self.articles[self.articleIndex+12]["publishedAt"]))
            self.label_176.setText(_translate("MainWindow", self.articles[self.articleIndex+12]["description"]))
            self.label_177.setText(_translate("MainWindow", self.articles[self.articleIndex+12]["content"]))

        if (len(self.articles)) > 13:
            self.label_178.setText(_translate("MainWindow", self.articles[self.articleIndex+13]["title"]))
            self.label_179.setText(_translate("MainWindow", self.articles[self.articleIndex+13]["author"]))
            self.label_180.setText(_translate("MainWindow", self.articles[self.articleIndex+13]["publishedAt"]))
            self.label_181.setText(_translate("MainWindow", self.articles[self.articleIndex+13]["description"]))
            self.label_182.setText(_translate("MainWindow", self.articles[self.articleIndex+13]["content"]))

        if (len(self.articles)) > 14:
            self.label_183.setText(_translate("MainWindow", self.articles[self.articleIndex+14]["title"]))
            self.label_184.setText(_translate("MainWindow", self.articles[self.articleIndex+14]["author"]))
            self.label_185.setText(_translate("MainWindow", self.articles[self.articleIndex+14]["publishedAt"]))
            self.label_186.setText(_translate("MainWindow", self.articles[self.articleIndex+14]["description"]))
            self.label_187.setText(_translate("MainWindow", self.articles[self.articleIndex+14]["content"]))
        self.results_label.setText("Results: " + str(self.results))

    def readMoreLink(self):
        self.link_label.setText(f'<a href="{self.articles[self.articleIndex]['url']}">Read more')
        self.link_label.setOpenExternalLinks(True)
        self.link_label_2.setText(f'<a href="{self.articles[self.articleIndex+1]['url']}">Read more')
        self.link_label_2.setOpenExternalLinks(True)
        self.link_label_3.setText(f'<a href="{self.articles[self.articleIndex+2]['url']}">Read more')
        self.link_label_3.setOpenExternalLinks(True)
        self.link_label_4.setText(f'<a href="{self.articles[self.articleIndex+3]['url']}">Read more')
        self.link_label_4.setOpenExternalLinks(True)
        self.link_label_5.setText(f'<a href="{self.articles[self.articleIndex+4]['url']}">Read more')
        self.link_label_5.setOpenExternalLinks(True)
        self.link_label_6.setText(f'<a href="{self.articles[self.articleIndex+5]['url']}">Read more')
        self.link_label_6.setOpenExternalLinks(True)
        self.link_label_7.setText(f'<a href="{self.articles[self.articleIndex+6]['url']}">Read more')
        self.link_label_7.setOpenExternalLinks(True)
        self.link_label_8.setText(f'<a href="{self.articles[self.articleIndex+7]['url']}">Read more')
        self.link_label_8.setOpenExternalLinks(True)
        self.link_label_9.setText(f'<a href="{self.articles[self.articleIndex+8]['url']}">Read more')
        self.link_label_9.setOpenExternalLinks(True)
        self.link_label_10.setText(f'<a href="{self.articles[self.articleIndex+9]['url']}">Read more')
        self.link_label_10.setOpenExternalLinks(True)
        if (len(self.articles)) > 10:
            self.link_label_11.setText(f'<a href="{self.articles[self.articleIndex+10]['url']}">Read more')
            self.link_label_11.setOpenExternalLinks(True)
        if (len(self.articles)) > 11:
            self.link_label_12.setText(f'<a href="{self.articles[self.articleIndex+11]['url']}">Read more')
            self.link_label_12.setOpenExternalLinks(True)
        if (len(self.articles)) > 12:
            self.link_label_13.setText(f'<a href="{self.articles[self.articleIndex+12]['url']}">Read more')
            self.link_label_13.setOpenExternalLinks(True)
        if (len(self.articles)) > 13:
            self.link_label_14.setText(f'<a href="{self.articles[self.articleIndex+13]['url']}">Read more')
            self.link_label_14.setOpenExternalLinks(True)
        if (len(self.articles)) > 14:
            self.link_label_15.setText(f'<a href="{self.articles[self.articleIndex+14]['url']}">Read more')
            self.link_label_15.setOpenExternalLinks(True)
