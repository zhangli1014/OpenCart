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
    shopping_cart_option_xpath = "//a[@title='Shopping Cart']"
    shopping_cart_button_xpath = '//div[@id="cart"]'

    shopping_cart_empty_waring_xpath = '//div[@id="cart"]/ul/li/p' # click cart button create the warning
    add_product_to_cart_success_xpath = "//button[@onclick=\"cart.add('43');\"]" #mac
    add_product_to_cart_success_message_xpath = "//div[@class='alert alert-success alert-dismissible']"
    cart_link_after_add_product_xpath='//*[@id="common-home"]//a[text()="shopping cart"]'

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

    def shopping_cart_option_click(self):
        self.element_click("shopping_cart_option_xpath",self.shopping_cart_option_xpath)

    def shopping_cart_button_click(self):
        self.element_click("shopping_cart_button_xpath",self.shopping_cart_button_xpath)

    def retrieve_shopping_cart_empty_button_click_warning(self):
        return self.retrieve_element_text('shopping_cart_empty_waring_xpath',self.shopping_cart_empty_waring_xpath)

    def add_mac_to_cart(self):
        self.element_click("add_product_to_cart_success_xpath",self.add_product_to_cart_success_xpath)

    def retrieve_add_product_to_cart_success_message(self):
        return self.retrieve_element_text("add_product_to_cart_success_message_xpath",self.add_product_to_cart_success_message_xpath)
    def click_cart_link_after_add_product(self):
        self.element_click("cart_link_after_add_product_xpath",self.cart_link_after_add_product_xpath)