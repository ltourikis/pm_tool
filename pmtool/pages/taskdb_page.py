import logging
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TaskDBPage(BasePage):
    """
    Page Object Model for the TaskDB page.

    Inherits from:
        BasePage: A base class that includes common methods for all pages.
    """

    def check_if_tasks_present(self, task_list):
        """
        Check if all tasks in the task_list are present on the page.

        Args:
            task_list (list): List of task names to check.

        Returns:
            bool: True if all tasks are present, False otherwise.
        """
        logger.info("Checking if tasks are present: {}".format(task_list))
        for task in task_list:
            self.wait_for_element_in_page_source(task)
            if task not in self.driver.page_source:
                logger.info(f"Task '{task}' not found.")
                return False
        return True

    def check_if_tasks_not_present(self, task_list):
        """
        Check if none of the tasks in the task_list are present on the page.

        Args:
            task_list (list): List of task names to check.

        Returns:
            bool: True if none of the tasks are present, False otherwise.
        """
        logger.info("Checking if tasks are not present: {}".format(task_list))
        for task in task_list:
            if task in self.driver.page_source:
                logger.info(f"Task '{task}' found.")
                return False
        return True

    def click_sort(self):
        """
        Click the sort button to sort tasks.
        """
        logger.info("Clicking sort button.")
        sort_button = self.wait_for_clickable(By.ID, 'sort_tasks')
        sort_button.click()

    def get_tasks(self):
        """
        Retrieve the list of task titles.

        Returns:
            list: List of task titles.
        """
        logger.info("Retrieving task titles.")
        task_titles_elements = self.driver.find_elements(By.ID, 'card_title')
        return [task.text for task in task_titles_elements]

    def search_task(self, task_name):
        """
        Search for a task by name.

        Args:
            task_name (str): The name of the task to search for.
        """
        logger.info(f"Searching for task: {task_name}")
        self.wait_for_page_load()
        search_box = self.wait_for_element(By.ID, "search")
        search_box.clear()
        for x in task_name:
            search_box.send_keys(x)
            time.sleep(0.1)  # Add a small delay between keystrokes for realism
        time.sleep(1)  # Wait for search results to appear
