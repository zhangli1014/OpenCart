from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def type_into_element(self, locator_name, locator_value,text):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)
    def type_into_elements(self, locator_name, locator_value,text):
        elements = self.get_elements(locator_name, locator_value)
        for element in elements:
            element.click()
            element.clear()
            element.send_keys(text)

    def element_click(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()

    def elements_click(self, locator_name, locator_value):
        elements = self.get_elements(locator_name, locator_value)
        for element in elements:
            element.click()

    def element_action_click(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def check_display_status_of_element(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()

    def retrieve_element_text(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text

    def retrieve_elements_text(self, locator_name, locator_value):
        elements = self.get_elements(locator_name, locator_value)
        return [element.text for element in elements]

    def get_element(self, locator_name, locator_value):

        element = None
        #print(f"Locator Name: {locator_name}, Locator Value: {locator_value}")  # Debugging log
        if "_id" in locator_name:
            element = self.driver.find_element(By.ID, locator_value)
        elif "_name" in locator_name:
            element = self.driver.find_element(By.NAME, locator_value)
        elif "_class_name" in locator_name:
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif "_link_text" in locator_name:
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif "_partiallink_text" in locator_name:
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, locator_value)
        elif "_xpath" in locator_name:
            element = self.driver.find_element(By.XPATH, locator_value)
        elif "_css" in locator_name:
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        #print(f"Locator Name: {locator_name}, Locator Value: {locator_value}")  # Debugging log

        return element

    def get_elements(self, locator_name, locator_value):

        elements = []
        #print(f"Locator Name: {locator_name}, Locator Value: {locator_value}")  # Debugging log
        if "_id" in locator_name:
            elements = self.driver.find_elements(By.ID, locator_value)
        elif "_name" in locator_name:
            elements = self.driver.find_elements(By.NAME, locator_value)
        elif "_class_name" in locator_name:
            elements = self.driver.find_elements(By.CLASS_NAME, locator_value)
        elif "_link_text" in locator_name:
            elements = self.driver.find_elements(By.LINK_TEXT, locator_value)
        elif "_xpath" in locator_name:
            elements = self.driver.find_elements(By.XPATH, locator_value)
        elif "_css" in locator_name:
            elements = self.driver.find_elements(By.CSS_SELECTOR, locator_value)
        #print(f"Locator Name: {locator_name}, Locator Value: {locator_value}")  # Debugging log

        return elements