from parameterized import parameterized
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from tests.test_base import Base_Test
from pages.login_page import LoginPage


class Home_Test(Base_Test, LoginPage, HomePage):

    def test_verify_home_page_is_loading_or_not(self):
        self.login_swaglabs()
        # element = self.verify_heading_products()
        # self.assert_element_present(self.verify_heading_products(), by=By.CSS_SELECTOR)
        self.assertEqual(self.get_products_heading_text(), "PRODUCTS", "heading is not matching")

    def test_verify_swaglabs_cart_button_is_present_in_home_page(self):
        self.login_swaglabs()
        # element = self.verify_btn_cart()
        self.assert_element_present(self.verify_btn_cart(), by=By.CSS_SELECTOR)
