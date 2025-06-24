#update this test cases file.....

from pytest_metadata.plugin import metadata
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import FirefoxDriverManager



@pytest.fixture()
def setup(browser):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    if browser=='chrome':

        print("launching chrome browser .......")

    elif browser=='Firefox':
        driver = webdriver.Firefox(service=Service(FirefoxDriverManager().install()))

        print("launching Firefox browser")

    return driver

def pytest_addoption(parser):# this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):# this will return browser value to setup method
    return request.config.getoption("--browser")
##########Pytest html reports#######
# it is hook for adding environment info to html report
def pytest_html_report_title(report):
    report.title = "nop Commerce Automation Test Report"

    # metadata['Project Name']='nop Commerec'
    # metadata['Module Name'] = 'Customer'
    # metadata['Tester Name'] = 'karan'

# it is hook for delete and modify environment info to html reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
 metadata.pop("JAVA_HOME",None)
 metadata.pop("Plugins", None)

