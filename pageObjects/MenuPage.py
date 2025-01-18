from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage

class MenuPage(BasePage):
    PRODUCT_ADD_BUTTON_xpath= '//button[contains(@onclick,"cart.add")]'
    add_product_to_cart_success_message_xpath = "//div[@class='alert alert-success alert-dismissible']"
    cart_link_after_add_product_xpath = '//*[@id="product-category"]//a[text()="shopping cart"]'
    homepage_xpath = '//div[@id="logo"]//img[@class="img-responsive"]'

    def navigate_to_category(self,link):
        category_link_text = link  # Replace with category name
        self.element_click("category_link_text",category_link_text)

    def add_product_from_category(self):
        self.element_click("PRODUCT_ADD_BUTTON_xpath",self.PRODUCT_ADD_BUTTON_xpath)

    def retrieve_add_product_to_cart_success_message(self):
        return self.retrieve_element_text("add_product_to_cart_success_message_xpath",
                                          self.add_product_to_cart_success_message_xpath)

    def click_cart_link_after_add_product(self):
        self.element_click("cart_link_after_add_product_xpath",self.cart_link_after_add_product_xpath)

    def click_homepage_link(self):
        self.element_click("homepage_xpath",self.homepage_xpath)