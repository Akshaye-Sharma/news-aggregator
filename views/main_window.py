from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, articles, results):
        super().__init__()
        self.articles = articles
        self.results = results
        self.setupUi(self)
        self.createButtons()
        self.showArticles()

    def createButtons(self):
        self.signIn_button.clicked.connect(self.showSignInPage)
        self.skip_button.clicked.connect(self.showNewsPage)

    def showSignInPage(self):
        self.stackedWidget.setCurrentWidget(self.registration_page)
    
    def showNewsPage(self):
        self.stackedWidget.setCurrentWidget(self.news_page)

    def showArticles(self):
        _translate = QtCore.QCoreApplication.translate

        self.label_73.setText(_translate("MainWindow", self.articles[0]["title"]))
        self.label_74.setText(_translate("MainWindow", self.articles[0]["author"]))
        self.label_75.setText(_translate("MainWindow", self.articles[0]["publishedAt"]))
        self.label_76.setText(_translate("MainWindow", self.articles[0]["description"]))
        self.label_77.setText(_translate("MainWindow", self.articles[0]["content"]))

        self.label_78.setText(_translate("MainWindow", self.articles[1]["title"]))
        self.label_79.setText(_translate("MainWindow", self.articles[1]["author"]))
        self.label_80.setText(_translate("MainWindow", self.articles[1]["publishedAt"]))
        self.label_81.setText(_translate("MainWindow", self.articles[1]["description"]))
        self.label_82.setText(_translate("MainWindow", self.articles[1]["content"]))

        self.label_123.setText(_translate("MainWindow", self.articles[2]["title"]))
        self.label_124.setText(_translate("MainWindow", self.articles[2]["author"]))
        self.label_125.setText(_translate("MainWindow", self.articles[2]["publishedAt"]))
        self.label_126.setText(_translate("MainWindow", self.articles[2]["description"]))
        self.label_127.setText(_translate("MainWindow", self.articles[2]["content"]))

        self.label_128.setText(_translate("MainWindow", self.articles[3]["title"]))
        self.label_129.setText(_translate("MainWindow", self.articles[3]["author"]))
        self.label_130.setText(_translate("MainWindow", self.articles[3]["publishedAt"]))
        self.label_131.setText(_translate("MainWindow", self.articles[3]["description"]))
        self.label_132.setText(_translate("MainWindow", self.articles[3]["content"]))

        self.label_133.setText(_translate("MainWindow", self.articles[4]["title"]))
        self.label_134.setText(_translate("MainWindow", self.articles[4]["author"]))
        self.label_135.setText(_translate("MainWindow", self.articles[4]["publishedAt"]))
        self.label_136.setText(_translate("MainWindow", self.articles[4]["description"]))
        self.label_137.setText(_translate("MainWindow", self.articles[4]["content"]))

        self.label_138.setText(_translate("MainWindow", self.articles[5]["title"]))
        self.label_139.setText(_translate("MainWindow", self.articles[5]["author"]))
        self.label_140.setText(_translate("MainWindow", self.articles[5]["publishedAt"]))
        self.label_141.setText(_translate("MainWindow", self.articles[5]["description"]))
        self.label_142.setText(_translate("MainWindow", self.articles[5]["content"]))

        self.label_143.setText(_translate("MainWindow", self.articles[6]["title"]))
        self.label_144.setText(_translate("MainWindow", self.articles[6]["author"]))
        self.label_145.setText(_translate("MainWindow", self.articles[6]["publishedAt"]))
        self.label_146.setText(_translate("MainWindow", self.articles[6]["description"]))
        self.label_147.setText(_translate("MainWindow", self.articles[6]["content"]))

        self.label_148.setText(_translate("MainWindow", self.articles[7]["title"]))
        self.label_149.setText(_translate("MainWindow", self.articles[7]["author"]))
        self.label_150.setText(_translate("MainWindow", self.articles[7]["publishedAt"]))
        self.label_151.setText(_translate("MainWindow", self.articles[7]["description"]))
        self.label_152.setText(_translate("MainWindow", self.articles[7]["content"]))

        self.label_153.setText(_translate("MainWindow", self.articles[8]["title"]))
        self.label_154.setText(_translate("MainWindow", self.articles[8]["author"]))
        self.label_155.setText(_translate("MainWindow", self.articles[8]["publishedAt"]))
        self.label_156.setText(_translate("MainWindow", self.articles[8]["description"]))
        self.label_157.setText(_translate("MainWindow", self.articles[8]["content"]))

        self.label_158.setText(_translate("MainWindow", self.articles[9]["title"]))
        self.label_159.setText(_translate("MainWindow", self.articles[9]["author"]))
        self.label_160.setText(_translate("MainWindow", self.articles[9]["publishedAt"]))
        self.label_161.setText(_translate("MainWindow", self.articles[9]["description"]))
        self.label_162.setText(_translate("MainWindow", self.articles[9]["content"]))

        self.label_163.setText(_translate("MainWindow", self.articles[10]["title"]))
        self.label_164.setText(_translate("MainWindow", self.articles[10]["author"]))
        self.label_165.setText(_translate("MainWindow", self.articles[10]["publishedAt"]))
        self.label_166.setText(_translate("MainWindow", self.articles[10]["description"]))
        self.label_167.setText(_translate("MainWindow", self.articles[10]["content"]))

        self.label_168.setText(_translate("MainWindow", self.articles[11]["title"]))
        self.label_169.setText(_translate("MainWindow", self.articles[11]["author"]))
        self.label_170.setText(_translate("MainWindow", self.articles[11]["publishedAt"]))
        self.label_171.setText(_translate("MainWindow", self.articles[11]["description"]))
        self.label_172.setText(_translate("MainWindow", self.articles[11]["content"]))

        self.label_173.setText(_translate("MainWindow", self.articles[12]["title"]))
        self.label_174.setText(_translate("MainWindow", self.articles[12]["author"]))
        self.label_175.setText(_translate("MainWindow", self.articles[12]["publishedAt"]))
        self.label_176.setText(_translate("MainWindow", self.articles[12]["description"]))
        self.label_177.setText(_translate("MainWindow", self.articles[12]["content"]))

        self.label_178.setText(_translate("MainWindow", self.articles[13]["title"]))
        self.label_179.setText(_translate("MainWindow", self.articles[13]["author"]))
        self.label_180.setText(_translate("MainWindow", self.articles[13]["publishedAt"]))
        self.label_181.setText(_translate("MainWindow", self.articles[13]["description"]))
        self.label_182.setText(_translate("MainWindow", self.articles[13]["content"]))

        self.label_183.setText(_translate("MainWindow", self.articles[14]["title"]))
        self.label_184.setText(_translate("MainWindow", self.articles[14]["author"]))
        self.label_185.setText(_translate("MainWindow", self.articles[14]["publishedAt"]))
        self.label_186.setText(_translate("MainWindow", self.articles[14]["description"]))
        self.label_187.setText(_translate("MainWindow", self.articles[14]["content"]))
        self.results_label.setText("Results: " + str(self.results))
