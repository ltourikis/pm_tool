import logging
from selenium.webdriver.common.by import By
from .base_page import BasePage

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SignupPage(BasePage):
    """
    Page object model for the Signup page.

    Inherits from:
        BasePage: A base class that includes common methods for all pages.
    """

    def select_signup_button(self):
        """
        Click the signup button to navigate to the signup form.
        """
        logger.info("Clicking signup button.")
        self.wait_for_clickable(By.ID, "signup").click()

    def signup(self, name, email, password, company="", address=""):
        """
        Fill out the signup form and submit it.

        Args:
            name (str): Full name of the user.
            email (str): Email address of the user.
            password (str): Password for the user account.
            company (str, optional): Company name (default is an empty string).
            address (str, optional): Address of the user (default is an empty string).
        """
        logger.info("Filling out signup form.")

        # Fill in the full name field
        self.wait_for_element(By.ID, "fullName").send_keys(name)
        logger.info(f"Full name entered: {name}")

        # Fill in the email field
        self.wait_for_element(By.ID, "email").send_keys(email)
        logger.info(f"Email entered: {email}")

        # Fill in the password field
        self.wait_for_element(By.ID, "password").send_keys(password)
        logger.info("Password entered.")

        # Optionally fill in the company field if provided
        if company:
            self.wait_for_element(By.ID, "company").send_keys(company)
            logger.info(f"Company entered: {company}")

        # Optionally fill in the address field if provided
        if address:
            self.wait_for_element(By.ID, "address").send_keys(address)
            logger.info(f"Address entered: {address}")

        # Submit the signup form
        self.wait_for_element(By.CSS_SELECTOR, '.btn.waves-effect.waves-light').click()
        logger.info("Signup form submitted.")
