GUVI Website Automation Using Selenium

Project Overview:

This project automates the testing of the GUVI website using Python's Selenium framework. The automation script follows the Page Object Model (POM) for better maintainability and reusability. It includes seven test cases to validate different functionalities of the website. The test cases are executed using pytest, and proper Python exception handling is implemented.

Technologies Used:

1. Python
2. Selenium WebDriver
3. Pytest
4. Page Object Model (POM)

Test Cases Implemented:

1. Validate Webpage URL: Checks whether the webpage "https://www.guvi.in" is valid.
2. Validate Webpage Title: Verifies that the webpage title is "GUVI | Learn to code in your native language".
3. Login Button Visibility and Clickability: Ensures that the login button is visible, clickable, and navigates back.
4. Sign-Up Button Visibility and Clickability: Ensures that the sign-up button is visible, clickable, and navigates back.
5. Sign-Up Page Navigation: Clicks the sign-up button to check if the page exists.
6. Valid Login & Logout: Logs into a GUVI account with valid credentials, verifies login, then logs out.
7. Invalid Login Handling: Attempts login with invalid credentials and captures the error message.

Project Structure:

PAT_mini_project_1/
│──  Tests/
│   ├── test_guvi.py         #  Contains all test cases
│   ├── conftest.py          #  Pytest fixture to initialize WebDriver
│──  Pages/
│   ├── base_page.py         #  Base class for all pages
│   ├── home_page.py         #  Home Page - Handles home page elements
│   ├── login_page.py        #  Login Page - Handles login functionality
│──  Utils/
│   ├── config.py            #  Stores test data (emails, passwords, URLs)
│── README.md                #  Instructions to run the tests


Setup Instructions:
Prerequisites:

Ensure that you have the following installed on your system:
Python (>=3.8)
Google Chrome
ChromeDriver (compatible with your Chrome version)
pip (Python package manager)

Installation Steps:

1.Clone this repository:
git clone https://github.com/yourusername/GUVI_Automation.git
cd GUVI_Automation

2.Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3.Install dependencies:
pip install -r requirements.txt

4.Download ChromeDriver and place it in the drivers/ directory.

Running the Tests:
Run all test cases using: pytest -v tests/

To run a specific test: pytest -v tests/test_guvi.py::test_valid_login

Exception Handling:

* The BasePage class includes exception handling for failed element interactions.
* Try-except blocks are used in all test cases to prevent abrupt failures.
* WebDriverWait ensures elements are properly loaded before interactions.

Contributing:
Feel free to fork this repository and submit pull requests with improvements.



