from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
     driver= webdriver.Chrome()
     print("launching chrome browser .......")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("launching Firefox browser")
    else:
        driver = webdriver.Edge()

    return driver


def pytest_addoption(parser):# this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):# this will return browser value to setup method
    return request.config.getoption("--browser")


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
