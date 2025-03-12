from selenium.webdriver.common.by import By
from config import Config
from pages.base_page import BasePage

class HomePage(BasePage):

    def open(self):
        self.driver.get(Config.URL)

    def get_home_element_color(self):
        home_element = self.wait_for_element(self.HOME_ELEMENT)
        return home_element.value_of_css_property("color")

