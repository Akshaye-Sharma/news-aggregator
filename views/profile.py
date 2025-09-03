from config_manager import load_config

class ProfilePage:
    def __init__(self, main_window):
        self.main_window = main_window
        self.buttons()

        config = load_config()
        key = config.get("api_key", None)
        self.main_window.profile_key_entry.setPlaceholderText(key)

    def buttons(self):
        self.main_window.profile_news_button.clicked.connect(self.main_window.showNewsPage)