from selenium.webdriver.common.by import By
from config import Config
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators for the login page
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="login-button"]')
    NEW_USER_SIGNUP_TEXT = (By.XPATH, "//h2[text()='New User Signup!']")
    SIGNUP_NAME_FIELD = (By.CSS_SELECTOR, 'input[data-qa="signup-name"]')
    SIGNUP_EMAIL_FIELD = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    SIGNUP_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="signup-button"]')

    def get_login_element_color(self):
        home_element = self.wait_for_element(self.HOME_ELEMENT)
        return home_element.value_of_css_property("color")

    def wait_for_login_page(self):
        self.wait_for_element(self.LOGIN_BUTTON)


    def click_login_button(self):
        login_button = self.wait_for_element(self.LOGIN_BUTTON)
        login_button.click()

    def click_signup_button(self):
        signup_button = self.wait_for_element(self.SIGNUP_BUTTON)
        signup_button.click()
    
    def wait_for_signup_text(self):
        return self.wait_for_element(self.NEW_USER_SIGNUP_TEXT)

    def get_signup_text(self):
        signup_text = self.wait_for_element(self.NEW_USER_SIGNUP_TEXT)
        return signup_text.text
    
    def enter_signup_name(self, name):
        name_field = self.wait_for_element(self.SIGNUP_NAME_FIELD)
        name_field.send_keys(name)
    
    def enter_signup_email(self, email):
        email_field = self.wait_for_element(self.SIGNUP_EMAIL_FIELD)
        email_field.send_keys(email)