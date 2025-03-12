# test_register_user.py
import pytest
from config import Config

def test_register_user(home_page, login_page, signup_page):
    #step 1 and 2 - launch browser and navigate to home URL
    home_page.open() 
    element_color = home_page.get_home_element_color()

    #step 3 - validate page
    assert element_color == Config.EXPECTED_COLOR, f"Expected color {Config.EXPECTED_COLOR}, but got {element_color}"

    #step 4 - click 'Signup/Login' button
    home_page.click_signup_login_element()
    login_page.wait_for_login_page()
    signup_text = login_page.wait_for_signup_text()

    #step 5 - verify text
    assert signup_text.is_displayed(), "'New User Signup!' is not visible"

    #step 6 - enter name and email address
    login_page.enter_signup_name(Config.USERNAME)
    login_page.enter_signup_email(Config.EMAIL)

    #step 7 - click 'Signup'
    login_page.click_signup_button()

    #step 8 verify 'ENTER ACCOUNT INFORMATION'
    enter_info_text = signup_page.wait_for_enter_info_text()
    assert enter_info_text.is_displayed(), "'Enter Account Information' is not visible"

    #step 9 complete: Title, Name, Email, Password, DoB
    """since no radio button is specified, I will select one. In a real world, check this with stakeholders!"""
    signup_page.select_title_mr()
    #assert login_page.is_title_mr_selected(), "Mr radio button was not selected"
    """name and email already entered"""
    signup_page.enter_signup_password(Config.PASSWORD)
    signup_page.select_DOB_day(25)
    signup_page.select_DOB_month(12)
    signup_page.select_DOB_year(1977)

    #step 10 select checkbox 'Sign up for our newsletter!'
    signup_page.select_newsletter()

    #step 11 select checkbox 'Receive special offers from our partners'
    signup_page.select_offers()

    #step 12 complete: first name, last name, company, address
    #        address 2, country, state, city, zipcode, mobile
    #step 13 click 'create account'
    #step 14 verify 'ACCOUNT CREATED!' is visible
    #step 15 click 'Continue'
    #step 16 verify 'Logged in as ...' is visibile
    #step 17 click 'Delete Account'
    #step 18 verify 'Account Deleted' is visible


