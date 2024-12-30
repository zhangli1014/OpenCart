import pytest
from selenium import webdriver
from utilities.readconfig import readConfig

@pytest.fixture()
def setup_teardown(request):
    baseURL = readConfig.getconfig('opencart info', 'baseURL')
    browser = readConfig.getconfig('opencart info', 'browser')
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")
    driver.get(baseURL)
    request.cls.driver = driver # return driver to class instance
    yield
    driver.quit()

