from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Base Page with Exception Handling
class BasePage:

    """
     A base class that all other page classes will inherit.
     Contains common functionalities like clicking, entering text, and waiting for elements.
     """

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

        """   Initializes the BasePage class.
              WebDriver instance used to interact with the browser.
              This class serves as a parent for other page objects, providing common functionalities.
              """

    # Method to open a specific URL
    def open_url(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(f"Error opening URL {url}: {e}")

    # Returns the title of the current webpage.
    def get_title(self):
        try:
            return self.driver.title
        except Exception as e:
            print(f"Error getting title: {e}")
            return None

    # Method to find an element with explicit wait
    def find_element(self, by, value):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))
        except Exception as e:
            print(f"Error finding element {value}: {e}")
            return None

    # Waits for an element to be clickable and then clicks it.
    def click_element(self, by, value):
        try:
            element = self.find_element(by, value)
            if element:
                element.click()
        except Exception as e:
            print(f"Error clicking element {value}: {e}")

    # Check if the element is visible or not
    def is_element_visible(self, by, value):
        try:
            element = self.find_element(by, value)
            return element.is_displayed() if element else False
        except Exception as e:
            print(f"Error checking visibility of {value}: {e}")
            return False