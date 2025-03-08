from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def validate_element_color(driver, xpath, expected_color, timeout=10):
    """
    Validates if the element located by the given XPath has the expected color.
    
    :param driver: The WebDriver instance.
    :param xpath: The XPath of the element.
    :param expected_color: The expected color in 'rgba' format (e.g., 'rgba(255, 165, 0, 1)').
    :param timeout: Maximum wait time for the element to become visible.
    :return: True if the element has the expected color, False otherwise.
    """
    try:
        # Wait for the element to be visible
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

        # Get the color of the element
        element_color = element.value_of_css_property('color')

        # Compare the color of the element with the expected color
        return element_color == expected_color
    except Exception as e:
        print(f"Error while validating color: {e}")
        return False
