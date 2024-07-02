from selenium.webdriver.common.by import By
from .base_page import BasePage
import time


class TaskDBPage(BasePage):
    """
    Page Object Model for the TaskDB page.

    Inherits from:
        BasePage: A base class that includes common methods for all pages.
    """

    def check_if_tasks_present(self, task_list):
        for task in task_list:
            self.wait_for_element_in_page_source(task)
            if task not in self.driver.page_source:
                return False
        return True

    def check_if_tasks_not_present(self, task_list):
        for task in task_list:
            if task in self.driver.page_source:
                return False
        return True

    def click_sort(self):
        sort_button = self.wait_for_clickable(By.ID, 'sort_tasks')
        sort_button.click()

    def get_sorted_tasks(self):
        task_titles_elements = self.driver.find_elements(By.ID, 'card_title')
        return [task.text for task in task_titles_elements]

    def get_tasks(self):
        task_titles_elements = self.driver.find_elements(By.ID, 'card_title')
        return [task.text for task in task_titles_elements]

    def search_task(self, task_name):
        """
        Search for a task by name.
        """
        self.wait_for_page_load()
        search_box = self.wait_for_element(By.ID, "search")
        search_box.clear()
        for x in task_name:
            search_box.send_keys(x)
            time.sleep(0.1)
        time.sleep(1)
