from selenium.webdriver.common.by import By
from .base_page import BasePage


class NavigationBar(BasePage):
    """
    NavigationBar handles the interactions with the navigation bar in the application.

    Inherits from:
        BasePage: A base class that includes common methods for all pages.
    """

    def select_settings_button(self):
        """
        Click the settings button in the navigation bar.
        """
        self.wait_for_clickable(By.ID, "settings").click()

    def select_logout_button(self):
        """
        Click the logout button in the navigation bar to log out of the application.
        """
        self.wait_for_clickable(By.ID, "logout").click()

    def select_dashboard_button(self):
        """
        Click the dashboard button in the navigation bar to navigate to the dashboard.
        """
        self.wait_for_clickable(By.ID, "dashboard").click()

    def select_tasks_db_button(self):
        """
        Click the tasks database button in the navigation bar to navigate to the tasks database.
        """
        self.wait_for_clickable(By.ID, "tasks_db").click()
