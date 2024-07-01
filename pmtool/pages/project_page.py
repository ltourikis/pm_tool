from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProjectPage(BasePage):
    def add_project(self, project_name, description):
        self.wait_for_clickable(By.CSS_SELECTOR, 'a[href="/createProject"]').click()
        self.wait_for_element(By.ID, "name").send_keys(project_name)
        self.wait_for_element(By.ID, "description").send_keys(description)
        self.wait_for_clickable(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def edit_project(self, old_project_name, new_project_name="", new_description=""):
        project = (f'//span[text()="{old_project_name}"]/ancestor::div[contains(@class, "card")]/div['
                   f'@class="card-action"]/')
        self.wait_for_clickable(By.XPATH, project + 'a[@id="btn_update_project"]').click()
        if new_project_name:
            self.wait_for_clickable(By.ID, "name").clear()
            self.wait_for_clickable(By.ID, "name").send_keys(new_project_name)
        if new_description:
            self.wait_for_clickable(By.ID, "description").clear()
            self.wait_for_clickable(By.ID, "description").send_keys(new_description)
        self.wait_for_clickable(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def delete_project(self, project_name):
        project = (f'//span[text()="{project_name}"]/ancestor::div[contains(@class, "card")]/div['
                   f'@class="card-action"]/')
        self.wait_for_clickable(By.XPATH, project + 'a[@id="delete_project"]').click()
        self.accept_alert()

    def cancel_delete_project(self, project_name):
        project = (f'//span[text()="{project_name}"]/ancestor::div[contains(@class, "card")]/div['
                   f'@class="card-action"]/')
        self.wait_for_clickable(By.XPATH, project + 'a[@id="delete_project"]').click()
        self.dismiss_alert()

    def add_task(self, project_name):
        project = (f'//span[text()="{project_name}"]/ancestor::div[contains(@class, "card")]/div['
                   f'@class="card-action"]/')
        self.wait_for_clickable(By.XPATH, project + 'a[@id="btn_add_task"]').click()

    def view_task(self, project_name):
        project = (f'//span[text()="{project_name}"]/ancestor::div[contains(@class, "card")]/div['
                   f'@class="card-action"]/')
        self.wait_for_clickable(By.XPATH, project + 'a[@id="btn_view_tasks"]').click()
