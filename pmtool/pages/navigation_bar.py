import logging
from selenium.webdriver.common.by import By
from .base_page import BasePage

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
        logger.info("Selecting Settings button from navigation bar.")
        self.wait_for_clickable(By.ID, "settings").click()

    def select_logout_button(self):
        """
        Click the logout button in the navigation bar to log out of the application.
        """
        logger.info("Selecting Logout button from navigation bar.")
        self.wait_for_clickable(By.ID, "logout").click()

    def select_dashboard_button(self):
        """
        Click the dashboard button in the navigation bar to navigate to the dashboard.
        """
        logger.info("Selecting Dashboard button from navigation bar.")
        self.wait_for_clickable(By.ID, "dashboard").click()

    def select_tasks_db_button(self):
        """
        Click the tasks database button in the navigation bar to navigate to the task database.
        """
        logger.info("Selecting Tasks Database button from navigation bar.")
        self.wait_for_clickable(By.ID, "task_db").click()
