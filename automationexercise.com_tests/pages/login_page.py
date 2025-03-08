from selenium.webdriver.common.by import By

class LoginPage:
    # Locators for login page elements
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    def __init__(self, driver):
        self.driver = driver
    
    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
    
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
    
    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
