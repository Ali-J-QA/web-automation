# home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config  # Import the Config class to access global settings

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Config.URL  # URL is now configurable from Config
        self.home_element_xpath = "/html/body/header/div/div/div/div[2]/div/ul/li[1]/a"
        self.expected_color = Config.EXPECTED_COLOR  # Color is now configurable from Config

    def wait_for_home_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.home_element_xpath))
        )

    def get_home_element_color(self):
        home_element = self.wait_for_home_element()
        return home_element.value_of_css_property('color')

    def validate_home_element_color(self):
        element_color = self.get_home_element_color()
        assert element_color == self.expected_color, f"Expected color {self.expected_color}, but got {element_color}"
