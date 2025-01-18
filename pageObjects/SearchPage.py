from pageObjects.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_link_text = "HP LP3065"
    no_product_message_xpath = "//input[@id='button-search']/following-sibling::p"
    add_product_to_cart_css = ".product-thumb .fa-shopping-cart"
    add_product_to_cart_success_message_xpath = "//div[@class='alert alert-success alert-dismissible']"
    cart_link_after_add_product_xpath = '//*[@id="product-search"]//a[text()="shopping cart"]'
    homepage_xpath = '//div[@id="logo"]//img[@class="img-responsive"]'


    def display_status_of_valid_product(self):
        return self.check_display_status_of_element("valid_hp_product_link_text", self.valid_hp_product_link_text)

    def retrieve_no_product_message(self):
        return self.retrieve_element_text("no_product_message_xpath", self.no_product_message_xpath)

    def add_product_to_cart_from_search(self):
        self.element_click('add_product_to_cart_css',self.add_product_to_cart_css)

    def retrieve_add_product_to_cart_success_message(self):
        return self.retrieve_element_text("add_product_to_cart_success_message_xpath",
                                          self.add_product_to_cart_success_message_xpath)

    def click_cart_link_after_add_product(self):
        self.element_click("cart_link_after_add_product_xpath",self.cart_link_after_add_product_xpath)
    def click_homepage_link(self):
        self.element_click("homepage_xpath",self.homepage_xpath)