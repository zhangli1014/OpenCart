from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage

class ShoppingCartPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    empty_shopping_cart_warning_xpath = '//div[@id="content"]/p'
    quantity_input_box_xpath='//div[@class="input-group btn-block"]/input'
    quantity_update_xpath='//span[@class="input-group-btn"]/button[@class="btn btn-primary"]'
    quantity_remove_xpath='//span[@class="input-group-btn"]/button[@class="btn btn-danger"]'
    unit_price_xpath = '//div[@class="input-group btn-block"]//../following-sibling::td[1]' # maybe not only one
    sigle_total_price_xpath =  '//div[@class="input-group btn-block"]//../following-sibling::td[2]' # total price for single product
    total_price_xpath = '//div[@class="col-sm-4 col-sm-offset-8"]//tr[4]/td[2]' # total price for all products
    continue_shopping_button_link_text = 'Continue Shopping'
    checkou_button_link_text = 'Checkout'
    update_quantity_warning_xpath = '//div[@id="checkout-cart"]/div[@class="alert alert-success alert-dismissible"]'
    update_quantity_over_stock_warning_xpath='//div[@id="checkout-cart"]/div[@class="alert alert-danger alert-dismissible"]'
    def enter_quantity_input_box(self,num):#modify the first quantity
        self.type_into_element("quantity_input_box_xpath",self.quantity_input_box_xpath,num)

    def enter_quantity_input_box_all(self,num):#modify  all the quantity
        self.type_into_elements("quantity_input_box_xpath",self.quantity_input_box_xpath,num)

    def click_quantity_update(self):#modify the first
        self.element_click("quantity_update_xpath",self.quantity_update_xpath)

    def click_quantity_update_all(self):
        self.element_click("quantity_update_xpath",self.quantity_update_xpath)

    def click_quantity_remove_one(self):
        self.element_click("quantity_remove_xpath",self.quantity_remove_xpath)
    def click_quantity_remove_all(self):
        self.elements_click("quantity_remove_xpath",self.quantity_remove_xpath)
    def click_continue_shopping_button(self):
        self.element_click("continue_shopping_button_link_text",self.continue_shopping_button_link_text)

    def click_check_out_button(self):
        self.element_click("checkou_button_link_text",self.checkou_button_link_text)

    def retrieve_update_quantity_warning(self):
        return self.retrieve_element_text("update_quantity_warning_xpath",self.update_quantity_warning_xpath)
    def retrieve_over_shopping_cart_quantity_warning(self):
        return self.retrieve_element_text("update_quantity_over_stock_warning_xpath", self.update_quantity_over_stock_warning_xpath)

    def retrieve_empty_shopping_cart_warning(self):
        return self.retrieve_element_text("empty_shopping_cart_warning_xpath",self.empty_shopping_cart_warning_xpath)

    def retrieve_quantity(self): # get a list of quantity for single product
        quantity_elemet = self.get_elements("quantity_input_box_xpath",self.quantity_input_box_xpath)
        quantity_list = [int(i.get_attribute('value')) for i in quantity_elemet]
        return quantity_list

    def retrieve_unit_price(self):# get a list of unit price for single product
        price_element = self.retrieve_elements_text("unit_price_xpath",self.unit_price_xpath)
        price_list = [i.replace("$", "").replace(",", "") for i in price_element]
        return price_list

    def retrieve_single_total_price(self):# get a list of total price for single product
        total_price_elemet= self.retrieve_elements_text("sigle_total_price_xpath",self.sigle_total_price_xpath)
        total_price_list = [i.replace("$", "").replace(",", "") for i in total_price_elemet]
        total_price_list = [round(float(i),2) for i in total_price_list]
        return total_price_list

    def retrieve_total_price(self):
        total_price = self.retrieve_element_text("total_price_xpath",self.total_price_xpath).replace("$", "").replace(",", "")
        return (round(float(total_price),2))


