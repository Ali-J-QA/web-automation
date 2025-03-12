# conftest.py
import pytest
from selenium import webdriver
from config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(Config.URL)
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def signup_page(driver):
    return SignupPage(driver)