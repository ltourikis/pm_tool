import logging
import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SettingsPage(BasePage):
    """
    Page Object Model for the settings page.

    Inherits from:
        BasePage: A base class that includes common methods for all pages.
    """

    def change_settings(self, name="", email="", password="", company="", address="", checkbox=""):
        """
        Change user settings based on provided parameters.

        Args:
            name (str): The new full name of the user.
            email (str): The new email address of the user.
            password (str): The new password for the user account.
            company (str): The new company name of the user.
            address (str): The new address of the user.
            checkbox (str): The action to perform on the 2FA checkbox ('click' to toggle).

        Returns:
            None
        """
        if name:
            self.wait_for_element(By.ID, "fullName").clear()
            time.sleep(1)
            self.wait_for_element(By.ID, "fullName").send_keys(name)
            logger.info(f"Changed full name to: {name}")
        if email:
            self.wait_for_element(By.ID, "email").clear()
            time.sleep(1)
            self.wait_for_element(By.ID, "email").send_keys(email)
            logger.info(f"Changed email to: {email}")
        if password:
            self.wait_for_element(By.ID, "password").clear()
            time.sleep(1)
            self.wait_for_element(By.ID, "password").send_keys(password)
            logger.info("Changed password.")
        if company:
            self.wait_for_element(By.ID, "company").clear()
            time.sleep(1)
            self.wait_for_element(By.ID, "company").send_keys(company)
            logger.info(f"Changed company name to: {company}")
        if address:
            self.wait_for_element(By.ID, "address").clear()
            time.sleep(1)
            self.wait_for_element(By.ID, "address").send_keys(address)
            logger.info(f"Changed address to: {address}")
        if checkbox:
            checkbox_element = self.wait_for_element_present(By.ID, 'has2fa')
            self.driver.execute_script("arguments[0].click();", checkbox_element)
            logger.info("Toggled 2FA checkbox.")

        # Click the save button to apply changes
        self.wait_for_element(By.CSS_SELECTOR, '.btn.waves-effect.waves-light').click()
        logger.info("Settings changes saved.")

    def get_settings(self):
        """
        Retrieve the current user settings from the page.

        Returns:
            dict: A dictionary containing the current settings of the user.
        """
        def is_checked(driver, item_id):
            """
            Check if a checkbox is checked.

            Args:
                driver (WebDriver): The WebDriver instance.
                item_id (str): The ID of the checkbox element.

            Returns:
                bool: True if the checkbox is checked, False otherwise.
            """
            checked = driver.execute_script(
                f"return document.getElementById('{item_id}').checked"
            )
            return checked

        settings = {
            'name': self.wait_for_element(By.ID, "fullName").get_attribute("value"),
            'email': self.wait_for_element(By.ID, "email").get_attribute("value"),
            'password': self.wait_for_element(By.ID, "password").get_attribute("value"),
            'company': self.wait_for_element(By.ID, "company").get_attribute("value"),
            'address': self.wait_for_element(By.ID, "address").get_attribute("value"),
            '2fa': is_checked(self.driver, "has2fa")
        }
        logger.info("Retrieved current user settings.")
        return settings

    def edit_name_to_blank(self):
        """
        Clear name and attempt to update Settings.
        """
        self.wait_for_element(By.ID, "fullName").clear()
        time.sleep(1)
        self.wait_for_element(By.ID, "email").click()  # Click to trigger any validation
        self.wait_for_element(By.CSS_SELECTOR, '.btn.waves-effect.waves-light').click()
        logger.info("Cleared name field and attempted to update Settings.")

    def edit_email_to_blank(self):
        """
        Clear email and attempt to update Settings.
        """
        self.wait_for_clickable(By.ID, "email").clear()
        time.sleep(1)
        self.wait_for_element(By.ID, "fullName").click()  # Click to trigger any validation
        self.wait_for_element(By.CSS_SELECTOR, '.btn.waves-effect.waves-light').click()
        logger.info("Cleared email field and attempted to update Settings.")

    def edit_password_to_blank(self):
        """
        Clear password and attempt to update Settings.
        """
        self.wait_for_clickable(By.ID, "password").clear()
        time.sleep(1)
        self.wait_for_element(By.ID, "fullName").click()  # Click to trigger any validation
        self.wait_for_element(By.CSS_SELECTOR, '.btn.waves-effect.waves-light').click()
        logger.info("Cleared password field and attempted to update Settings.")
