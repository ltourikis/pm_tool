import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pmtool.pages.project_page import ProjectPage
from pmtool.pages.login_page import LoginPage
from pmtool.pages.settings_page import SettingsPage
from pmtool.pages.navigation_bar import NavigationBar


@pytest.fixture(scope="module")
def general_setup_teardown():
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
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
    driver.get("https://pm-tool-e63fa77e3353.herokuapp.com")
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def task_setup():
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
    yield task_setup
    navigation_bar = NavigationBar(task_setup)
    navigation_bar.select_dashboard_button()


@pytest.fixture(scope="function")
def settings_setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
    driver.get("https://pm-tool-e63fa77e3353.herokuapp.com")
    login_page = LoginPage(driver)
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="4321")
    settings_page = SettingsPage(driver)
    navigation_bar = NavigationBar(driver)
    navigation_bar.select_settings_button()
    # settings_page.wait_for_element_in_page_source("Enable 2FA")
    # assert "Enable 2FA" in driver.page_source

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def change_email_teardown(settings_setup):
    yield settings_setup
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(email="loukastourikis3@gmail.com", password="4321")


@pytest.fixture(scope="function")
def change_password_teardown(settings_setup):
    yield settings_setup
    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_settings_button()
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(email="loukastourikis3@gmail.com", password="4321")


@pytest.fixture(scope="function")
def change_2fa_teardown(settings_setup):
    yield settings_setup
    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_settings_button()
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(checkbox="uncheck")
