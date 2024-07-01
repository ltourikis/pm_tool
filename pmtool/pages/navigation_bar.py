from selenium.webdriver.common.by import By
from .base_page import BasePage


class NavigationBar(BasePage):

    def select_settings_button(self):
        self.wait_for_clickable(By.ID, "settings").click()

    def select_logout_button(self):
        self.wait_for_clickable(By.ID, "logout").click()

    def select_dashboard_button(self):
        self.wait_for_clickable(By.ID, "dashboard").click()

    def select_tasks_db_button(self):
        self.wait_for_clickable(By.ID, "tasks_db").click()
