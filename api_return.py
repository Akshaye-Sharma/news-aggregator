import requests
from datetime import datetime as dt

# Retrieve articles via API request
class Api_request:
    def __init__(self, apiKey, URL, params):
        self.API_KEY = apiKey
        self.URL = URL
        self.params = params

        self.response = requests.get(self.URL, params=self.params)
        self.articles = []
        self.results = 0

        if self.response.status_code == 200:
            data = self.response.json()
            self.results = data.get("totalResults", 0)

            for article in data.get("articles", []):
                self.articles.append(article)
        else:
            print("Error:", self.response.status_code)
