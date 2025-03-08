import pytest
from selenium import webdriver
from pages.home_page import HomePage
from config import Config  

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Config.URL) 
    yield driver
    driver.quit()

def test_home_element_color(driver):
    home_page = HomePage(driver)
    home_page.wait_for_home_element() 
    home_page.validate_home_element_color() 
