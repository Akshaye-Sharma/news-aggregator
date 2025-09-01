from config_manager import load_config
import sqlite3
import bcrypt

class SignInPage:
    def __init__(self, main_window):
        self.main_window = main_window
        self.buttons()

    def account_creation(self):        
        self.first_name = self.main_window.first_name_entry.text()
        self.last_name = self.main_window.last_name_entry.text()
        self.email = self.main_window.create_email_entry.text()
        self.password = self.main_window.create_password_entry.text()
        self.country_code = self.main_window.phone_code_comboBox.currentText()
        self.country_code = self.country_code[self.country_code.find("("):]
        self.phone = self.main_window.phone_number_entry.text()
        self.country = self.main_window.country_comboBox.currentText()
        
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT email FROM users WHERE email = ?", (self.email,))
        result = cursor.fetchone()

        conn.commit()
        conn.close()
        # Account creation constraints
        if not self.first_name:
            self.main_window.create_account_message.setText("First name must not be empty")
            self.main_window.create_account_message.show()
            return
        if not self.last_name:
            self.main_window.create_account_message.setText("Last name must not be empty")
            self.main_window.create_account_message.show()
            return
        if not self.email or "@" not in self.email or "." not in self.email:
            self.main_window.create_account_message.setText("Please enter a valid email")
            self.main_window.create_account_message.show()
            return
        if result is not None:
            self.main_window.create_account_message.setText("Account with this email already exists")
            self.main_window.create_account_message.show()
            return
        if not self.password:
            self.main_window.create_account_message.setText("Password field must not be empty")
            self.main_window.create_account_message.show()
            return
        if len(self.password) < 6:
            self.main_window.create_account_message.setText("Password must be at least 6 characters long")
            self.main_window.create_account_message.show()
            return
        if self.password.lower().__contains__(self.first_name.lower()) or self.password.lower().__contains__(self.last_name.lower()):
            self.main_window.create_account_message.setText("Password must not contain your name")
            self.main_window.create_account_message.show()
            return            
        if not self.phone.isdigit() or 11 < len(self.phone) or len(self.phone) < 6:
            self.main_window.create_account_message.setText("Please enter a valid phone number")
            self.main_window.create_account_message.show()
            return
        if not self.country:
            self.main_window.create_account_message.setText("Please select a country")
            self.main_window.create_account_message.show()
            return
        
        self.phone_number = f"{self.country_code} {self.phone}"
        self.main_window.name_label.setText(self.first_name)

        self.main_window.create_account_message.setText("Account creation successful!")
        self.main_window.create_account_message.show()

        # Encrypt the password
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), salt)
        self.hashed_password_str = self.hashed_password.decode('utf-8')
        if self.email != "":
            self.update_database()
            self.main_window.create_account_submit.setEnabled(False)
    
    def update_database(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO users (first_name, last_name, email, password, phone, country)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (self.first_name, self.last_name, self.email, self.hashed_password_str, self.phone_number, self.country))
        
        conn.commit()
        conn.close()

    def login(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        email = self.main_window.signIn_email.text().strip().lower()
        password = self.main_window.signIn_password.text()

        cursor.execute("SELECT id, email, password, first_name FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if not user:
            self.main_window.signIn_message.setText("Login Failed")
            self.main_window.signIn_message.show()
            conn.close()
            return

        user_id, _, stored_hash, first_name = user
        stored_hash = stored_hash.encode('utf-8')

        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            self.main_window.signIn_message.setText("Login Successful!")
            self.main_window.signIn_submit.setEnabled(False)
            self.main_window.signedIn = True
            self.main_window.user_id = user_id
            self.main_window.name_label.setText(first_name)
        else:
            self.main_window.signIn_message.setText("Login Failed")

        self.main_window.signIn_message.show()
        conn.close()


    def buttons(self):
        self.main_window.create_account_submit.clicked.connect(self.account_creation)
        self.main_window.signIn_submit.clicked.connect(self.login)

        # Hiding message labels
        self.main_window.create_account_message.hide()
        self.main_window.signIn_message.hide()
    
        config = load_config()
        key = config.get("api_key", None)
        self.main_window.key_label.setText("Api key:"+ key)
        tab = self.main_window.currentTab
        self.main_window.news_page_button.clicked.connect(self.main_window.showNewsPage)
