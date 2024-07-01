from selenium.webdriver.common.by import By
from .base_page import BasePage


class SignupPage(BasePage):

    def select_signup_button(self):
        self.wait_for_clickable(By.ID, "signup").click()

    def signup(self, name, email, password, company="", address=""):
        self.wait_for_element(By.ID, "fullName").send_keys(name)
        self.wait_for_element(By.ID, "email").send_keys(email)
        self.wait_for_element(By.ID, "password").send_keys(password)
        if company:
            self.wait_for_element(By.ID, "company").send_keys(company)
        if address:
            self.wait_for_element(By.ID, "address").send_keys(address)
        self.wait_for_element(By.CSS_SELECTOR, '.btn.waves-effect.waves-light').click()
