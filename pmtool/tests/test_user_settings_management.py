import logging
from pmtool.pages.login_page import LoginPage
from pmtool.pages.settings_page import SettingsPage
from pmtool.pages.navigation_bar import NavigationBar

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_change_name_setting_successful(settings_setup):
    """
    Test changing name setting successfully.

    Args:
        settings_setup: Fixture for setting up and tearing down the settings environment.
    """
    logger.info("Starting test_change_name_setting_successful...")
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(name="George R.R. Martin", password="4321")

    # Verify success message after settings change
    login_page = LoginPage(settings_setup)
    login_page.wait_for_element_in_page_source("User info updated successfully!")
    assert "User info updated successfully!" in settings_setup.page_source

    # Logout and login again to verify the changed name
    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_logout_button()
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="4321")

    # Verify the name change in settings
    settings_page = SettingsPage(settings_setup)
    navigation_bar.select_settings_button()
    settings_page.wait_for_element_in_page_source("George R.R. Martin")
    settings = settings_page.get_settings()
    assert settings['name'] == "George R.R. Martin"
    logger.info("test_change_name_setting_successful completed successfully.\n")


def test_change_email_setting_successful(settings_setup, change_email_teardown):
    """
    Test changing email setting successfully.

    Args:
        settings_setup: Fixture for setting up and tearing down the settings environment.
        change_email_teardown: Fixture to clean up after changing email.
    """
    logger.info("Starting test_change_email_setting_successful...")
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(email="loukas2@gmail.com", password="4321")

    # Verify success message after settings change
    login_page = LoginPage(settings_setup)
    login_page.wait_for_element_in_page_source("User info updated successfully!")
    assert "User info updated successfully!" in settings_setup.page_source

    # Logout and login again to verify the changed email
    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_logout_button()
    login_page.select_login_button()
    login_page.login(email="loukas2@gmail.com", password="4321")

    # Verify the email change in settings
    settings_page = SettingsPage(settings_setup)
    navigation_bar.select_settings_button()
    settings_page.wait_for_element_in_page_source("loukas2@gmail.com")
    settings = settings_page.get_settings()
    assert settings['email'] == "loukas2@gmail.com"
    logger.info("test_change_email_setting_successful completed successfully.\n")


def test_change_password_setting_successful(settings_setup, change_password_teardown):
    """
    Test changing password setting successfully.

    Args:
        settings_setup: Fixture for setting up and tearing down the settings environment.
        change_password_teardown: Fixture to clean up after changing password.
    """
    logger.info("Starting test_change_password_setting_successful...")
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(email="loukastourikis3@gmail.com", password="new_pass")

    # Verify success message after settings change
    login_page = LoginPage(settings_setup)
    login_page.wait_for_element_in_page_source("User info updated successfully!")
    assert "User info updated successfully!" in settings_setup.page_source

    # Logout and login again to verify the changed password
    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_logout_button()
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="new_pass")
    login_page.wait_for_element_in_page_source("TaskDB")
    assert "TaskDB" in settings_setup.page_source
    logger.info("test_change_password_setting_successful completed successfully.\n")


def test_change_company_and_address_setting_successful(settings_setup, change_password_teardown):
    """
    Test changing company and address settings successfully.

    Args:
        settings_setup: Fixture for setting up and tearing down the settings environment.
        change_password_teardown: Fixture to clean up after changing password.
    """
    logger.info("Starting test_change_company_and_address_setting_successful...")
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(company="Workable", address="khfisias")

    # Verify success message after settings change
    login_page = LoginPage(settings_setup)
    login_page.wait_for_element_in_page_source("User info updated successfully!")
    assert "User info updated successfully!" in settings_setup.page_source

    # Logout and login again to verify the changed company and address
    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_logout_button()
    login_page.select_login_button()
    login_page.login(email="loukastourikis3@gmail.com", password="4321")

    # Verify the company and address change in settings
    settings_page = SettingsPage(settings_setup)
    navigation_bar.select_settings_button()
    settings = settings_page.get_settings()
    assert settings['company'] == "Workable"
    assert settings['address'] == "khfisias"
    logger.info("test_change_company_and_address_setting_successful completed successfully.\n")


def test_enable_2fa_setting_successful(settings_setup, change_2fa_teardown):
    """
    Test enabling 2FA setting successfully.

    Args:
        settings_setup: Fixture for setting up and tearing down the settings environment.
        change_2fa_teardown: Fixture to clean up after enabling 2FA.
    """
    logger.info("Starting test_enable_2fa_setting_successful...")
    settings_page = SettingsPage(settings_setup)
    settings_page.change_settings(checkbox="click")

    # Verify success message after settings change
    login_page = LoginPage(settings_setup)
    login_page.wait_for_element_in_page_source("User info updated successfully!")
    assert "User info updated successfully!" in settings_setup.page_source

    # Verify 2FA is enabled in settings
    settings_page = SettingsPage(settings_setup)
    navigation_bar = NavigationBar(settings_setup)
    navigation_bar.select_settings_button()
    settings = settings_page.get_settings()
    assert settings['2fa']
    logger.info("test_enable_2fa_setting_successful completed successfully.\n")


# FAILS!
def test_change_to_blank_name_setting_failure(settings_setup):
    """
    Test changing name setting to blank (expect failure).

    Args:
        settings_setup: Fixture for setting up and tearing down the settings environment.
    """
    logger.info("Starting test_change_to_blank_name_setting_failure...")
    settings_page = SettingsPage(settings_setup)
    settings_page.edit_name_to_blank()

    settings_page.wait_for_element_in_page_source("This field is required")  # Wait for error message
    assert "This field is required" in settings_setup.page_source  # Verify the error message is present
    logger.info("test_change_to_blank_name_setting_failure completed successfully.\n")


# FAILS!
def test_change_to_blank_email_setting_failure(settings_setup):
    """
    Test changing email setting to blank (expect failure).

    Args:
        settings_setup: Fixture for setting up and tearing down the settings environment.
    """
    logger.info("Starting test_change_to_blank_email_setting_failure...")
    settings_page = SettingsPage(settings_setup)
    settings_page.edit_email_to_blank()

    settings_page.wait_for_element_in_page_source("This field is required")  # Wait for error message
    assert "This field is required" in settings_setup.page_source  # Verify the error message is present
    logger.info("test_change_to_blank_email_setting_failure completed successfully.\n")


# FAILS!
def test_change_to_blank_password_setting_failure(settings_setup):
    """
    Test changing password setting to blank (expect failure).

    Args:
        settings_setup: Fixture for setting up and tearing down the settings environment.
    """
    logger.info("Starting test_change_to_blank_password_setting_failure...")
    settings_page = SettingsPage(settings_setup)
    settings_page.edit_password_to_blank()

    settings_page.wait_for_element_in_page_source("This field is required")  # Wait for error message
    assert "This field is required" in settings_setup.page_source  # Verify the error message is present
    logger.info("test_change_to_blank_password_setting_failure completed successfully.\n")
