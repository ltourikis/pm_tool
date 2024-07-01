from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):

    def select_login_button(self):
        self.wait_for_clickable(By.ID, "login").click()

    def login(self, email, password):
        self.wait_for_element(By.ID, "email").send_keys(email)
        self.wait_for_element(By.ID, "password").send_keys(password)
        self.wait_for_element(By.CSS_SELECTOR, '.btn.waves-effect.waves-light').click()
