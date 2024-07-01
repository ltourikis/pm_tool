from pmtool.pages.task_page import TaskPage
from pmtool.pages.project_page import ProjectPage
from pmtool.utils.utils import generate_random_sublist


def test_add_task_required_fields_success(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    task_page.create_task("Task1", "Task1 Description")
    assert task_page.check_if_task_present("Task1", "Task1 Description", "TO DO")


def test_add_task_status_to_do_success(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    task_page.create_task("Task2", "Task2 Description", "TO DO")
    assert task_page.check_if_task_present("Task2", "Task2 Description", "TO DO")


def test_add_task_status_in_progress_success(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    task_page.create_task("Task3", "Task3 Description", "IN PROGRESS")
    assert task_page.check_if_task_present("Task3", "Task3 Description", "IN PROGRESS")


def test_add_task_status_in_review_success(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    task_page.create_task("Task4", "Task4 Description", "IN REVIEW")
    assert task_page.check_if_task_present("Task4", "Task4 Description", "IN REVIEW")


def test_add_task_status_done_success(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    task_page.create_task("Task5", "Task5 Description", "DONE")
    assert task_page.check_if_task_present("Task5", "Task5 Description", "DONE")


def test_add_task_random_labels_success(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    random_labels = generate_random_sublist(task_page.labels)
    random_status = generate_random_sublist(task_page.status)[0]
    task_page.create_task("Task6", "Task6 Description", random_status, labels=random_labels)
    assert task_page.check_if_task_present("Task6", "Task6 Description", random_status, labels=random_labels)


def test_add_task_all_labels_success(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    random_status = generate_random_sublist(task_page.status)[0]
    task_page.create_task("Task67", "Task67 Description", random_status, labels=task_page.labels)
    assert task_page.check_if_task_present("Task67", "Task67 Description", random_status, labels=task_page.labels)


def test_add_task_upload_one_file_success(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    random_status = generate_random_sublist(task_page.status)[0]
    random_labels = generate_random_sublist(task_page.labels)
    files_list = [task_page.file1_path]
    task_page.create_task("Task66", "Task66 Description", random_status,
                          labels=random_labels, files=files_list)
    assert task_page.check_if_task_present("Task66", "Task66 Description", random_status,
                                           labels=random_labels, files=files_list)


def test_add_task_upload_two_files_success(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    random_status = generate_random_sublist(task_page.status)[0]
    random_labels = generate_random_sublist(task_page.labels)
    files_list = [task_page.file1_path, task_page.file2_path]
    task_page.create_task("Task7", "Task7 Description", random_status,
                          labels=random_labels, files=files_list)
    assert task_page.check_if_task_present("Task7", "Task7 Description", random_status,
                                           labels=random_labels, files=files_list)


def test_add_task_missing_summary_fail(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    random_status = generate_random_sublist(task_page.status)[0]
    task_page.create_task("", "Task7 Description", random_status)
    task_page.wait_for_element_in_page_source("This field is required")
    # Assert error message
    assert "This field is required" in task_setup.page_source


def test_add_task_missing_description_fail(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    random_status = generate_random_sublist(task_page.status)[0]
    task_page.create_task("Task7", "", random_status)
    task_page.wait_for_element_in_page_source("This field is required")
    # Assert error message
    assert "This field is required" in task_setup.page_source


def test_view_tasks_success(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.view_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    task_page.wait_for_element_in_page_source("Task66")
    assert "Task66" in task_setup.page_source
    assert "Task67" in task_setup.page_source


def test_delete_task_success(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.view_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    task_page.wait_for_element_in_page_source("Task67")
    task_page.delete_task("Task67")
    task_page.delete_task("Task66")
    task_setup.refresh()
    assert "Task66" not in task_setup.page_source
    assert "Task67" not in task_setup.page_source


def test_cancel_delete_task_success(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.view_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    task_page.wait_for_element_in_page_source("Task6")
    task_page.cancel_delete_task("Task6")
    task_setup.refresh()
    task_page.wait_for_element_in_page_source("Task6")
    assert "Task6" in task_setup.page_source


def test_edit_task_success(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.add_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    files_list = [task_page.file1_path]
    updated_files_list = [task_page.file3_path]
    task_page.create_task("Task_before_edit", "Task Description Before edit", "TO DO",
                          labels=["backend", "frontend"], files=files_list)
    assert task_page.check_if_task_present("Task_before_edit", "Task Description Before edit",
                                           "TO DO", labels=["backend", "frontend"], files=files_list)
    task_page.click_edit_task("Task_before_edit")
    task_page.edit_task("Task_after_edit", "Task Description After edit", "DONE",
                        add_labels=["jenkins"], remove_labels=["frontend"], add_files=[task_page.file3_path],
                        remove_files=files_list)

    task_page.wait_for_element_in_page_source("Task_after_edit")
    assert task_page.check_if_task_present("Task_after_edit", "Task Description After edit",
                                           "DONE", labels=["backend", "jenkins"],
                                           files=updated_files_list)


# Something going very wrong with this TC!
def test_edit_task_missing_summary_fail(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.view_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    task_page.click_edit_task("Task2")
    task_page.edit_summary_blank()
    task_page.wait_for_element_in_page_source("This field is required")
    assert "This field is required" in task_setup.page_source


# Something going very wrong with this TC!
def test_edit_task_missing_description_fail(task_setup, task_teardown):
    project_page = ProjectPage(task_setup)
    project_page.view_task("ForTaskManagement")
    task_page = TaskPage(task_setup)
    task_page.click_edit_task("Task_after_edit")
    task_page.edit_description_blank()
    task_page.wait_for_element_in_page_source("This field is required")
    assert "This field is required" in task_setup.page_source
