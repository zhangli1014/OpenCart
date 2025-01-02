import pytest
from selenium import webdriver
from utilities.readconfig import readConfig
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup_teardown(request):
    baseURL = readConfig.getconfig('opencart info', 'baseURL')
    browser = readConfig.getconfig('opencart info', 'browser')
    # 设置 Chrome 无头模式
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 无头模式
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    if browser == 'chrome':
        driver = webdriver.Chrome()
        #driver = webdriver.Chrome(options = chrome_options)
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

