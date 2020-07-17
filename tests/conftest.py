import pytest
import allure
from selene.support.shared import browser
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session', autouse=True)
def browser_management(request):
    """
    Here, before yield,
    goes all "setup" code for each test case
    aka "before test function" hook
    """

    # def attach_snapshots_on_failure(error: TimeoutException) -> Exception:
    #     """
    #     An example of selene hook_wait_failure that attaches snapshots to failed test step.
    #     It is actually not needed and optional,
    #     because in the pytest_runtest_makereport hook below
    #     we attach screenshots to the test body itself,
    #     that is more handy during analysis of test report
    #
    #     but if you need it, you can enable it by uncommenting
    #     together with the following ``browser.config.hook_wait_failure =`` line;)
    #
    #     otherwise, you can remove it
    #     """
    #     last_screenshot = browser.config.last_screenshot
    #     if last_screenshot:
    #         allure.attach.file(source=last_screenshot,
    #                            name='screenshot on failure',
    #                            attachment_type=allure.attachment_type.PNG)
    #
    #     last_page_source = browser.config.last_page_source
    #     if last_page_source:
    #         allure.attach.file(source=last_page_source,
    #                            name='page source on failure',
    #                            attachment_type=allure.attachment_type.HTML)
    #     return error
    # browser.config.hook_wait_failure = attach_snapshots_on_failure

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")

    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.config.base_url = 'https://www.saucedemo.com'
    browser.driver.maximize_window()

    yield

    """
    Here, after yield,
    goes all "tear down" code for each test case
    aka "after test function" hook
    """

    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def test_wrapper():
    yield

    browser.clear_session_storage()
    browser.driver.delete_all_cookies()

prev_test_screenshot = None
prev_test_page_source = None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_setup(item):
    yield

    global prev_test_screenshot
    prev_test_screenshot = browser.config.last_screenshot
    global prev_test_page_source
    prev_test_page_source = browser.config.last_page_source


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):
    """
    Attach snapshots on test failure
    """

    # All code prior to yield statement would be ran prior
    # to any other of the same fixtures defined

    outcome = yield # Run all other pytest_runtest_makereport non wrapped hooks
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        last_screenshot = browser.config.last_screenshot
        if last_screenshot and not last_screenshot == prev_test_screenshot:
            allure.attach.file(source=last_screenshot,
                               name='screenshot',
                               attachment_type=allure.attachment_type.PNG)

        last_page_source = browser.config.last_page_source
        if last_page_source and not last_page_source == prev_test_page_source:
            allure.attach.file(source=last_page_source,
                               name='page source',
                               attachment_type=allure.attachment_type.HTML)
