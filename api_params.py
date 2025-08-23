from api_return import Api_request
import os
import random as r

# Sets up paramters for API request
class Api_params:
    def __init__(self):
        self.API_KEY = os.getenv("API_KEY")
        self.BASE = "https://newsapi.org/v2/everything"
        self.TOP_HEADLINES = "https://newsapi.org/v2/top-headlines"

    def fetch_articles(self, topic: str):
        if topic == "Tesla":
            params = {"q": "tesla", "apiKey": self.API_KEY}
            url = self.BASE
        elif topic == "Apple":
            params = {
                "q": "apple",
                "from": "2025-08-18",
                "to": "2025-08-18",
                "sortBy": "popularity",
                "apiKey": self.API_KEY
            }
            url = self.BASE
        elif topic == "Wall Street Journal":
            params = {"domains": "wsj.com", "apiKey": self.API_KEY}
            url = self.BASE
        elif topic == "Top US":
            params = {"country": "us", "category": "business", "apiKey": self.API_KEY}
            url = "https://newsapi.org/v2/top-headlines"
        else:
            raise ValueError(f"Unknown topic: {topic}")
        
        request = Api_request(self.API_KEY, url, params)
        self.articles = request.articles
        self.results = request.results
        if len(self.articles) < 15:
            self.articleIndex = 0
        else:
            self.articleIndex = r.randint(0, len(self.articles) - 15)

        return self.articles, self.results, self.articleIndex