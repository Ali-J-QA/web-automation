# test_home_validation.py
import pytest
from pages.home_page import HomePage
from config import Config

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

def test_home_element_color(home_page):
    home_page.open()  
    element_color = home_page.get_home_element_color()
    assert element_color == Config.EXPECTED_COLOR, f"Expected color {Config.EXPECTED_COLOR}, but got {element_color}"
