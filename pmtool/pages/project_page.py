from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProjectPage(BasePage):
    """
    Page Object Model for the Project Page.

    Inherits from:
        BasePage: A base class that includes common methods for all pages.
    """

    def add_project(self, project_name, description):
        """
        Add a new project with the given name and description.

        Args:
            project_name (str): The name of the project to add.
            description (str): The description of the project.
        """
        # Click on the 'Create' button
        self.wait_for_clickable(By.CSS_SELECTOR, 'a[href="/createProject"]').click()

        # Enter the project name and description
        self.wait_for_element(By.ID, "name").send_keys(project_name)
        self.wait_for_element(By.ID, "description").send_keys(description)

        # Submit the form
        self.wait_for_clickable(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def edit_project(self, old_project_name, new_project_name="", new_description=""):
        """
        Edit an existing project identified by old_project_name. Update with new_project_name and/or new_description.

        Args:
            old_project_name (str): The name of the project to edit.
            new_project_name (str): The new name for the project (optional).
            new_description (str): The new description for the project (optional).
        """
        project = (f'//span[text()="{old_project_name}"]/ancestor::div[contains(@class, "card")]/div['
                   f'@class="card-action"]/')

        # Click on the 'Edit Project' button
        self.wait_for_clickable(By.XPATH, project + 'a[@id="btn_update_project"]').click()

        # Update the project name if provided
        if new_project_name:
            self.wait_for_clickable(By.ID, "name").clear()
            self.wait_for_clickable(By.ID, "name").send_keys(new_project_name)

        # Update the project description if provided
        if new_description:
            self.wait_for_clickable(By.ID, "description").clear()
            self.wait_for_clickable(By.ID, "description").send_keys(new_description)

        # Submit the form
        self.wait_for_clickable(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def delete_project(self, project_name):
        """
        Delete a project by name.

        Args:
            project_name (str): The name of the project to delete.
        """
        project = (f'//span[text()="{project_name}"]/ancestor::div[contains(@class, "card")]/div['
                   f'@class="card-action"]/')

        # Click on the 'Delete Project' button
        self.wait_for_clickable(By.XPATH, project + 'a[@id="delete_project"]').click()

        # Accept the confirmation alert
        self.accept_alert()

    def cancel_delete_project(self, project_name):
        """
        Cancel the deletion of a project by name.

        Args:
            project_name (str): The name of the project to cancel deletion.
        """
        project = (f'//span[text()="{project_name}"]/ancestor::div[contains(@class, "card")]/div['
                   f'@class="card-action"]/')

        # Click on the 'Delete Project' button
        self.wait_for_clickable(By.XPATH, project + 'a[@id="delete_project"]').click()

        # Dismiss the confirmation alert
        self.dismiss_alert()

    def add_task(self, project_name):
        """
        Clicks the Add Task button to the relevant project.

        Args:
            project_name (str): The name of the project to add a task to.
        """
        project = (f'//span[text()="{project_name}"]/ancestor::div[contains(@class, "card")]/div['
                   f'@class="card-action"]/')

        # Click on the 'Add Task' button
        self.wait_for_clickable(By.XPATH, project + 'a[@id="btn_add_task"]').click()

    def view_task(self, project_name):
        """
        View tasks of a project by name.

        Args:
            project_name (str): The name of the project to view tasks.
        """
        project = (f'//span[text()="{project_name}"]/ancestor::div[contains(@class, "card")]/div['
                   f'@class="card-action"]/')

        # Click on the 'View Tasks' button
        self.wait_for_clickable(By.XPATH, project + 'a[@id="btn_view_tasks"]').click()
