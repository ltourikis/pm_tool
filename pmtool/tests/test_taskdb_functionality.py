from pmtool.pages.navigation_bar import NavigationBar
from pmtool.pages.taskdb_page import TaskDBPage
from pmtool.pages.project_page import ProjectPage
from pmtool.pages.task_page import TaskPage


def test_view_tasks_successful(taskdb_setup_teardown):
    """
    Test to verify that all expected tasks are present in the TaskDB page.

    Parameters:
    taskdb_setup_teardown (fixture): Setup and teardown fixture for the task database.
    """
    navigation_bar = NavigationBar(taskdb_setup_teardown)
    navigation_bar.select_tasks_db_button()
    taskdb_page = TaskDBPage(taskdb_setup_teardown)

    # List of tasks expected to be present
    tasks_present = ["A_Task", "B_Task", "$_Task", "Z_Task"]

    # Assert that all expected tasks are present
    assert taskdb_page.check_if_tasks_present(tasks_present)


def test_add_task_check_taskdb_successful(taskdb_setup_teardown):
    """
    Test to verify that a task added is present in the TaskDB page.

    Parameters:
    taskdb_setup_teardown (fixture): Setup and teardown fixture for the task database.
    """
    navigation_bar = NavigationBar(taskdb_setup_teardown)
    project_page = ProjectPage(taskdb_setup_teardown)
    task_page = TaskPage(taskdb_setup_teardown)

    # Navigate to the dashboard and add a new task
    navigation_bar.select_dashboard_button()
    project_page.add_task("ForTaskDBTests1")
    task_page.create_task("Just_Added", "Just_Added Description")

    # Navigate to the TaskDB page and check for the presence of the newly added task
    navigation_bar.select_tasks_db_button()
    taskdb_page = TaskDBPage(taskdb_setup_teardown)
    tasks_present = ["A_Task", "B_Task", "$_Task", "Z_Task", "Just_Added"]

    # Assert that all expected tasks, including the new one, are present
    assert taskdb_page.check_if_tasks_present(tasks_present)


def test_remove_task_check_taskdb_successful(taskdb_setup_teardown):
    """
    Test to verify that a task removed is no longer present in the TaskDB page.

    Parameters:
    taskdb_setup_teardown (fixture): Setup and teardown fixture for the task database.
    """
    navigation_bar = NavigationBar(taskdb_setup_teardown)
    project_page = ProjectPage(taskdb_setup_teardown)
    task_page = TaskPage(taskdb_setup_teardown)

    # Navigate to the dashboard, view the task and delete it
    navigation_bar.select_dashboard_button()
    project_page.view_task("ForTaskDBTests1")
    task_page.delete_task("Just_Added")

    # Navigate to the TaskDB page and check for the absence of the deleted task
    navigation_bar.select_tasks_db_button()
    taskdb_page = TaskDBPage(taskdb_setup_teardown)
    tasks_present = ["A_Task", "B_Task", "$_Task", "Z_Task"]

    # Assert that all expected tasks, except the deleted one, are present
    assert taskdb_page.check_if_tasks_present(tasks_present)

    # Refresh the page and check that the deleted task is not present
    tasks_deleted = ["Just_Added"]
    taskdb_page.driver.refresh()
    assert taskdb_page.check_if_tasks_not_present(tasks_deleted)


def test_sort_tasks_by_summary(taskdb_setup_teardown):
    """
    Test to verify that tasks can be sorted by their summary in both ascending and descending order.

    Parameters:
    taskdb_setup_teardown (fixture): Setup and teardown fixture for the task database.
    """
    navigation_bar = NavigationBar(taskdb_setup_teardown)
    navigation_bar.select_tasks_db_button()
    taskdb_page = TaskDBPage(taskdb_setup_teardown)

    # Click the "Sort by Summary" button to sort tasks in ascending order
    taskdb_page.click_sort()

    # Wait for the page to load after sorting
    taskdb_page.wait_for_page_load()

    # Get the titles of the tasks after sorting
    sorted_task_titles = taskdb_page.get_tasks()

    # Assert that tasks are sorted in ascending order
    assert sorted_task_titles == sorted(sorted_task_titles)

    # Click the "Sort by Summary" button again to sort tasks in descending order
    taskdb_page.click_sort()

    # Wait for the page to load after sorting
    taskdb_page.wait_for_page_load()

    # Get the titles of the tasks after sorting
    sorted_task_titles = taskdb_page.get_tasks()

    # Assert that tasks are sorted in descending order
    assert sorted_task_titles == sorted(sorted_task_titles, reverse=True)


def test_search_field(taskdb_setup_teardown):
    """
    Test to verify that the search functionality works correctly in the TaskDB page.

    Parameters:
    taskdb_setup_teardown (fixture): Setup and teardown fixture for the task database.
    """
    navigation_bar = NavigationBar(taskdb_setup_teardown)
    navigation_bar.select_tasks_db_button()
    taskdb_page = TaskDBPage(taskdb_setup_teardown)
    taskdb_page.wait_for_page_load()

    # Check initial state of tasks present
    expected_tasks = ["$_Task", "A_Task", "B_Task", "Z_Task"]
    visible_tasks = taskdb_page.get_tasks()
    print(visible_tasks)
    assert set(visible_tasks) == set(expected_tasks)

    # Search for each task individually and verify the search results
    search_tasks = ["A_Task", "B_Task", "$_Task", "Z_Task"]
    for task in search_tasks:
        taskdb_page.search_task(task)
        visible_tasks = taskdb_page.get_tasks()
        assert visible_tasks == [task]

    # Search for a non-existent task and verify the search result is empty
    taskdb_page.search_task("Non_Existent_Task")
    visible_tasks = taskdb_page.get_tasks()
    assert visible_tasks == []
