import time
import logging
from pmtool.pages.project_page import ProjectPage

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_add_new_project_successful(general_setup_teardown):
    """
    Test the successful addition of new projects.

    Args:
        general_setup_teardown: Fixture that sets up and tears down the test environment.
    """
    logger.info("Starting test_add_new_project_successful...")
    project_page = ProjectPage(general_setup_teardown)
    project_page.add_project("Project1", "Description1")
    project_page.wait_for_element_in_page_source("Project1")
    assert "Project1" in general_setup_teardown.page_source
    logger.info("Project1 added successfully.")

    project_page.add_project("Project2", "Description2")
    project_page.wait_for_element_in_page_source("Project2")
    assert "Project2" in general_setup_teardown.page_source
    logger.info("Project2 added successfully.")

    logger.info("test_add_new_project_successful completed successfully.")


def test_edit_project_name_description_successful(general_setup_teardown):
    """
    Test the successful editing of a project's name and description.

    Args:
        general_setup_teardown: Fixture that sets up and tears down the test environment.
    """
    logger.info("Starting test_edit_project_name_description_successful...")
    project_page = ProjectPage(general_setup_teardown)
    project_page.edit_project("Project2", "Project3", "Description3")
    time.sleep(1)
    project_page.wait_for_element_in_page_source("Project3")
    assert "Project3" in general_setup_teardown.page_source
    assert "Project2" not in general_setup_teardown.page_source
    logger.info("Project2 edited successfully to Project3.")

    logger.info("test_edit_project_name_description_successful completed successfully.")


def test_edit_project_name_successful(general_setup_teardown):
    """
    Test the successful editing of a project's name only.

    Args:
        general_setup_teardown: Fixture that sets up and tears down the test environment.
    """
    logger.info("Starting test_edit_project_name_successful...")
    project_page = ProjectPage(general_setup_teardown)
    project_page.edit_project("Project3", "Project4")
    time.sleep(1)
    project_page.wait_for_element_in_page_source("Project4")
    assert "Project4" in general_setup_teardown.page_source
    assert "Project3" not in general_setup_teardown.page_source
    logger.info("Project3 edited successfully to Project4.")

    logger.info("test_edit_project_name_successful completed successfully.")


def test_edit_project_description_successful(general_setup_teardown):
    """
    Test the successful editing of a project's description only.

    Args:
        general_setup_teardown: Fixture that sets up and tears down the test environment.
    """
    logger.info("Starting test_edit_project_description_successful...")
    project_page = ProjectPage(general_setup_teardown)
    project_page.edit_project("Project4", new_description="Description4")
    time.sleep(1)
    project_page.wait_for_element_in_page_source("Description4")
    assert "Description4" in general_setup_teardown.page_source
    assert "Description3" not in general_setup_teardown.page_source
    logger.info("Description of Project4 edited successfully to Description4.")

    logger.info("test_edit_project_description_successful completed successfully.")


def test_edit_project_with_no_changes_successful(general_setup_teardown):
    """
    Test editing a project without making any changes.

    Args:
        general_setup_teardown: Fixture that sets up and tears down the test environment.
    """
    logger.info("Starting test_edit_project_with_no_changes_successful...")
    project_page = ProjectPage(general_setup_teardown)
    project_page.edit_project("Project4")
    time.sleep(1)
    project_page.wait_for_element_in_page_source("Description4")
    assert "Project4" in general_setup_teardown.page_source
    assert "Description4" in general_setup_teardown.page_source
    logger.info("Project4 edited without changes successfully.")

    logger.info("test_edit_project_with_no_changes_successful completed successfully.")


def test_delete_existent_project_successful(general_setup_teardown):
    """
    Test the successful deletion of an existing project.

    Args:
        general_setup_teardown: Fixture that sets up and tears down the test environment.
    """
    logger.info("Starting test_delete_existent_project_successful...")
    project_page = ProjectPage(general_setup_teardown)
    project_page.delete_project("Project4")
    time.sleep(1)
    assert "Project4" not in general_setup_teardown.page_source
    assert "Description4" not in general_setup_teardown.page_source
    logger.info("Project4 deleted successfully.")

    logger.info("test_delete_existent_project_successful completed successfully.")


def test_cancel_delete_existent_project_successful(general_setup_teardown):
    """
    Test cancelling the deletion of an existing project.

    Args:
        general_setup_teardown: Fixture that sets up and tears down the test environment.
    """
    logger.info("Starting test_cancel_delete_existent_project_successful...")
    project_page = ProjectPage(general_setup_teardown)
    project_page.cancel_delete_project("Project1")
    time.sleep(1)
    assert "Project1" in general_setup_teardown.page_source
    assert "Description1" in general_setup_teardown.page_source
    logger.info("Deletion of Project1 cancelled successfully.")

    logger.info("test_cancel_delete_existent_project_successful completed successfully.")
