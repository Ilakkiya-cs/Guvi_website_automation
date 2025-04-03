from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


# Login Page with Exception Handling
class LoginPage(BasePage):
    """
        Page Object Model for the Login Page of GUVI.
        Contains locators and methods related to the login functionality.
        """

    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    SUBMIT_BUTTON = (By.XPATH, "//a[@id='login-btn']")
    ERROR_MESSAGE = (By.CLASS_NAME, "invalid-feedback")
    PROFILE_DROPDOWN = (By.XPATH, "//div[@id='dropdown_container']")
    LOGOUT_BUTTON = (By.XPATH, "//li[div[@id='dropdown_contents']]")

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        #Enters email and password, then clicks the login button
        try:
            self.find_element(*self.EMAIL_FIELD).send_keys(email)
            self.find_element(*self.PASSWORD_FIELD).send_keys(password)
            self.click_element(*self.SUBMIT_BUTTON)
        except Exception as e:
            print(f"Error during login: {e}")

    def get_error_message(self):
        # Retrieves the error message displayed for incorrect login attempts.
        try:
            return self.find_element(*self.ERROR_MESSAGE).text
        except Exception as e:
            print(f"Error fetching error message: {e}")
            return ""

    def logout(self):
        # Logs out from the GUVI account.
        try:
            # Click on Profile Dropdown
            profile_dropdown = self.driver.find_element(*self.PROFILE_DROPDOWN)
            profile_dropdown.click()

            # Click on Sign Out Button
            logout_button = self.driver.find_element(*self.LOGOUT_BUTTON)
            logout_button.click()
        except Exception as e:
            print(f"Error during logout: {e}")
