from seleniumbase import BaseCase
from selenium.webdriver.common.by import By


class LoginPage(BaseCase):
    txt_username_id = "user-name"
    txt_password_id = "password"
    btn_login_id = "login-button"
    logo_swaglabs_css = "div.login_logo"

    def verify_login_button(self):
        self.highlight(LoginPage.btn_login_id, by=By.ID)
        return self.btn_login_id

    def verify_swaglabs_logo(self):
        self.highlight(LoginPage.logo_swaglabs_css, by=By.CSS_SELECTOR)
        return self.logo_swaglabs_css

    def login_swaglabs(self, username="standard_user", password="secret_sauce"):
        self.clear(LoginPage.txt_username_id, by=By.ID)
        self.highlight(LoginPage.txt_username_id, by=By.ID)
        self.type(LoginPage.txt_username_id, username, by=By.ID)
        self.clear(LoginPage.txt_password_id, by=By.ID)
        self.highlight(LoginPage.txt_password_id, by=By.ID)
        self.type(LoginPage.txt_password_id, password, by=By.ID)
        self.highlight(LoginPage.btn_login_id, by=By.ID)
        self.click(LoginPage.btn_login_id, by=By.ID)
