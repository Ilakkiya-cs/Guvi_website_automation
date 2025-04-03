import pytest
from selenium import webdriver


# Pytest Test Cases
@pytest.fixture(scope="function")
def driver():

    """
     Pytest fixture to initialize WebDriver before each test.
       Closes the browser after test execution.
    """

    driver = webdriver.Chrome()
    driver.maximize_window()
    # Passing driver instance to test
    yield driver
    driver.quit()
