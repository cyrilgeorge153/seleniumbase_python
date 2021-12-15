from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class HomePage(BaseCase):
    heading_products_css = ".title"
    btn_cart_css = ".shopping_cart_link"

    def verify_heading_products(self):
        self.highlight(HomePage.heading_products_css, by=By.CSS_SELECTOR)
        return self.heading_products_css

    def get_products_heading_text(self):
        self.highlight(HomePage.heading_products_css, by=By.CSS_SELECTOR)
        return self.get_text(HomePage.heading_products_css, by=By.CSS_SELECTOR)

    def verify_btn_cart(self):
        self.highlight(HomePage.btn_cart_css, by=By.CSS_SELECTOR)
        return self.btn_cart_css


