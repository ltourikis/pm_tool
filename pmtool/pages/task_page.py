import logging
from selenium.webdriver.common.by import By
from .base_page import BasePage

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TaskPage(BasePage):
    """
    Page object model for the Tasks page.

    Inherits from:
        BasePage: A base class that includes common methods for all pages.
    """

    def __init__(self, driver):
        """
        Initialize the Tasks Page with a WebDriver instance.
        Tasks Page has increased custom delay compared to Base Page.
        """
        super().__init__(driver)
        self.custom_delay = 0.5  # Set a custom delay for actions on this page

    labels = ["frontend", "backend", "design", "testing", "performance", "techdept", "ci", "jenkins"]
    status = ["TO DO", "IN PROGRESS", "DONE", "IN REVIEW"]

    # Paths to files for uploading tasks
    file1_path = r"C:\Users\loukas\Scripts\pmtool_tests\pmtool\files_for_upload\file1.txt"
    file2_path = r"C:\Users\loukas\Scripts\pmtool_tests\pmtool\files_for_upload\file2.txt"
    file3_path = r"C:\Users\loukas\Scripts\pmtool_tests\pmtool\files_for_upload\file3.txt"

    def create_task(self, task_summary, task_description, status="", labels="", files=""):
        """
        Create a new task with the given details.

        Args:
            task_summary (str): The summary of the task.
            task_description (str): The description of the task.
            status (str, optional): The status of the task. Defaults to "".
            labels (str, optional): The labels to be added to the task. Defaults to "".
            files (str, optional): The files to be uploaded with the task. Defaults to "".
        """
        logger.info(f"Creating task: {task_summary}")
        self.wait_for_element(By.ID, "summary").send_keys(task_summary)
        self.wait_for_element(By.ID, "description").send_keys(task_description)
        if status:
            logger.info(f"Setting status to: {status}")
            self.select_from_dropdown(".select-dropdown.dropdown-trigger", status)
        if labels:
            logger.info(f"Adding labels: {labels}")
            self.select_options_from_select_box("search_input", "optionContainer", labels)
            self.wait_for_element(By.ID, "summary").click()  # Click to close dropdown
        if files:
            logger.info(f"Uploading files: {files}")
            for file in files:
                self.upload_file("attachments", file)

        self.wait_for_clickable(By.XPATH, "//button[contains(text(), 'Create')]").click()

    def click_edit_task(self, task_summary):
        """
        Click the edit button for a task with the given summary.

        Args:
            task_summary (str): The summary of the task to be edited.
        """
        logger.info(f"Editing task: {task_summary}")
        task = (f'//span[text()="{task_summary}"]/ancestor::div[contains(@class, "card")]/div['
                f'@class="card-action"]/')
        self.wait_for_clickable(By.XPATH, task + 'a[@id="btn_update_task"]').click()
        self.wait_for_page_load()

    def edit_task(self, task_summary="", task_description="", status="", add_labels="", remove_labels="",
                  add_files="", remove_files=""):
        """
        Edit an existing task with the given details.

        Args:
            task_summary (str, optional): The new summary for the task. Defaults to "".
            task_description (str, optional): The new description for the task. Defaults to "".
            status (str, optional): The new status for the task. Defaults to "".
            add_labels (str, optional): Labels to be added to the task. Defaults to "".
            remove_labels (str, optional): Labels to be removed from the task. Defaults to "".
            add_files (str, optional): Files to be added to the task. Defaults to "".
            remove_files (str, optional): Files to be removed from the task. Defaults to "".
        """
        if task_summary:
            logger.info(f"Editing task summary to: {task_summary}")
            self.wait_for_clickable(By.ID, "summary").clear()
            self.wait_for_element(By.ID, "summary").send_keys(task_summary)
        if task_description:
            logger.info(f"Editing task description to: {task_description}")
            self.wait_for_element(By.ID, "description").clear()
            self.wait_for_element(By.ID, "description").send_keys(task_description)
        if status:
            logger.info(f"Setting status to: {status}")
            self.select_from_dropdown(".select-dropdown.dropdown-trigger", status)
        if add_labels:
            logger.info(f"Adding labels: {add_labels}")
            self.select_options_from_select_box("search_input", "optionContainer", add_labels)
            self.wait_for_element(By.ID, "summary").click()  # Click to close dropdown
        if remove_labels:
            logger.info(f"Removing labels: {remove_labels}")
            for label in remove_labels:
                self.remove_label(label)
                self.wait_for_clickable(By.ID, "summary").click()  # Click to refresh state
        if add_files:
            logger.info(f"Adding files: {add_files}")
            for file in add_files:
                self.upload_file("attachments", file)
                self.wait_for_clickable(By.ID, "summary").click()  # Click to refresh state
        if remove_files:
            logger.info(f"Removing files: {remove_files}")
            for file in remove_files:
                self.remove_file(file)
                self.wait_for_clickable(By.ID, "summary").click()  # Click to refresh state
        self.wait_for_clickable(By.XPATH, "//button[contains(text(), 'Update')]").click()

    def edit_summary_blank(self):
        """
        Clear the task summary and attempt to update the task.
        """
        logger.info("Editing task summary to blank")
        self.wait_for_clickable(By.ID, "summary").clear()
        self.wait_for_element(By.ID, "description").click()  # Click to trigger any validation
        self.wait_for_clickable(By.XPATH, "//button[contains(text(), 'Update')]").click()

    def edit_description_blank(self):
        """
        Clear the task description and attempt to update the task.
        """
        logger.info("Editing task description to blank")
        self.wait_for_clickable(By.ID, "description").clear()
        self.wait_for_element(By.ID, "summary").click()  # Click to trigger any validation
        self.wait_for_clickable(By.XPATH, "//button[contains(text(), 'Update')]").click()

    def check_if_task_present(self, task_summary, task_description, status_column, labels="", files=""):
        """
        Check if a task with the given details is present in the specified column.

        Args:
            task_summary (str): The summary of the task.
            task_description (str): The description of the task.
            status_column (str): The column where the task is expected to be.
            labels (str, optional): The labels associated with the task. Defaults to "".
            files (str, optional): The files associated with the task. Defaults to "".

        Returns:
            bool: True if the task is present, False otherwise.
        """
        logger.info(f"Checking if task '{task_summary}' with description '{task_description}' is present in "
                    f"'{status_column}' column")
        column = self.wait_for_element(By.ID, f"{status_column.lower().replace(' ', '_')}_items")
        child_element = column.find_element(By.XPATH, f".//*[contains(text(), '{task_summary}')]")
        if not child_element:
            return False
        child_element = column.find_element(By.XPATH, f".//*[contains(text(), '{task_description}')]")
        if not child_element:
            return False
        if labels:
            for label in labels:
                if not column.find_element(By.XPATH, f".//*[contains(text(), '{label}')]"):
                    return False
        if files:
            for file in files:
                file_name = file.split("\\")[-1]
                if not column.find_element(By.XPATH, f".//*[contains(text(), '{file_name}')]"):
                    return False
        return True

    def delete_task(self, task_summary):
        """
        Delete a task with the given summary.

        Args:
            task_summary (str): The summary of the task to be deleted.
        """
        logger.info(f"Deleting task: {task_summary}")
        task = (f'//span[text()="{task_summary}"]/ancestor::div[contains(@class, "card")]/div['
                f'@class="card-action"]/')
        self.wait_for_clickable(By.XPATH, task + 'a[@id="btn_delete_task"]').click()
        self.accept_alert()

    def cancel_delete_task(self, task_summary):
        """
        Cancel the deletion of a task with the given summary.

        Args:
            task_summary (str): The summary of the task whose deletion is to be canceled.
        """
        logger.info(f"Cancelling deletion of task: {task_summary}")
        task = (f'//span[text()="{task_summary}"]/ancestor::div[contains(@class, "card")]/div['
                f'@class="card-action"]/')
        self.wait_for_clickable(By.XPATH, task + 'a[@id="btn_delete_task"]').click()
        self.dismiss_alert()

    def remove_label(self, label):
        """
        Remove a label from a task.

        Args:
            label (str): The label to be removed.
        """
        logger.info(f"Removing label: {label}")
        element = self.wait_for_element(By.XPATH, f"//span[contains(text(), '{label}')]")
        element.find_element(By.XPATH, ".//img[contains(@class, 'icon_cancel')]").click()

    def remove_file(self, file):
        """
        Remove a file from a task.

        Args:
            file (str): The file to be removed.
        """
        logger.info(f"Removing file: {file}")
        file_name = file.split("\\")[-1]
        element = self.wait_for_element(By.XPATH, f"//span[contains(text(), '{file_name}')]")
        element.find_element(By.XPATH, ".//i[contains(text(), 'delete_forever')]").click()
