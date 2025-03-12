from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    HOME_ELEMENT = (By.LINK_TEXT, "Home")
    SIGNUP_LOGIN_ELEMENT = (By.LINK_TEXT, "Signup / Login")
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def click_home_element(self):
        home_button = self.wait_for_element(self.HOME_ELEMENT)
        home_button.click()
    
    def click_signup_login_element(self):
        signup_login_button = self.wait_for_element(self.SIGNUP_LOGIN_ELEMENT)
        signup_login_button.click()