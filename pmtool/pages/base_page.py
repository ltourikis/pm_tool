from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time


class BasePage:
    custom_delay = 0.3

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_title(self, title):
        time.sleep(self.custom_delay)
        return self.wait.until(EC.title_contains(title))

    def wait_for_page_load(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
        except TimeoutException:
            print("Timed out waiting for page to load.")

    def wait_for_element_present(self, by, value):
        time.sleep(self.custom_delay)
        return self.wait.until(EC.presence_of_element_located((by, value)))

    #  An element is considered visible if it is present in the DOM, has a height and width greater than zero,
    #  and is not hidden (e.g., via CSS properties like display: none or visibility: hidden).
    # This method is to be used as default when waiting for an element.
    def wait_for_element(self, by, value):
        time.sleep(self.custom_delay)
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def wait_for_clickable(self, by, value):
        time.sleep(self.custom_delay)
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def wait_for_element_in_page_source(self, message):
        time.sleep(self.custom_delay)
        return self.wait.until(lambda driver: message in driver.page_source)

    def accept_alert(self):
        time.sleep(self.custom_delay)
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        time.sleep(self.custom_delay)
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def select_from_dropdown(self, css_drop_down_menu, menu_option):
        # Click on the dropdown to open it
        time.sleep(self.custom_delay)
        dropdown = self.wait_for_clickable(By.CSS_SELECTOR, css_drop_down_menu)
        dropdown.click()
        self.wait_for_clickable(By.XPATH, f"//li[span[text()='{menu_option}']]").click()

    def select_options_from_select_box(self, box_id, container_class_name, labels):
        time.sleep(self.custom_delay)
        self.wait_for_clickable(By.ID, box_id).click()

        # Wait until the options container is visible
        option_container = self.wait_for_element(By.CLASS_NAME, container_class_name)

        options = option_container.find_elements(By.CLASS_NAME, "option")

        for label in labels:
            for option in options:
                if option.text.strip().lower() == label.lower():
                    time.sleep(self.custom_delay)
                    option.click()
                    break

    def upload_file(self, file_input_id, file_path):
        # Wait until the file input element is present and visible
        time.sleep(self.custom_delay)
        file_input = self.wait_for_element_present(By.ID, file_input_id)

        # Send the file path to the file input element
        file_input.send_keys(os.path.abspath(file_path))
