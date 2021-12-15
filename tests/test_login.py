from selenium.webdriver.common.by import By
from tests.test_base import Base_Test
from pages.login_page import LoginPage


class Login_Test(Base_Test, LoginPage):

    def test_verify_login_page_is_loading_or_not(self):
        # element = self.verify_login_button()
        self.assert_element_present(self.verify_login_button(), by=By.ID)

    def test_verify_swaglabs_logo_is_present_in_login_page(self):
        # element = self.verify_swaglabs_logo()
        self.assert_element_present(self.verify_swaglabs_logo(), by=By.CSS_SELECTOR)
