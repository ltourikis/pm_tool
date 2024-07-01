from selenium.webdriver.common.by import By
from .base_page import BasePage


class TaskPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.custom_delay = 0.5

    labels = ["frontend", "backend", "design", "testing", "performance", "techdept", "ci", "jenkins"]
    status = ["TO DO", "IN PROGRESS", "DONE", "IN REVIEW"]

    file1_path = r"C:\Users\loukas\Scripts\pmtool_tests\pmtool\files_for_upload\file1.txt"
    file2_path = r"C:\Users\loukas\Scripts\pmtool_tests\pmtool\files_for_upload\file2.txt"
    file3_path = r"C:\Users\loukas\Scripts\pmtool_tests\pmtool\files_for_upload\file3.txt"

    def create_task(self, task_summary, task_description, status="", labels="", files=""):
        self.wait_for_element(By.ID, "summary").send_keys(task_summary)
        self.wait_for_element(By.ID, "description").send_keys(task_description)
        if status:
            self.select_from_dropdown(".select-dropdown.dropdown-trigger", status)
        if labels:
            self.select_options_from_select_box("search_input", "optionContainer", labels)
            self.wait_for_element(By.ID, "summary").click()
        if files:
            for file in files:
                self.upload_file("attachments", file)

        self.wait_for_clickable(By.XPATH, "//button[contains(text(), 'Create')]").click()

    def click_edit_task(self, task_summary):
        task = (f'//span[text()="{task_summary}"]/ancestor::div[contains(@class, "card")]/div['
                f'@class="card-action"]/')
        self.wait_for_clickable(By.XPATH, task + 'a[@id="btn_update_task"]').click()
        self.wait_for_page_load()

    def edit_task(self, task_summary="", task_description="", status="", add_labels="", remove_labels="",
                  add_files="", remove_files=""):
        if task_summary:
            self.wait_for_clickable(By.ID, "summary").clear()
            self.wait_for_element(By.ID, "summary").send_keys(task_summary)
        if task_description:
            self.wait_for_element(By.ID, "description").clear()
            self.wait_for_element(By.ID, "description").send_keys(task_description)
        if status:
            self.select_from_dropdown(".select-dropdown.dropdown-trigger", status)
        if add_labels:
            self.select_options_from_select_box("search_input", "optionContainer", add_labels)
            self.wait_for_element(By.ID, "summary").click()
        if remove_labels:
            for label in remove_labels:
                self.remove_label(label)
                self.wait_for_clickable(By.ID, "summary").click()
        if add_files:
            for file in add_files:
                self.upload_file("attachments", file)
                self.wait_for_clickable(By.ID, "summary").click()
        if remove_files:
            for file in remove_files:
                self.remove_file(file)
                self.wait_for_clickable(By.ID, "summary").click()
        self.wait_for_clickable(By.XPATH, "//button[contains(text(), 'Update')]").click()

    def edit_summary_blank(self):
        self.wait_for_clickable(By.ID, "summary").clear()
        self.wait_for_element(By.ID, "description").click()
        # time.sleep(5)
        self.wait_for_clickable(By.XPATH, "//button[contains(text(), 'Update')]").click()

    def edit_description_blank(self):
        self.wait_for_clickable(By.ID, "description").clear()
        self.wait_for_element(By.ID, "summary").click()
        # time.sleep(5)
        self.wait_for_clickable(By.XPATH, "//button[contains(text(), 'Update')]").click()

    def check_if_task_present(self, task_summary, task_description, status_column, labels="", files=""):
        column = self.wait_for_element(By.ID, f"{status_column.lower().replace(" ", "_")}_items")
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
        task = (f'//span[text()="{task_summary}"]/ancestor::div[contains(@class, "card")]/div['
                f'@class="card-action"]/')
        self.wait_for_clickable(By.XPATH, task + 'a[@id="btn_delete_task"]').click()
        self.accept_alert()

    def cancel_delete_task(self, task_summary):
        task = (f'//span[text()="{task_summary}"]/ancestor::div[contains(@class, "card")]/div['
                f'@class="card-action"]/')
        self.wait_for_clickable(By.XPATH, task + 'a[@id="btn_delete_task"]').click()
        self.dismiss_alert()

    def remove_label(self, label):
        element = self.wait_for_element(By.XPATH, f"//span[contains(text(), '{label}')]")
        element.find_element(By.XPATH, ".//img[contains(@class, 'icon_cancel')]").click()

    def remove_file(self, file):
        file_name = file.split("\\")[-1]
        element = self.wait_for_element(By.XPATH, f"//span[contains(text(), '{file_name}')]")
        element.find_element(By.XPATH, ".//i[contains(text(), 'delete_forever')]").click()
