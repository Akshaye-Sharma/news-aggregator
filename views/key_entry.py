from config_manager import load_config, is_first_run, save_config
from api.api_params import Api_params
from api.api_request import Api_request

class KeyEntryPage:
    def __init__(self, main_window):
        self.main_window = main_window
        self.create_widgets()

    def create_widgets(self):
        self.main_window.newsAPI_link.setText(f'<a href="https://newsapi.org">NewsAPI.org')
        self.main_window.newsAPI_link.setOpenExternalLinks(True)
        self.main_window.api_enter_button.clicked.connect(self.handle_key_entry)
        self.main_window.key_entry_message.hide()

    def handle_key_entry(self):
        api_key = self.main_window.api_entry.text().strip()
        if not api_key:
            self.main_window.key_entry_message.setText("Key cannot be empty")
            self.main_window.key_entry_message.show()
            return

        if self.checkValidKey(api_key):
            # Save key + mark as not first run
            config = load_config()
            config["api_key"] = api_key
            config["first_run"] = False
            save_config(config)

            # Switch to main news page
            self.main_window.stackedWidget.setCurrentWidget(self.main_window.news_page)
            self.main_window.news_service = Api_params()
            self.main_window.load_articles("Top US")
            self.main_window.key_label.setText("Api key:"+ api_key)
        else:
            self.main_window.key_entry_message.setText("Invalid API Key")
            self.main_window.key_entry_message.show()
    
    def checkValidKey(self, api_key: str) -> bool:
        """Make a quick test request to validate API key"""
        try:
            url = "https://newsapi.org/v2/top-headlines"
            params = {"country": "us", "category": "business", "apiKey": api_key}
            test_req = Api_request(api_key, url, params)
            return test_req.response.status_code == 200
        except Exception as e:
            print("Error checking key:", e)
            return False
