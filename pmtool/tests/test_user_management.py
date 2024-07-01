from pmtool.pages.signup_page import SignupPage
from pmtool.pages.login_page import LoginPage
from pmtool.pages.settings_page import SettingsPage
from pmtool.pages.navigation_bar import NavigationBar
from pmtool.utils.utils import (generate_random_name, generate_random_email, generate_random_password,
                                generate_random_address, generate_random_company_name)


def test_signup_new_user_success_no_optional_fields(user_setup_teardown):
    signup_page = SignupPage(user_setup_teardown)
    signup_page.select_signup_button()
    name = generate_random_name()
    email = generate_random_email()
    password = generate_random_password()
    signup_page.signup(name=name, email=email, password=password)
    signup_page.wait_for_element_in_page_source("Successfull registration, check your email in order to verify your "
                                                "account")
    # Assert successful account creation without optional fields filled
    assert "Successfull registration, check your email in order to verify your account" in user_setup_teardown.page_source


def test_signup_new_user_success_with_optional_fields(user_setup_teardown):
    signup_page = SignupPage(user_setup_teardown)
    signup_page.select_signup_button()
    name = generate_random_name()
    email = generate_random_email()
    password = generate_random_password()
    company = generate_random_company_name()
    address = generate_random_address()
    signup_page.signup(name=name, email=email, password=password, company=company, address=address)
    signup_page.wait_for_element_in_page_source("Successfull registration, check your email in order to verify your "
                                                "account")
    # Assert successful account creation with optional fields filled
    assert "Successfull registration, check your email in order to verify your account" in user_setup_teardown.page_source


def test_signup_new_user_error_missing_email(user_setup_teardown):
    signup_page = SignupPage(user_setup_teardown)
    signup_page.select_signup_button()
    name = generate_random_name()
    password = generate_random_password()
    signup_page.signup(name=name, email="", password=password)
    signup_page.wait_for_element_in_page_source("This field is required")
    # Assert error message
    assert "This field is required" in user_setup_teardown.page_source


def test_signup_new_user_error_missing_password(user_setup_teardown):
    signup_page = SignupPage(user_setup_teardown)
    signup_page.select_signup_button()
    name = generate_random_name()
    email = generate_random_email()
    signup_page.signup(name=name, email=email, password="")
    signup_page.wait_for_element_in_page_source("This field is required")
    # Assert error message
    assert "This field is required" in user_setup_teardown.page_source


def test_signup_new_user_error_missing_name(user_setup_teardown):
    signup_page = SignupPage(user_setup_teardown)
    signup_page.select_signup_button()
    email = generate_random_email()
    password = generate_random_password()
    signup_page.signup(name="", email=email, password=password)
    signup_page.wait_for_element_in_page_source("This field is required")
    # Assert error message
    assert "This field is required" in user_setup_teardown.page_source


def test_login_user_success(user_setup_teardown):
    login_page = LoginPage(user_setup_teardown)
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="4321")
    # Assert login successful
    login_page.wait_for_element_in_page_source("TaskDB")
    assert "TaskDB" in user_setup_teardown.page_source


def test_login_user_failure_invalid_credentials(user_setup_teardown):
    login_page = LoginPage(user_setup_teardown)
    login_page.select_login_button()
    login_page.login(email="invaliduser@example.com", password="WrongPassword")
    # Assert error message
    login_page.wait_for_element_in_page_source("Invalid login info")
    assert "Invalid login info" in user_setup_teardown.page_source


def test_login_user_failure_no_email(user_setup_teardown):
    login_page = LoginPage(user_setup_teardown)
    login_page.select_login_button()
    login_page.login(email="", password="4321")
    # Assert error message
    login_page.wait_for_element_in_page_source("Invalid login info")
    assert "Invalid login info" in user_setup_teardown.page_source


def test_login_user_failure_no_password(user_setup_teardown):
    login_page = LoginPage(user_setup_teardown)
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="")
    # Assert error message
    login_page.wait_for_element_in_page_source("Invalid login info")
    assert "Invalid login info" in user_setup_teardown.page_source


def test_login_user_success_after_password_change(user_setup_teardown):
    login_page = LoginPage(user_setup_teardown)
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="4321")
    # change the password to `1234` and try to log in with the password
    settings_page = SettingsPage(user_setup_teardown)
    navigation_bar = NavigationBar(user_setup_teardown)
    navigation_bar.select_settings_button()
    settings_page.change_settings(name="Loukas Tourikis", email="loukastourikis3@gmail.com", password="1234")
    login_page.wait_for_element_in_page_source("User info updated successfully!")
    assert "User info updated successfully!" in user_setup_teardown.page_source
    navigation_bar.select_logout_button()
    user_setup_teardown.refresh()

    login_page = LoginPage(user_setup_teardown)
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="1234")
    login_page.wait_for_element_in_page_source("TaskDB")
    assert "TaskDB" in user_setup_teardown.page_source

    # restore to initial password `4321`
    settings_page = SettingsPage(user_setup_teardown)
    navigation_bar = NavigationBar(user_setup_teardown)
    navigation_bar.select_settings_button()
    settings_page.change_settings(name="Loukas Tourikis", email="loukastourikis3@gmail.com", password="4321")

