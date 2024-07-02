import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pmtool.pages.project_page import ProjectPage
from pmtool.pages.login_page import LoginPage
from pmtool.pages.settings_page import SettingsPage
from pmtool.pages.task_page import TaskPage
from pmtool.pages.navigation_bar import NavigationBar


@pytest.fixture(scope="module")
def general_setup_teardown():
    """
    General fixture for setting up and tearing down the WebDriver session.
    Runs before the first test and after the last.

    This fixture:
    - Initializes a WebDriver instance using ChromeDriver with the WebDriver Manager.
    - Maximizes the browser window.
    - Logs into the PM Tool application.
    - Yields the WebDriver instance to the tests.
    - Quits the WebDriver session after the tests are completed.
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
    driver.get("https://pm-tool-e63fa77e3353.herokuapp.com")
    login_page = LoginPage(driver)
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="4321")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def user_setup_teardown():
    """
    Fixture for setting up and tearing down the WebDriver session for user-level tests.
    Runs before-after every test.

    This fixture:
    - Initializes a WebDriver instance using ChromeDriver with the WebDriver Manager.
    - Maximizes the browser window.
    - Opens the PM Tool application.
    - Yields the WebDriver instance to the tests.
    - Quits the WebDriver session after the tests are completed.
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
    driver.get("https://pm-tool-e63fa77e3353.herokuapp.com")
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def task_setup():
    """
    Fixture for setting up and tearing down the WebDriver session specifically for task-related module tests.
    Runs before the first test and after the last.

    This fixture:
    - Initializes a WebDriver instance using ChromeDriver with the WebDriver Manager.
    - Maximizes the browser window.
    - Logs into the PM Tool application.
    - Creates a project for task management.
    - Yields the WebDriver instance to the tests.
    - Quits the WebDriver session after the tests are completed.
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
    driver.get("https://pm-tool-e63fa77e3353.herokuapp.com")
    login_page = LoginPage(driver)
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="4321")

    project_page = ProjectPage(driver)
    project_page.add_project("ForTaskManagement", "For Task Management")
    project_page.wait_for_element_in_page_source("ForTaskManagement")
    assert "ForTaskManagement" in driver.page_source

    yield driver
    # project_page.delete_project("ForTaskManagement")
    driver.quit()


@pytest.fixture(scope="function")
def task_teardown(task_setup):
    """
    Fixture for cleaning up after task-related tests.

    This fixture:
    - Yields the WebDriver instance to the tests.
    - After tests complete, navigates back to the dashboard using the navigation bar.
    """
    yield task_setup
    navigation_bar = NavigationBar(task_setup)
    navigation_bar.select_dashboard_button()


@pytest.fixture(scope="function")
def settings_setup():
    """
    Fixture for setting up and tearing down the WebDriver session specifically for User settings related tests.

    This fixture:
    - Initializes a WebDriver instance using ChromeDriver with the WebDriver Manager.
    - Maximizes the browser window.
    - Logs into the PM Tool application.
    - Navigates to the settings page.
    - Yields the WebDriver instance to the tests.
    - Quits the WebDriver session after the tests are completed.
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
    driver.get("https://pm-tool-e63fa77e3353.herokuapp.com")
    login_page = LoginPage(driver)
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="4321")

    navigation_bar = NavigationBar(driver)
    navigation_bar.select_settings_button()

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def change_email_teardown(settings_setup):
    """
    Fixture for cleaning up after changing email settings.

    This fixture:
    - Yields the WebDriver instance to the tests.
    - After tests complete, changes the email setting back to the original.
    """
    yield settings_setup
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(email="loukastourikis3@gmail.com", password="4321")


@pytest.fixture(scope="function")
def change_password_teardown(settings_setup):
    """
    Fixture for cleaning up after changing password settings.

    This fixture:
    - Yields the WebDriver instance to the tests.
    - After tests complete, navigates to the settings page and changes the password setting back to the original.
    """
    yield settings_setup
    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_settings_button()
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(email="loukastourikis3@gmail.com", password="4321")


@pytest.fixture(scope="function")
def change_2fa_teardown(settings_setup):
    """
    Fixture for cleaning up after enabling/disabling 2FA settings.

    This fixture:
    - Yields the WebDriver instance to the tests.
    - After tests complete, navigates to the settings page and changes the 2FA setting back to the original state.
    """
    yield settings_setup
    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_settings_button()
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(checkbox="uncheck")


@pytest.fixture(scope="module")
def taskdb_setup_teardown():
    """
    Fixture for setting up and tearing down the WebDriver session specifically for TaskDB-related tests.


    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
    driver.get("https://pm-tool-e63fa77e3353.herokuapp.com")
    login_page = LoginPage(driver)
    navigation_bar = NavigationBar(driver)
    project_page = ProjectPage(driver)
    task_page = TaskPage(driver)

    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="4321")

    project_page.add_project("ForTaskDBTests1", "For Testing Purposes 1")
    project_page.wait_for_element_in_page_source("ForTaskDBTests1")  # Create a project
    assert "ForTaskDBTests1" in driver.page_source
    project_page.add_project("ForTaskDBTests2", "For Testing Purposes 2")
    project_page.wait_for_element_in_page_source("ForTaskDBTests2")  # Create a second project
    assert "ForTaskDBTests2" in driver.page_source

    # Create a few tasks
    for task in ["A_Task", "Z_Task"]:
        project_page.add_task("ForTaskDBTests1")
        task_page.create_task(task, f"{task} Description")  # Add a task
        navigation_bar.select_dashboard_button()
    for task in ["B_Task", "$_Task"]:
        project_page.add_task("ForTaskDBTests2")
        task_page.create_task(task, f"{task} Description")  # Add a task
        navigation_bar.select_dashboard_button()

    yield driver
    # project_page.delete_project("ForTaskManagement")
    driver.quit()
