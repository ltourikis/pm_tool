from selenium.webdriver.common.by import By
from .base_page import BasePage
import time


class SettingsPage(BasePage):

    def change_settings(self, name="", email="", password="", company="", address="", checkbox=""):
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
        self.wait_for_element(By.CSS_SELECTOR, '.btn.waves-effect.waves-light').click()

    # def get_settings(self):
    #
    #     settings = {'name': self.wait_for_element(By.ID, "fullName").get_attribute("value"),
    #                 'email': self.wait_for_element(By.ID, "email").get_attribute("value"),
    #                 'password': self.wait_for_element(By.ID, "password").get_attribute("value"),
    #                 'company': self.wait_for_element(By.ID, "company").get_attribute("value"),
    #                 'address': self.wait_for_element(By.ID, "address").get_attribute("value"),
    #                 '2fa': self.wait_for_clickable(By.ID, "has2fa").is_selected()}
    #     return settings

    def get_settings(self):
        def is_checked(driver, item_id):
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
