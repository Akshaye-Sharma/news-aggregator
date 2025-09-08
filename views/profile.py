from config_manager import load_config, save_config
import sqlite3
import bcrypt
from api.api_request import Api_request

class ProfilePage:
    def __init__(self, main_window):
        self.main_window = main_window
        self.buttons()
        self.editing = False

        self.loadWidgets()

    def loadWidgets(self):
        config = load_config()
        key = config.get("api_key", None)
        self.main_window.profile_key_entry.setPlaceholderText(key)
        self.main_window.add_email_message.hide()

    def updateData(self):
        self.toggleMode(False)
        self.main_window.profile_edit_button.setText("Edit")

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (self.main_window.user_id,))
        user = cursor.fetchone()

        # Sets all input fields to current data
        self.main_window.profile_name_label.setText(user[1] + " " + user[2])
        self.main_window.profile_email_label.setText(user[3])
        self.main_window.profile_first_name.setText(user[1])
        self.main_window.profile_last_name.setText(user[2])
        self.main_window.profile_email.setText(user[3])
        self.main_window.first_email_name.setText(user[3])
        self.main_window.profile_phone_number.setText(user[6])
        self.set_comboBox(self.main_window.profile_phone_code, user[7])
        self.set_comboBox(self.main_window.profile_country, user[8])
        
        cursor.execute("SELECT second_email FROM users WHERE id = ?", (self.main_window.user_id,))
        user = cursor.fetchone()
        if user and user[0] != None:
            self.main_window.second_email_name.setText(user[0])
            self.main_window.second_email_name.show()
            self.main_window.second_email_icon.show()
            self.main_window.second_email_description.show()
            self.main_window.second_email_description.setText("Secondary email")
            self.main_window.delete_second_email.show()
            self.main_window.profile_second_email.hide()
            self.main_window.add_email_button.hide()
        else:
            self.main_window.second_email_name.hide()
            self.main_window.second_email_icon.hide()
            self.main_window.second_email_description.hide()
            self.main_window.delete_second_email.hide()

        conn.commit()
        conn.close()

    # Helper methods for the combobox
    def set_comboBox(self, comboBox, stored_code):
        for i in range(comboBox.count()):
            text = comboBox.itemText(i)
            if text.__contains__(stored_code):
                comboBox.setCurrentIndex(i)
                return

    def saveProfile(self):
        self.first_name = self.main_window.profile_first_name.text()
        self.last_name = self.main_window.profile_last_name.text()
        self.email = self.main_window.profile_email.text()
        self.password = self.main_window.profile_password.text()
        self.phone_code = self.main_window.profile_phone_code.currentText()
        self.phone_code = self.phone_code[self.phone_code.find("("):]
        self.phone_number = self.main_window.profile_phone_number.text()
        self.country = self.main_window.profile_country.currentText()
        self.newKey = self.main_window.profile_key_entry.text()

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT email, id FROM users WHERE email = ? or second_email = ?", (self.main_window.email, self.main_window.email))
        result = cursor.fetchone()

        conn.commit()
        conn.close()
        # Account creation constraints
        if not self.first_name:
            self.main_window.details_entry_message.setText("First name must not be empty")
            self.main_window.details_entry_message.show()
            return
        if not self.last_name:
            self.main_window.details_entry_message.setText("Last name must not be empty")
            self.main_window.details_entry_message.show()
            return
        if self.email != self.main_window.email and ("@" not in self.email or "." not in self.email or len(self.email) < 4):
            self.main_window.details_entry_message.setText("Please enter a valid email")
            self.main_window.details_entry_message.show()
            return
        if result[0] and result[1] != self.main_window.user_id:
            self.main_window.create_account_message.setText("Account with this email already exists")
            self.main_window.create_account_message.show()
            return
        if self.password and len(self.password) < 6:
            self.main_window.details_entry_message.setText("Password must be at least 6 characters long")
            self.main_window.details_entry_message.show()
            return
        if self.password and (self.password.lower().__contains__(self.first_name.lower()) or self.password.lower().__contains__(self.last_name.lower())):
            self.main_window.details_entry_message.setText("Password must not contain your name")
            self.main_window.details_entry_message.show()
            return            
        if not self.phone_number.isdigit() or 11 < len(self.phone_number) or len(self.phone_number) < 6:
            self.main_window.details_entry_message.setText("Please enter a valid phone number")
            self.main_window.details_entry_message.show()
            return
        if not self.country:
            self.main_window.details_entry_message.setText("Please select a country")
            self.main_window.details_entry_message.show()
            return
        if self.newKey and (not self.checkValidKey(self.newKey)):
            self.main_window.details_entry_message.setText("Please enter a valid api key")
            self.main_window.details_entry_message.show()
            return
    
        self.main_window.details_entry_message.setText("Details Saved")
        self.main_window.details_entry_message.show()

        self.main_window.name_label.setText(self.first_name)

        config = load_config()
        config["api_key"] = self.newKey
        config["first_run"] = False
        save_config(config)

        # Encrypt the password
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), salt)
        self.hashed_password_str = self.hashed_password.decode('utf-8')
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        if not self.password:
            cursor.execute("""
            UPDATE users
            SET first_name = ?,
                last_name = ?,
                email = ?,
                phone_number = ?,
                phone_code = ?,
                country = ?
            WHERE id = ?
            """, (self.first_name, self.last_name, self.email,
                self.phone_number, self.phone_code, self.country, self.main_window.user_id))
        else:
            cursor.execute("""
            UPDATE users
            SET first_name = ?,
                last_name = ?,
                email = ?,
                password = ?,
                phone_number = ?,
                phone_code = ?,
                country = ?
            WHERE id = ?
            """, (self.first_name, self.last_name, self.email, self.hashed_password_str,
                self.phone_number, self.phone_code, self.country, self.main_window.user_id))

        conn.commit()
        conn.close()

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

    def editSave(self):
        if not self.editing:
            self.toggleMode(True)
        else:
            self.saveProfile()
            self.toggleMode(False)

    # Switch between editing and saving modes
    def toggleMode(self, editing: bool):
        self.editing = editing
        self.main_window.profile_edit_button.setText("Save" if editing else "Edit")

        self.main_window.profile_first_name.setEnabled(editing)
        self.main_window.profile_last_name.setEnabled(editing)
        self.main_window.profile_email.setEnabled(editing)
        self.main_window.profile_password.setEnabled(editing)
        self.main_window.profile_phone_code.setEnabled(editing)
        self.main_window.profile_phone_number.setEnabled(editing)
        self.main_window.profile_country.setEnabled(editing)
        self.main_window.profile_key_entry.setEnabled(editing)
        self.main_window.add_email_button.setEnabled(editing)
        self.main_window.profile_second_email.setEnabled(editing)
        self.main_window.delete_second_email.setEnabled(editing)

    def addEmail(self):
        self.second_email = self.main_window.profile_second_email.text()
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT email FROM users WHERE email = ? or second_email = ?", (self.second_email, self.second_email))
        result = cursor.fetchone()

        if self.second_email:
            if self.second_email == self.main_window.email:
                self.main_window.add_email_message.show()
                self.main_window.add_email_message.setText("Email already entered")
                self.main_window.second_email_icon.hide()
                self.main_window.second_email_name.hide()
                self.main_window.second_email_description.hide()
                return
            if result:
                self.main_window.add_email_message.show()
                self.main_window.add_email_message.setText("Email unavailable")
                self.main_window.second_email_icon.hide()
                self.main_window.second_email_name.hide()
                self.main_window.second_email_description.hide()
            if "@" not in self.second_email or "." not in self.second_email or len(self.second_email) < 4:
                self.main_window.add_email_message.show()
                self.main_window.add_email_message.setText("Please enter a valid email")
                self.main_window.second_email_icon.hide()
                self.main_window.second_email_name.hide()
                self.main_window.second_email_description.hide()
            else:
                cursor.execute("UPDATE users SET second_email = ? WHERE id = ?", (self.second_email, self.main_window.user_id))
                self.main_window.add_email_message.hide()
                self.main_window.second_email_icon.show()
                self.main_window.second_email_name.setText(self.second_email)
                self.main_window.second_email_name.show()
                self.main_window.second_email_description.show()
                self.main_window.delete_second_email.show()
                self.main_window.profile_second_email.hide()
                self.main_window.add_email_button.hide()

        conn.commit()
        conn.close()
    
    def deleteEmail(self):
        conn = sqlite3.connect("users.db") 
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET second_email = NULL WHERE id = ?", (self.main_window.user_id,))
        conn.commit()
        conn.close()
        self.main_window.second_email_icon.hide()
        self.main_window.second_email_name.hide()
        self.main_window.second_email_description.hide()
        self.main_window.delete_second_email.hide()
        self.main_window.profile_second_email.show()
        self.main_window.add_email_button.show()

    def buttons(self):
        self.main_window.profile_news_button.clicked.connect(self.main_window.showNewsPage)
        self.main_window.profile_edit_button.clicked.connect(self.editSave)
        self.main_window.add_email_button.clicked.connect(self.addEmail)
        self.main_window.delete_second_email.clicked.connect(self.deleteEmail)