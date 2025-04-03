from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Utils.config import VALID_EMAIL, VALID_PASSWORD, INVALID_EMAIL, INVALID_PASSWORD
from time import sleep


def test_webpage_valid(driver):
    # Test to check if the webpage URL is correct.
    home = HomePage(driver)
    assert "https://www.guvi.in" in driver.current_url.lower()
    print("The given URL is valid")
    sleep(2)


def test_title_of_webpage(driver):
    # Test to check if the webpage title is correct.
    home = HomePage(driver)
    assert home.get_title() == "GUVI | Learn to code in your native language"
    print("Title of the webpage is : 'GUVI | Learn to code in your native language'")
    sleep(2)


def test_login_button_clickable(driver):
    # Test to check if the login button is visible and functional
    home = HomePage(driver)
    assert home.is_login_button_visible()
    home.click_login()
    sleep(2)
    driver.back()
    print("The login button is visible and clickable")


def test_signup_button_clickable(driver):
    # Test to check if the signup button is visible and functional.
    home = HomePage(driver)
    assert home.is_signup_button_visible()
    home.click_signup()
    sleep(2)
    driver.back()
    print("The signup button is visible and clickable")


def test_signup_navigation(driver):
    # Test to check if the signup button correctly navigates to the signup page
    home = HomePage(driver)
    home.click_signup()
    assert "https://www.guvi.in/register/" in driver.current_url.lower()
    sleep(2)
    driver.back()
    print("The given webpage exists")


def test_valid_login(driver):
    # Test for a successful login and logout scenario
    home = HomePage(driver)
    home.click_login()
    login = LoginPage(driver)
    login.login(VALID_EMAIL, VALID_PASSWORD)
    assert "https://www.guvi.in/sign-in/" in driver.current_url.lower()
    print("The Login was successful")
    sleep(3)
    login.logout()
    assert "https://www.guvi.in/" in driver.current_url.lower()
    print("The Logout was successful")
    sleep(3)


def test_invalid_login(driver):
    # Test for an invalid login attempt.
    home = HomePage(driver)
    home.click_login()
    login = LoginPage(driver)
    login.login(INVALID_EMAIL, INVALID_PASSWORD)
    assert "" in login.get_error_message()
    print("Error Message : Incorrect Email or Password")
