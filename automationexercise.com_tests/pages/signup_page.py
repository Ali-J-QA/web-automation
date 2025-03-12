from selenium.webdriver.common.by import By
from config import Config
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class SignupPage(BasePage):
    # Locators for the signup page  
    ENTER_INFO_TEXT = (By.XPATH, '//*[@id="form"]/div/div/div/div[1]/h2/b')
    def wait_for_enter_info_text(self):
        return self.wait_for_element(self.ENTER_INFO_TEXT)

    SIGNUP_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[data-qa="password"]')
    def enter_signup_password(self, password):
        password_field = self.wait_for_element(self.SIGNUP_PASSWORD_FIELD)
        password_field.send_keys(password)

    SIGNUP_MR_RADIO = (By.ID, "id_gender1") #IDs can change
    def select_title_mr(self):
        mr_radio = self.wait_for_element(self.SIGNUP_MR_RADIO)
        if not mr_radio.is_selected():
            mr_radio.click()

    SIGNUP_MRS_RADIO = (By.ID, "id_gender2") #IDs can change
    def select_title_mrs(self):
        mrs_radio = self.wait_for_element(self.SIGNUP_MRS_RADIO)
        if not mrs_radio.is_selected():
            mrs_radio.click()

    SIGNUP_DOB_DAY = (By.CSS_SELECTOR, 'select[data-qa="days"]')
    def select_DOB_day(self, day):
        dob_day_dropdown = self.wait_for_element(self.SIGNUP_DOB_DAY)
        select = Select(dob_day_dropdown)
        select.select_by_value(str(day))

    SIGNUP_DOB_MONTH = (By.CSS_SELECTOR, 'select[data-qa="months"]')
    def select_DOB_month(self, month):
        dob_month_dropdown = self.wait_for_element(self.SIGNUP_DOB_MONTH)
        select = Select(dob_month_dropdown)
        select.select_by_value(str(month))

    SIGNUP_DOB_YEAR = (By.CSS_SELECTOR, 'select[data-qa="years"]')
    def select_DOB_year(self, year):
        dob_year_dropdown = self.wait_for_element(self.SIGNUP_DOB_YEAR)
        select = Select(dob_year_dropdown)
        select.select_by_value(str(year))

    CHECKBOX_NEWSLETTER = (By.ID, "newsletter")
    def select_newsletter(self):
        newsletter = self.wait_for_element(self.CHECKBOX_NEWSLETTER)
        if not newsletter.is_selected():
            newsletter.click()

    CHECKBOX_OFFERS = (By.ID, "optin")
    def select_offers(self):
        offers = self.wait_for_element(self.CHECKBOX_OFFERS)
        if not offers.is_selected():
            offers.click()









