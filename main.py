import sys
from PyQt5.QtWidgets import QApplication
from api_return import Api_request
from views.main_window import MainWindow
import os

def create_request():
    API_KEY = os.getenv("API_KEY")
    URL2 = "https://newsapi.org/v2/everything"
    params2 = {
        "q": "tesla", 
        "apiKey": API_KEY
    }
    request = Api_request(API_KEY, URL2, params2)
    return request.articles, request.results


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Get API data
    articles, results = create_request()

    window = MainWindow(articles, results)
    window.show()

    sys.exit(app.exec_())
    