from pmtool.pages.login_page import LoginPage
from pmtool.pages.settings_page import SettingsPage
from pmtool.pages.navigation_bar import NavigationBar


def test_change_name_setting_successful(settings_setup):
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(name="George R.R. Martin", password="4321")

    login_page = LoginPage(settings_setup)
    login_page.wait_for_element_in_page_source("User info updated successfully!")
    assert "User info updated successfully!" in settings_setup.page_source

    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_logout_button()

    login_page = LoginPage(settings_setup)
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="4321")

    settings_page = SettingsPage(settings_setup)
    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_settings_button()
    settings_page.wait_for_element_in_page_source("George R.R. Martin")
    settings = settings_page.get_settings()
    assert settings['name'] == "George R.R. Martin"


def test_change_email_setting_successful(settings_setup, change_email_teardown):
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(email="loukas2@gmail.com", password="4321")

    login_page = LoginPage(settings_setup)
    login_page.wait_for_element_in_page_source("User info updated successfully!")
    assert "User info updated successfully!" in settings_setup.page_source

    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_logout_button()

    login_page = LoginPage(settings_setup)
    login_page.select_login_button()
    login_page.login(email="loukas2@gmail.com", password="4321")

    settings_page = SettingsPage(settings_setup)
    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_settings_button()
    settings_page.wait_for_element_in_page_source("loukas2@gmail.com")
    settings = settings_page.get_settings()
    assert settings['email'] == "loukas2@gmail.com"


def test_change_password_setting_successful(settings_setup, change_password_teardown):
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(email="loukastourikis3@gmail.com", password="new_pass")

    login_page = LoginPage(settings_setup)
    login_page.wait_for_element_in_page_source("User info updated successfully!")
    assert "User info updated successfully!" in settings_setup.page_source

    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_logout_button()

    login_page = LoginPage(settings_setup)
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="new_pass")
    login_page.wait_for_element_in_page_source("TaskDB")
    assert "TaskDB" in settings_setup.page_source


def test_change_company_and_address_setting_successful(settings_setup, change_password_teardown):
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(company="Workable", address="khfisias")

    login_page = LoginPage(settings_setup)
    login_page.wait_for_element_in_page_source("User info updated successfully!")
    assert "User info updated successfully!" in settings_setup.page_source

    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_logout_button()

    login_page = LoginPage(settings_setup)
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="4321")

    settings_page = SettingsPage(settings_setup)
    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_settings_button()
    settings = settings_page.get_settings()
    assert settings['company'] == "Workable"
    assert settings['address'] == "khfisias"


def test_enable_2fa_setting_successful(settings_setup, change_2fa_teardown):
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(checkbox="click")

    login_page = LoginPage(settings_setup)
    login_page.wait_for_element_in_page_source("User info updated successfully!")
    assert "User info updated successfully!" in settings_setup.page_source

    settings_page = SettingsPage(settings_setup)
    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_settings_button()
    settings = settings_page.get_settings()
    assert settings['2fa']
