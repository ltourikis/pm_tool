from pmtool.pages.login_page import LoginPage
from pmtool.pages.settings_page import SettingsPage
from pmtool.pages.navigation_bar import NavigationBar
from pmtool.pages.taskdb_page import TaskDBPage
from pmtool.pages.project_page import ProjectPage
from pmtool.pages.task_page import TaskPage
import time


def test_view_tasks_successful(taskdb_setup_teardown):

    navigation_bar = NavigationBar(taskdb_setup_teardown)
    navigation_bar.select_tasks_db_button()
    taskdb_page = TaskDBPage(taskdb_setup_teardown)
    tasks_present = ["A_Task", "B_Task", "$_Task", "Z_Task"]
    assert taskdb_page.check_if_tasks_present(tasks_present)


def test_add_task_check_taskdb_successful(taskdb_setup_teardown):

    navigation_bar = NavigationBar(taskdb_setup_teardown)
    project_page = ProjectPage(taskdb_setup_teardown)
    task_page = TaskPage(taskdb_setup_teardown)

    navigation_bar.select_dashboard_button()
    project_page.add_task("ForTaskDBTests1")
    task_page.create_task("Just_Added", "Just_Added Description")

    navigation_bar.select_tasks_db_button()
    taskdb_page = TaskDBPage(taskdb_setup_teardown)
    tasks_present = ["A_Task", "B_Task", "$_Task", "Z_Task", "Just_Added"]
    assert taskdb_page.check_if_tasks_present(tasks_present)


def test_remove_task_check_taskdb_successful(taskdb_setup_teardown):

    navigation_bar = NavigationBar(taskdb_setup_teardown)
    project_page = ProjectPage(taskdb_setup_teardown)
    task_page = TaskPage(taskdb_setup_teardown)

    navigation_bar.select_dashboard_button()
    project_page.view_task("ForTaskDBTests1")
    task_page.delete_task("Just_Added")

    navigation_bar.select_tasks_db_button()
    taskdb_page = TaskDBPage(taskdb_setup_teardown)
    tasks_present = ["A_Task", "B_Task", "$_Task", "Z_Task"]
    assert taskdb_page.check_if_tasks_present(tasks_present)
    tasks_deleted = ["Just_Added"]
    taskdb_page.driver.refresh()
    assert taskdb_page.check_if_tasks_not_present(tasks_deleted)


def test_sort_tasks_by_summary(taskdb_setup_teardown):
    navigation_bar = NavigationBar(taskdb_setup_teardown)
    navigation_bar.select_tasks_db_button()
    taskdb_page = TaskDBPage(taskdb_setup_teardown)

    # Click the "Sort by Summary" button
    taskdb_page.click_sort()

    # Wait for the page to load after sorting
    taskdb_page.wait_for_page_load()

    # Get the titles of the tasks after sorting
    sorted_task_titles = taskdb_page.get_sorted_tasks()

    assert sorted_task_titles == sorted(sorted_task_titles)

    # Click the "Sort by Summary" button
    # This time the Tasks should be sorted in descending order
    taskdb_page.click_sort()

    # Wait for the page to load after sorting
    taskdb_page.wait_for_page_load()

    # Get the titles of the tasks after sorting
    sorted_task_titles = taskdb_page.get_sorted_tasks()
    assert sorted_task_titles == sorted(sorted_task_titles, reverse=True)


def test_search_field(taskdb_setup_teardown):

    navigation_bar = NavigationBar(taskdb_setup_teardown)
    navigation_bar.select_tasks_db_button()
    taskdb_page = TaskDBPage(taskdb_setup_teardown)
    taskdb_page.wait_for_page_load()

    # Check initial state
    expected_tasks = ["$_Task", "A_Task", "B_Task", "Z_Task"]
    visible_tasks = taskdb_page.get_tasks()
    print(visible_tasks)
    assert set(visible_tasks) == set(expected_tasks)

    # Search for 'A_Task'
    taskdb_page.search_task("A_Task")
    visible_tasks = taskdb_page.get_tasks()
    assert visible_tasks == ["A_Task"]

    # Search for 'B_Task'
    taskdb_page.search_task("B_Task")
    visible_tasks = taskdb_page.get_tasks()
    assert visible_tasks == ["B_Task"]

    # Search for '$_Task'
    taskdb_page.search_task("$_Task")
    visible_tasks = taskdb_page.get_tasks()
    assert visible_tasks == ["$_Task"]

    # Search for 'Z_Task'
    taskdb_page.search_task("Z_Task")
    visible_tasks = taskdb_page.get_tasks()
    assert visible_tasks == ["Z_Task"]

    # Search for a task that does not exist
    taskdb_page.search_task("Non_Existent_Task")
    visible_tasks = taskdb_page.get_tasks()
    assert visible_tasks == []
