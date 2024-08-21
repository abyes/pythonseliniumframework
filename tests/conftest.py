import os
from _pydatetime import time

import pytest
import logging
from selenium import webdriver
driver = None

# Register the command-line option
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Name of the browser to use for testing"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported.")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()
    print(f"Browser selected: {browser_name}")


@pytest.fixture(scope="function")
def logger():
    logger = logging.getLogger("TestLogger")
    # Clear existing handlers if any
    for handler in logger.handlers:
        logger.removeHandler(handler)
    logger.handlers.clear()
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler("test_log.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    yield logger
    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)
# Directory where screenshots will be saved

# Define the hook for taking screenshots on test failure

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
