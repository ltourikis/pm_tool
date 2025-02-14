import logging
from selenium.webdriver.common.by import By
from .base_page import BasePage

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
        logger.info("Selecting Login button.")
        self.wait_for_clickable(By.ID, "login").click()

    def login(self, email, password):
        """
        Perform the login action by entering the email and password,
        and clicking the submit button.

        Args:
            email (str): The email address to be entered in the email field.
            password (str): The password to be entered in the password field.
        """
        logger.info(f"Logging in with email: {email}")

        self.wait_for_element(By.ID, "email").send_keys(email)
        self.wait_for_element(By.ID, "password").send_keys(password)

        logger.info("Clicking Login submit button.")
        self.wait_for_element(By.CSS_SELECTOR, '.btn.waves-effect.waves-light').click()
