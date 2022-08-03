import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        serv_obj = Service("C:\\Driver\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    elif browser == 'firefox':
        serv_obj = Service("/home/prashant/Documents/Browser_Driver/geckodriver")
        driver = webdriver.Firefox(service=serv_obj)
    else:
        serv_obj = Service("C:\\Driver\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI  /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return browser value to setup method
    return request.config.getoption("--browser")


############ Pytest HTML Report ##############

# It is hook for adding environment info to HTNL Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Prashant'


# It is hook for delete/modify Envirnment info to HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
