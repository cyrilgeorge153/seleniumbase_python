from seleniumbase import BaseCase


class Base_Test(BaseCase):
    def setUp(self):
        super().setUp()
        self.open("https://www.saucedemo.com/")
        self.maximize_window()
