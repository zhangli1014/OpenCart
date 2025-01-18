import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 启动浏览器
driver = webdriver.Chrome()
driver.get("http://localhost/opencart/upload/index.php")

driver.find_element(By.LINK_TEXT,'Tablets').click()
time.sleep(10)

driver.find_element(By.XPATH,'//button[contains(@onclick,"cart.add")]').click()
time.sleep(5)

driver.quit()
