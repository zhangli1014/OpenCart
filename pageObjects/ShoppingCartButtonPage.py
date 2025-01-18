#After click shopping button, pop up a ui
from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage

class ShoppingCartButtonPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
