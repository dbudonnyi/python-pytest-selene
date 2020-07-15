import pytest
from selene.support.shared import browser


@pytest.fixture(scope='class', autouse=True)
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

    browser.config.timeout = 3
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://www.saucedemo.com/'

    yield

    """
    Here, after yield,
    goes all "tear down" code for each test case
    aka "after test function" hook
    """

    browser.quit()

# @pytest.fixture(scope='class')
# def login_cookie():
#