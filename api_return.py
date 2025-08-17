import requests
from datetime import datetime as dt

# Retrieve and filter articles via API
class Api_request:
    def __init__(self, apiKey, URL, params):
        self.API_KEY = apiKey
        self.URL = URL
        self.params = params

        self.response = requests.get(self.URL, params=self.params)
        self.articles = []
        self.results = 0
        self.retrieving()

    def retrieving(self):
        if self.response.status_code == 200:
            data = self.response.json()
            self.results = data.get("totalResults", 0)

            # Filter articles to only include features
            for article in data.get("articles", []):
                if all([
                    article.get("title"),
                    article.get("description"),
                    article.get("content"),
                    article.get("url")
                ]): # If data is missing
                    article["author"] = article.get("author") or "Unknown author"
                    article["publishedAt"] = article.get("publishedAt") or "Unknown date"
                    self.articles.append(article)
        else:
            print("Error:", self.response.status_code)

        self.convert_time()

    # Format time displayed on articles
    def convert_time(self):
        for article in self.articles:
            try:
                date = dt.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
                formatted = date.strftime("%B %d, %Y at %I:%M %p UTC")
                article["publishedAt"] = formatted
            except Exception:
                pass  # In the event that the parsing fails
