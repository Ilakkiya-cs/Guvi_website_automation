from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


# Home Page
class HomePage(BasePage):
    """
       Home page object. Contains locators for homepage elements and related actions.
       """

    LOGIN_BUTTON = (By.XPATH, "//a[@id='login-btn']")
    SIGNUP_BUTTON = (By.LINK_TEXT, "Sign up")

    def __init__(self, driver):
        super().__init__(driver)
        self.open_url("https://www.guvi.in")   # Open the homepage

#Checks if the login button is displayed.
    def is_login_button_visible(self):
        return self.is_element_visible(*self.LOGIN_BUTTON)

#Checks if the signup button is displayed
    def is_signup_button_visible(self):
        return self.is_element_visible(*self.SIGNUP_BUTTON)

#Clicks the login button.
    def click_login(self):
        self.click_element(*self.LOGIN_BUTTON)

#Clicks the signup button
    def click_signup(self):
        self.click_element(*self.SIGNUP_BUTTON)
