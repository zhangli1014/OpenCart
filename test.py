import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def test_1():

    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,"//a[@title='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Register").click()
    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    time.sleep(4)

    privacy = driver.find_element(By.XPATH,"//div[@id='account-register']/div[1]")
    print(privacy.text)
    assert privacy.text=="Warning: You must agree to the Privacy Policy!"

    element = driver.find_element(By.XPATH,"//input[@id='input-firstname']/following-sibling::div")
    print(element.text)

    assert element.text=="First Name must be between 1 and 32 characters!"

