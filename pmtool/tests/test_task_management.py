from pmtool.pages.task_page import TaskPage
from pmtool.pages.project_page import ProjectPage
from pmtool.utils.utils import generate_random_sublist


def test_add_task_required_fields_success(task_setup, task_teardown):
    """
    Test adding a task with required fields only.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")  # Create a project for task management

    task_page = TaskPage(task_setup)
    task_page.create_task("Task1", "Task1 Description")  # Add a task with required fields

    assert task_page.check_if_task_present("Task1", "Task1 Description", "TO DO")  # Verify the task is present


def test_add_task_status_to_do_success(task_setup, task_teardown):
    """
    Test adding a task with 'TO DO' status.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")  # Create a project for task management

    task_page = TaskPage(task_setup)
    task_page.create_task("Task2", "Task2 Description", "TO DO")  # Add a task with 'TO DO' status

    assert task_page.check_if_task_present("Task2", "Task2 Description", "TO DO")  # Verify the task is present


def test_add_task_status_in_progress_success(task_setup, task_teardown):
    """
    Test adding a task with 'IN PROGRESS' status.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")  # Create a project for task management

    task_page = TaskPage(task_setup)
    task_page.create_task("Task3", "Task3 Description", "IN PROGRESS")  # Add a task with 'IN PROGRESS' status

    assert task_page.check_if_task_present("Task3", "Task3 Description", "IN PROGRESS")  # Verify the task is present


def test_add_task_status_in_review_success(task_setup, task_teardown):
    """
    Test adding a task with 'IN REVIEW' status.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")  # Create a project for task management

    task_page = TaskPage(task_setup)
    task_page.create_task("Task4", "Task4 Description", "IN REVIEW")  # Add a task with 'IN REVIEW' status

    assert task_page.check_if_task_present("Task4", "Task4 Description", "IN REVIEW")  # Verify the task is present


def test_add_task_status_done_success(task_setup, task_teardown):
    """
    Test adding a task with 'DONE' status.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")  # Create a project for task management

    task_page = TaskPage(task_setup)
    task_page.create_task("Task5", "Task5 Description", "DONE")  # Add a task with 'DONE' status

    assert task_page.check_if_task_present("Task5", "Task5 Description", "DONE")  # Verify the task is present


def test_add_task_random_labels_success(task_setup, task_teardown):
    """
    Test adding a task with random labels.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")  # Create a project for task management

    task_page = TaskPage(task_setup)
    random_labels = generate_random_sublist(task_page.labels)  # Generate random labels
    random_status = generate_random_sublist(task_page.status)[0]  # Generate random status
    # Add a task with random labels
    task_page.create_task("Task6", "Task6 Description", random_status, labels=random_labels)

    assert task_page.check_if_task_present("Task6", "Task6 Description", random_status,
                                           labels=random_labels)  # Verify the task is present


def test_add_task_all_labels_success(task_setup, task_teardown):
    """
    Test adding a task with all available labels.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")  # Create a project for task management

    task_page = TaskPage(task_setup)
    random_status = generate_random_sublist(task_page.status)[0]  # Generate random status
    task_page.create_task("Task67", "Task67 Description", random_status,
                          labels=task_page.labels)  # Add a task with all labels

    assert task_page.check_if_task_present("Task67", "Task67 Description", random_status,
                                           labels=task_page.labels)  # Verify the task is present


def test_add_task_upload_one_file_success(task_setup, task_teardown):
    """
    Test adding a task with one uploaded file.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")  # Create a project for task management

    task_page = TaskPage(task_setup)
    random_status = generate_random_sublist(task_page.status)[0]  # Generate random status
    random_labels = generate_random_sublist(task_page.labels)  # Generate random labels
    files_list = [task_page.file1_path]  # Specify a file to upload
    task_page.create_task("Task66", "Task66 Description", random_status, labels=random_labels,
                          files=files_list)  # Add a task with one file

    assert task_page.check_if_task_present("Task66", "Task66 Description", random_status,
                                           labels=random_labels, files=files_list)  # Verify the task is present


def test_add_task_upload_two_files_success(task_setup, task_teardown):
    """
    Test adding a task with two uploaded files.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")  # Create a project for task management

    task_page = TaskPage(task_setup)
    random_status = generate_random_sublist(task_page.status)[0]  # Generate random status
    random_labels = generate_random_sublist(task_page.labels)  # Generate random labels
    files_list = [task_page.file1_path, task_page.file2_path]  # Specify two files to upload
    task_page.create_task("Task7", "Task7 Description", random_status, labels=random_labels,
                          files=files_list)  # Add a task with two files

    assert task_page.check_if_task_present("Task7", "Task7 Description", random_status,
                                           labels=random_labels, files=files_list)  # Verify the task is present


def test_add_task_missing_summary_fail(task_setup, task_teardown):
    """
    Test adding a task without a summary and expect failure.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")  # Create a project for task management

    task_page = TaskPage(task_setup)
    random_status = generate_random_sublist(task_page.status)[0]  # Generate random status
    task_page.create_task("", "Task7 Description", random_status)  # Add a task without a summary

    task_page.wait_for_element_in_page_source("This field is required")  # Wait for error message
    assert "This field is required" in task_setup.page_source  # Verify the error message is present


def test_add_task_missing_description_fail(task_setup, task_teardown):
    """
    Test adding a task without a description and expect failure.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")  # Create a project for task management

    task_page = TaskPage(task_setup)
    random_status = generate_random_sublist(task_page.status)[0]  # Generate random status
    task_page.create_task("Task7", "", random_status)  # Add a task without a description

    task_page.wait_for_element_in_page_source("This field is required")  # Wait for error message
    assert "This field is required" in task_setup.page_source  # Verify the error message is present


def test_view_tasks_success(task_setup, task_teardown):
    """
    Test viewing tasks after adding them.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.view_task("ForTaskManagement")  # View the project for task management

    task_page = TaskPage(task_setup)
    task_page.wait_for_element_in_page_source("Task66")  # Wait for task to appear

    assert "Task66" in task_setup.page_source  # Verify task is present
    assert "Task67" in task_setup.page_source  # Verify task is present


def test_delete_task_success(task_setup, task_teardown):
    """
    Test deleting tasks.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.view_task("ForTaskManagement")  # View the project for task management

    task_page = TaskPage(task_setup)
    task_page.wait_for_element_in_page_source("Task67")  # Wait for task to appear
    task_page.delete_task("Task67")  # Delete the task
    task_page.delete_task("Task66")  # Delete the task
    task_setup.refresh()  # Refresh the page

    assert "Task66" not in task_setup.page_source  # Verify task is deleted
    assert "Task67" not in task_setup.page_source  # Verify task is deleted


def test_cancel_delete_task_success(task_setup, task_teardown):
    """
    Test cancelling the deletion of tasks.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.view_task("ForTaskManagement")  # View the project for task management

    task_page = TaskPage(task_setup)
    task_page.wait_for_element_in_page_source("Task6")  # Wait for task to appear
    task_page.cancel_delete_task("Task6")  # Cancel the deletion of the task
    task_setup.refresh()  # Refresh the page
    task_page.wait_for_element_in_page_source("Task6")  # Wait for task to appear

    assert "Task6" in task_setup.page_source  # Verify task is present


def test_edit_task_success(task_setup, task_teardown):
    """
    Test editing a task.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")  # Create a project for task management

    task_page = TaskPage(task_setup)
    files_list = [task_page.file1_path]  # Specify initial file
    updated_files_list = [task_page.file3_path]  # Specify updated file
    task_page.create_task("Task_before_edit", "Task Description Before edit", "TO DO",
                          labels=["backend", "frontend"], files=files_list)  # Add a task

    assert task_page.check_if_task_present("Task_before_edit", "Task Description Before edit",
                                           "TO DO", labels=["backend", "frontend"],
                                           files=files_list)  # Verify the task is present

    task_page.click_edit_task("Task_before_edit")  # Click to edit the task
    task_page.edit_task("Task_after_edit", "Task Description After edit", "DONE",
                        add_labels=["jenkins"], remove_labels=["frontend"], add_files=[task_page.file3_path],
                        remove_files=files_list)  # Edit the task

    task_page.wait_for_element_in_page_source("Task_after_edit")  # Wait for updated task to appear
    assert task_page.check_if_task_present("Task_after_edit", "Task Description After edit",
                                           "DONE", labels=["backend", "jenkins"],
                                           files=updated_files_list)  # Verify the updated task is present


# FAILS!!
def test_edit_task_missing_summary_fail(task_setup, task_teardown):
    """
    Test editing a task without a summary and expect failure.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.view_task("ForTaskManagement")  # View the project for task management

    task_page = TaskPage(task_setup)
    task_page.click_edit_task("Task2")  # Click to edit the task
    task_page.edit_summary_blank()  # Edit the task to have a blank summary

    task_page.wait_for_element_in_page_source("This field is required")  # Wait for error message
    assert "This field is required" in task_setup.page_source  # Verify the error message is present

# FAILS!!
def test_edit_task_missing_description_fail(task_setup, task_teardown):
    """
    Test editing a task without a description and expect failure.

    Args:
        task_setup: Fixture for setting up the test environment.
        task_teardown: Fixture for tearing down the test environment.
    """
    project_page = ProjectPage(task_setup)
    project_page.view_task("ForTaskManagement")  # View the project for task management

    task_page = TaskPage(task_setup)
    task_page.click_edit_task("Task_after_edit")  # Click to edit the task
    task_page.edit_description_blank()  # Edit the task to have a blank description

    task_page.wait_for_element_in_page_source("This field is required")  # Wait for error message
    assert "This field is required" in task_setup.page_source  # Verify the error message is present
