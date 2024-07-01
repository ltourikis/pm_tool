from selenium.webdriver.common.by import By
from .base_page import BasePage


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
            self.wait_for_element(By.ID, "fullName").send_keys(name)
        if email:
            self.wait_for_element(By.ID, "email").clear()
            self.wait_for_element(By.ID, "email").send_keys(email)
        if password:
            self.wait_for_element(By.ID, "password").clear()
            self.wait_for_element(By.ID, "password").send_keys(password)
        if company:
            self.wait_for_element(By.ID, "company").clear()
            self.wait_for_element(By.ID, "company").send_keys(company)
        if address:
            self.wait_for_element(By.ID, "address").clear()
            self.wait_for_element(By.ID, "address").send_keys(address)
        if checkbox:
            checkbox_element = self.wait_for_element_present(By.ID, 'has2fa')
            self.driver.execute_script("arguments[0].click();", checkbox_element)

        # Click the save button to apply changes
        self.wait_for_element(By.CSS_SELECTOR, '.btn.waves-effect.waves-light').click()

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
        return settings
