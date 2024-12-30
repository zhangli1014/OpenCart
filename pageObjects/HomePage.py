from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage

class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    #define the element locate function
    #my_account_drop_menu_xpath = "//span[text()='My Account']"
    my_account_drop_menu_xpath = "//a[@title='My Account']"

    login_option_link_text = "Login"
    register_option_link_text = "Register"
    wish_list_id = 'wishlist-total'
    shopping_cart_xpath ='//a[@title="Shopping Cart"]'

    search_box_css = '#search>input[name="search"]'
    search_button_xpath = '//*[@id="search"]/span/button'
    cart_button_id = 'cart-total'

    def enter_product_into_search_box(self, product_name):
        self.type_into_element("search_box_css",self.search_box_css,product_name)

    def click_on_search_button(self):
        self.element_click("search_button_xpath", self.search_button_xpath)

    def click_on_my_account_drop_menu(self):
        self.element_click("my_account_drop_menu_xpath", self.my_account_drop_menu_xpath)

    def action_click_on_my_account_drop_menu(self):
        self.element_action_click("my_account_drop_menu_xpath", self.my_account_drop_menu_xpath)

    def get_my_account_drop_menu(self):
        self.get_element("my_account_drop_menu_xpath", self.my_account_drop_menu_xpath)
    def select_login_option(self):
        self.element_click("login_option_link_text", self.login_option_link_text)

    def naviage_to_login_page(self):
        return self.select_login_option()

    def select_register_option(self):
        self.element_click("register_option_link_text", self.register_option_link_text)