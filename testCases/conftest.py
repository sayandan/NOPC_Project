from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from utilities.TestData import TestData
# fixtures are functions which will run before each test function to which it is applied.
# it is used to feed some data to tests such as db connections, url etc. to access the fixture function the tests have
# to mention the fixture name as input parameter


options = Options()
# disable popups that asked to allow locations etc, pass argument 1 to allow and 2 to block
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
# disable Chrome info bar that shows its been controlled by test
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # remove devtools/device errors
options.add_argument("start-maximized")

# # passing browser option using params
# @pytest.fixture(params=['chrome', 'edge'], scope='class')
# def init_driver(request):
#     if request.param == 'chrome':
#         web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH, options=options)
#     if request.param == 'edge':
#         web_driver = webdriver.Edge(executable_path=TestData.EDGE_EXECUTABLE_PATH)
#     web_driver.get(TestData.BASE_URL)
#     request.cls.driver = web_driver
#     yield
#     web_driver.quit()


""" get browser option from command line : --browser=chrome or --browser=edge"""
@pytest.fixture(scope='class')
def init_driver(request):
    browser = request.config.getoption('browser')
    if browser == 'chrome':
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH, options=options)
    elif browser == 'edge':
        web_driver = webdriver.Edge(executable_path=TestData.EDGE_EXECUTABLE_PATH)
    else:
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH, options=options)
    web_driver.get(TestData.BASE_URL)
    request.cls.driver = web_driver
    yield
    web_driver.quit()


def pytest_addoption(parser):   # this will get the browser value from CLI / hooks
    parser.addoption("--browser", action="store", default="chrome")


# ---------------PyTest HTML report  create report using the  CLI command --html=..\Reports\reports.html
# it is hook for adding environment ingo to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Siva'


# it is  hook for delete/modify environment info from html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

