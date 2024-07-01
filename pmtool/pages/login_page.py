from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object Model for the Login Page.

    Inherits from:
        BasePage: A base class that includes common methods for all pages.
    """

    def select_login_button(self):
        """
        Select the login button on the page.
        """
        self.wait_for_clickable(By.ID, "login").click()

    def login(self, email, password):
        """
        Perform the login action by entering the email and password,
        and clicking the submit button.

        Args:
            email (str): The email address to be entered in the email field.
            password (str): The password to be entered in the password field.
        """
        self.wait_for_element(By.ID, "email").send_keys(email)
        self.wait_for_element(By.ID, "password").send_keys(password)
        self.wait_for_element(By.CSS_SELECTOR, '.btn.waves-effect.waves-light').click()
