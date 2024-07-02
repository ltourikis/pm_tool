from pmtool.pages.signup_page import SignupPage
from pmtool.pages.login_page import LoginPage
from pmtool.pages.settings_page import SettingsPage
from pmtool.pages.navigation_bar import NavigationBar
from pmtool.utils.utils import (generate_random_name, generate_random_email, generate_random_password,
                                generate_random_address, generate_random_company_name)


def test_signup_new_user_no_optional_fields_successful(user_setup_teardown):
    """
    Test successful signup without optional fields.

    Args:
        user_setup_teardown: Fixture for setting up and tearing down the user environment.
    """
    signup_page = SignupPage(user_setup_teardown)
    signup_page.select_signup_button()  # Click on the signup button
    name = generate_random_name()  # Generate a random name
    email = generate_random_email()  # Generate a random email
    password = generate_random_password()  # Generate a random password
    signup_page.signup(name=name, email=email, password=password)  # Perform signup with required fields
    signup_page.wait_for_element_in_page_source("Successfull registration, check your email in order to verify your "
                                                "account")  # Wait for success message
    assert ("Successfull registration, check your email in order to verify your account"
            in user_setup_teardown.page_source)  # Assert successful signup message


def test_signup_new_user_with_optional_fields_successful(user_setup_teardown):
    """
    Test successful signup with optional fields filled.

    Args:
        user_setup_teardown: Fixture for setting up and tearing down the user environment.
    """
    signup_page = SignupPage(user_setup_teardown)
    signup_page.select_signup_button()  # Click on the signup button
    name = generate_random_name()  # Generate a random name
    email = generate_random_email()  # Generate a random email
    password = generate_random_password()  # Generate a random password
    company = generate_random_company_name()  # Generate a random company name
    address = generate_random_address()  # Generate a random address
    signup_page.signup(name=name, email=email, password=password, company=company,
                       address=address)  # Signup with optional fields
    signup_page.wait_for_element_in_page_source("Successfull registration, check your email in order to verify your "
                                                "account")  # Wait for success message
    assert ("Successfull registration, check your email in order to verify your account"
            in user_setup_teardown.page_source)  # Assert successful signup message


def test_signup_new_user_missing_email_failure(user_setup_teardown):
    """
    Test signup with missing email field and expect an error.

    Args:
        user_setup_teardown: Fixture for setting up and tearing down the user environment.
    """
    signup_page = SignupPage(user_setup_teardown)
    signup_page.select_signup_button()  # Click on the signup button
    name = generate_random_name()  # Generate a random name
    password = generate_random_password()  # Generate a random password
    signup_page.signup(name=name, email="", password=password)  # Signup with missing email field
    signup_page.wait_for_element_in_page_source("This field is required")  # Wait for error message
    assert "This field is required" in user_setup_teardown.page_source  # Assert error message


def test_signup_new_user_missing_password_failure(user_setup_teardown):
    """
    Test signup with missing password field and expect an error.

    Args:
        user_setup_teardown: Fixture for setting up and tearing down the user environment.
    """
    signup_page = SignupPage(user_setup_teardown)
    signup_page.select_signup_button()  # Click on the signup button
    name = generate_random_name()  # Generate a random name
    email = generate_random_email()  # Generate a random email
    signup_page.signup(name=name, email=email, password="")  # Signup with missing password field
    signup_page.wait_for_element_in_page_source("This field is required")  # Wait for error message
    assert "This field is required" in user_setup_teardown.page_source  # Assert error message


def test_signup_new_user_missing_name_failure(user_setup_teardown):
    """
    Test signup with missing name field and expect an error.

    Args:
        user_setup_teardown: Fixture for setting up and tearing down the user environment.
    """
    signup_page = SignupPage(user_setup_teardown)
    signup_page.select_signup_button()  # Click on the signup button
    email = generate_random_email()  # Generate a random email
    password = generate_random_password()  # Generate a random password
    signup_page.signup(name="", email=email, password=password)  # Signup with missing name field
    signup_page.wait_for_element_in_page_source("This field is required")  # Wait for error message
    assert "This field is required" in user_setup_teardown.page_source  # Assert error message


def test_login_user_successful(user_setup_teardown):
    """
    Test login with correct credentials.

    Args:
        user_setup_teardown: Fixture for setting up and tearing down the user environment.
    """
    login_page = LoginPage(user_setup_teardown)
    login_page.select_login_button()  # Click on the login button
    login_page.login(email="loukastourikis3@gmail.com", password="4321")  # Perform login with correct credentials
    login_page.wait_for_element_in_page_source("TaskDB")  # Wait for dashboard page
    assert "TaskDB" in user_setup_teardown.page_source  # Assert successful login


def test_login_user_invalid_credentials_failure(user_setup_teardown):
    """
    Test login with invalid credentials and expect an error.

    Args:
        user_setup_teardown: Fixture for setting up and tearing down the user environment.
    """
    login_page = LoginPage(user_setup_teardown)
    login_page.select_login_button()  # Click on the login button
    login_page.login(email="invaliduser@example.com",
                     password="WrongPassword")  # Perform login with invalid credentials
    login_page.wait_for_element_in_page_source("Invalid login info")  # Wait for error message
    assert "Invalid login info" in user_setup_teardown.page_source  # Assert error message


def test_login_user_no_email_failure(user_setup_teardown):
    """
    Test login with no email provided and expect an error.

    Args:
        user_setup_teardown: Fixture for setting up and tearing down the user environment.
    """
    login_page = LoginPage(user_setup_teardown)
    login_page.select_login_button()  # Click on the login button
    login_page.login(email="", password="4321")  # Perform login with no email
    login_page.wait_for_element_in_page_source("Invalid login info")  # Wait for error message
    assert "Invalid login info" in user_setup_teardown.page_source  # Assert error message


def test_login_user_no_password_failure(user_setup_teardown):
    """
    Test login with no password provided and expect an error.

    Args:
        user_setup_teardown: Fixture for setting up and tearing down the user environment.
    """
    login_page = LoginPage(user_setup_teardown)
    login_page.select_login_button()  # Click on the login button
    login_page.login(email="loukastourikis3@gmail.com", password="")  # Perform login with no password
    login_page.wait_for_element_in_page_source("Invalid login info")  # Wait for error message
    assert "Invalid login info" in user_setup_teardown.page_source  # Assert error message


def test_login_user_after_password_change_successful(user_setup_teardown):
    """
    Test login after changing password successfully.

    Args:
        user_setup_teardown: Fixture for setting up and tearing down the user environment.
    """
    login_page = LoginPage(user_setup_teardown)
    login_page.select_login_button()  # Click on the login button
    login_page.login(email="loukastourikis3@gmail.com", password="4321")  # Perform login with initial password

    # Navigate to settings and change password to '1234'
    settings_page = SettingsPage(user_setup_teardown)
    navigation_bar = NavigationBar(user_setup_teardown)
    navigation_bar.select_settings_button()
    settings_page.change_settings(name="Loukas Tourikis", email="loukastourikis3@gmail.com", password="1234")
    login_page.wait_for_element_in_page_source("User info updated successfully!")  # Wait for success message
    assert "User info updated successfully!" in user_setup_teardown.page_source  # Assert success message

    # Logout and login again with new password '1234'
    navigation_bar.select_logout_button()
    user_setup_teardown.refresh()  # Refresh the page

    login_page = LoginPage(user_setup_teardown)
    login_page.select_login_button()  # Click on the login button
    login_page.login(email="loukastourikis3@gmail.com", password="1234")  # Login with new password

    # Restore password to initial '4321'
    settings_page = SettingsPage(user_setup_teardown)
    navigation_bar = NavigationBar(user_setup_teardown)
    navigation_bar.select_settings_button()
    settings_page.change_settings(name="Loukas Tourikis", email="loukastourikis3@gmail.com", password="4321")
