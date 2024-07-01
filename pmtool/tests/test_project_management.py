import time

from pmtool.pages.project_page import ProjectPage


def test_add_new_project_success(general_setup_teardown):
    project_page = ProjectPage(general_setup_teardown)
    project_page.add_project("Project1", "Description1")
    project_page.wait_for_element_in_page_source("Project1")
    assert "Project1" in general_setup_teardown.page_source
    project_page.add_project("Project2", "Description2")
    project_page.wait_for_element_in_page_source("Project2")
    assert "Project2" in general_setup_teardown.page_source


def test_edit_project_name_description_success(general_setup_teardown):
    project_page = ProjectPage(general_setup_teardown)
    project_page.edit_project("Project2", "Project3", "Description3")
    time.sleep(1)
    project_page.wait_for_element_in_page_source("Project3")
    assert "Project3" in general_setup_teardown.page_source
    assert "Project2" not in general_setup_teardown.page_source


def test_edit_project_name_success(general_setup_teardown):
    project_page = ProjectPage(general_setup_teardown)
    project_page.edit_project("Project3", "Project4")
    time.sleep(1)
    project_page.wait_for_element_in_page_source("Project4")
    assert "Project4" in general_setup_teardown.page_source
    assert "Project3" not in general_setup_teardown.page_source


def test_edit_project_description_success(general_setup_teardown):
    project_page = ProjectPage(general_setup_teardown)
    project_page.edit_project("Project4", new_description="Description4")
    time.sleep(1)
    project_page.wait_for_element_in_page_source("Description4")
    assert "Description4" in general_setup_teardown.page_source
    assert "Description3" not in general_setup_teardown.page_source


def test_edit_project_with_no_changes(general_setup_teardown):
    project_page = ProjectPage(general_setup_teardown)
    project_page.edit_project("Project4")
    time.sleep(1)
    project_page.wait_for_element_in_page_source("Description4")
    assert "Project4" in general_setup_teardown.page_source
    assert "Description4" in general_setup_teardown.page_source


def test_delete_existent_project(general_setup_teardown):
    project_page = ProjectPage(general_setup_teardown)
    project_page.delete_project("Project4")
    time.sleep(1)
    assert "Project4" not in general_setup_teardown.page_source
    assert "Description4" not in general_setup_teardown.page_source


def test_cancel_delete_existent_project(general_setup_teardown):
    project_page = ProjectPage(general_setup_teardown)
    project_page.cancel_delete_project("Project1")
    time.sleep(1)
    assert "Project1" in general_setup_teardown.page_source
    assert "Description1" in general_setup_teardown.page_source
