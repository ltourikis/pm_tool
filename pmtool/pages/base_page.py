from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time


class BasePage:
    custom_delay = 0.3

    def __init__(self, driver):
        """
        Initialize the base page with a WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_title(self, title):
        """
        Wait for the page title to contain the given title.
        """
        time.sleep(self.custom_delay)
        return self.wait.until(EC.title_contains(title))

    def wait_for_page_load(self, timeout=10):
        """
        Wait for the page to fully load.
        """
        time.sleep(self.custom_delay)
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
        except TimeoutException:
            print("Timed out waiting for page to load.")

    def wait_for_element_present(self, by, value):
        """
        Wait for an element to be present in the DOM.
        """
        time.sleep(self.custom_delay)
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def wait_for_element(self, by, value):
        """
        Wait for an element to be visible in the DOM.
        """
        time.sleep(self.custom_delay)
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def wait_for_clickable(self, by, value):
        """
        Wait for an element to be clickable.
        """
        time.sleep(self.custom_delay)
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def wait_for_element_in_page_source(self, message):
        """
        Wait for a specific message to be present in the page source.
        """
        time.sleep(self.custom_delay)
        return self.wait.until(lambda driver: message in driver.page_source)

    def accept_alert(self):
        """
        Accept an alert.
        """
        time.sleep(self.custom_delay)
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        """
        Dismiss an alert.
        """
        time.sleep(self.custom_delay)
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def select_from_dropdown(self, css_drop_down_menu, menu_option):
        """
        Select an option from a dropdown menu.
        """
        time.sleep(self.custom_delay)
        dropdown = self.wait_for_clickable(By.CSS_SELECTOR, css_drop_down_menu)
        dropdown.click()
        self.wait_for_clickable(By.XPATH, f"//li[span[text()='{menu_option}']]").click()

    def select_options_from_select_box(self, box_id, container_class_name, labels):
        """
        Select multiple options from a select box.
        """
        time.sleep(self.custom_delay)
        self.wait_for_clickable(By.ID, box_id).click()
        option_container = self.wait_for_element(By.CLASS_NAME, container_class_name)
        options = option_container.find_elements(By.CLASS_NAME, "option")

        for label in labels:
            for option in options:
                if option.text.strip().lower() == label.lower():
                    time.sleep(self.custom_delay)
                    option.click()
                    break

    def upload_file(self, file_input_id, file_path):
        """
        Upload a file using a file input element.
        """
        time.sleep(self.custom_delay)
        file_input = self.wait_for_element_present(By.ID, file_input_id)
        file_input.send_keys(os.path.abspath(file_path))
