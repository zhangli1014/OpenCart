from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from pageObjects.AccountPage import AccountPage
from pageObjects.RegisterPage import RegisterPage
from pageObjects.AccountSuccessPage import AccountSuccessPage
from pageObjects.ShoppingCartButtonPage import ShoppingCartButtonPage
from pageObjects.ShoppingCartPage import ShoppingCartPage
from pageObjects.SearchPage import SearchPage
from pageObjects.MenuPage import MenuPage
from utilities.CustomerLog import LogGen
from utilities.readconfig import readConfig
from utilities.ExcelUtility import writeData
import pytest
import time

# the methods of adding product to cart include:
# 1 from home page
# 2 from search page
# 3 from menu
# 4 from wish list
@pytest.mark.usefixtures("setup_teardown_cart")
class TestShoppingCart:
    logger = LogGen.loggen()
    def test_empty_cart_click_cart_option(self):
        home_page = HomePage(self.driver)
        time.sleep(1)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying cart page ************')
        home_page.shopping_cart_option_click()
        shopping_cart_page = ShoppingCartPage(self.driver)
        expected_empty_warning_text = 'Your shopping cart is empty!'
        if shopping_cart_page.retrieve_empty_shopping_cart_warning() == expected_empty_warning_text:
            assert True
            self.logger.info("*****test click cart option when cart is empty Pass***")
        else:
            assert False
            self.logger.info("*****test click cart option when cart is empty Fail***")


    #failed
    def test_empty_cart_click_cart_button(self):
        home_page = HomePage(self.driver)
        time.sleep(1)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying cart page ************')
        home_page.shopping_cart_button_click()
        time.sleep(1)
        expected_empty_warning_text = 'Your shopping cart is empty!'

        if home_page.retrieve_shopping_cart_empty_button_click_warning()==expected_empty_warning_text:
            assert True
            self.logger.info("*****test click cart button when cart is empty Pass***")
        else:
            assert False
            self.logger.info("*****test click cart button when cart is empty Fail***")

    def test_add_product_to_cart_from_homepage(self):
        home_page = HomePage(self.driver)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying cart page ***********')
        home_page.add_mac_to_cart()
        time.sleep(1)
        expected_add_product_success_message = 'Success: You have added'
        if expected_add_product_success_message in home_page.retrieve_add_product_to_cart_success_message():
            assert True
            self.logger.info("*****test add mac to cart from homepage Pass***")
        else:
            assert False
            self.logger.info("*****test add mac to cart from homepage Fail***")
        # switch to cart page
        home_page.shopping_cart_option_click()

        if self.assert_price()==True:
            assert True
            self.logger.info("*****test the total price of cart after adding product from home page Pass***")
        else:
            assert False
            self.logger.info("*****test the total price of cart after adding product from home page Fail***")

    def test_add_product_to_cart_from_search(self):
        self.logger.info("*************** Start ****************")
        self.logger.info("********* Verifying cart page *********")
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box("iphone")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        search_page.add_product_to_cart_from_search()
        time.sleep(1)
        expected_add_product_success_message = 'Success: You have added'

        if expected_add_product_success_message in search_page.retrieve_add_product_to_cart_success_message():
            assert True
            self.logger.info("*****test add product to cart from search page Pass***")
        else:
            assert True
            self.logger.info("*****test add product to cart from search Fail***")
        # switch to cart page
        search_page.click_cart_link_after_add_product()
        if self.assert_price()==True:
            assert True
            self.logger.info("*****test the total price of cart after adding product from search page Pass***")
        else:
            assert False
            self.logger.info("*****test the total price of cart after adding product from search page Fail***")
    def test_add_product_to_cart_from_menu(self):
        self.logger.info("*************** Start ****************")
        self.logger.info("********* Verifying cart page *********")
        home_page = HomePage(self.driver)
        menu_page = MenuPage(self.driver)
        menu_page.navigate_to_category("Tablets")
        menu_page.add_product_from_category()
        time.sleep(1)
        expected_add_product_success_message = 'Success: You have added'

        if expected_add_product_success_message in menu_page.retrieve_add_product_to_cart_success_message():
            assert True
            self.logger.info("*****test add product to cart from menu Pass***")
        else:
            assert True
            self.logger.info("*****test add product to cart from menu Fail***")
        # switch to cart page
        menu_page.click_cart_link_after_add_product()

        if self.assert_price()==True:
            assert True
            self.logger.info("*****test the total price of cart after adding product from menu page Pass***")
        else:
            assert False
            self.logger.info("*****test the total price of cart after adding product from menu page Fail***")

    def test_add_products_to_cart(self):
        home_page = HomePage(self.driver)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying add mutiple products to cart  ***********')
        home_page.add_mac_to_cart()
        time.sleep(1)
        #switch to search page
        home_page.enter_product_into_search_box("iphone")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        search_page.add_product_to_cart_from_search()
        #switch to homepage
        search_page.click_homepage_link()
        #switch to menu page
        menu_page = MenuPage(self.driver)
        menu_page.navigate_to_category("Tablets")
        menu_page.add_product_from_category()
        time.sleep(1)
        menu_page.click_cart_link_after_add_product()

        if self.assert_price() == True:
            assert True
            self.logger.info("*****test the total price of cart after adding mutiple products  Pass***")
        else:
            assert False
            self.logger.info("*****test the total price of cart after adding mutiple products  Fail***")

    def test_modify_quantity_cart_zero(self):
        #first add product to cart
        home_page = HomePage(self.driver)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying cart page ***********')
        home_page.add_mac_to_cart()
        home_page.add_mac_to_cart()
        time.sleep(1)
        home_page.click_cart_link_after_add_product()
        cart_page = ShoppingCartPage(self.driver)
        min = 0
        cart_page.enter_quantity_input_box_all(min)
        cart_page.click_quantity_update_all()
        #verify
        time.sleep(1)
        expected_empty_warning_text = 'Your shopping cart is empty!'

        if expected_empty_warning_text==cart_page.retrieve_empty_shopping_cart_warning():
            assert True
            self.logger.info('***********modify the quantity in cart 0 pass***********')
        else:
            assert False
            self.logger.info('***********modify the quantity in cart 0 fail***********')

    def test_modify_quantity_cart_min(self):
        #first add product to cart
        home_page = HomePage(self.driver)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying cart page ***********')
        home_page.add_mac_to_cart()
        home_page.add_mac_to_cart()
        time.sleep(1)
        home_page.click_cart_link_after_add_product()
        cart_page = ShoppingCartPage(self.driver)
        min = 1
        cart_page.enter_quantity_input_box_all(min)
        cart_page.click_quantity_update_all()
        #verify
        time.sleep(1)
        quantity_actual = cart_page.retrieve_quantity()
        expected_actual = [min]

        if quantity_actual==expected_actual:
            assert True
            self.logger.info('***********modify the quantity to 1 in cart pass***********')
        else:
            assert False
            self.logger.info('***********modify the quantity to 1 in cart  fail***********')

        if self.assert_price() == True:
            assert True
            self.logger.info("*****test the total price of cart after modifying quantity to 1 Pass***")
        else:
            assert False
            self.logger.info("*****test the total price of cart after modifying quantity to 1  Fail***")

    def test_modify_quantity_cart_max_stock(self):
        home_page = HomePage(self.driver)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying cart page ***********')
        home_page.add_mac_to_cart()
        time.sleep(1)
        home_page.click_cart_link_after_add_product()
        cart_page = ShoppingCartPage(self.driver)
        max = 929
        cart_page.enter_quantity_input_box_all(max)
        cart_page.click_quantity_update_all()
        # verify
        time.sleep(1)
        quantity_actual = cart_page.retrieve_quantity()
        expected_actual = [max]
        if quantity_actual==expected_actual:
            assert True
            self.logger.info('***********modify the quantity in cart 929 pass***********')
        else:
            assert False
            self.logger.info('***********modify the quantity in cart 929 fail***********')
        if self.assert_price() == True:
            assert True
            self.logger.info("*****test the total price of cart after modifying quantity to 929 Pass***")
        else:
            assert False
            self.logger.info("*****test the total price of cart after modifying quantity to 929  Fail***")

    def test_modify_quantity_cart_over_max_stock(self):
        home_page = HomePage(self.driver)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying cart page ***********')
        home_page.add_mac_to_cart()
        time.sleep(1)
        home_page.click_cart_link_after_add_product()
        cart_page = ShoppingCartPage(self.driver)
        max = 930
        cart_page.enter_quantity_input_box_all(max)
        cart_page.click_quantity_update_all()
        # verify
        time.sleep(1)
        over_stock_expected_message = 'are not available in the desired quantity or not in stock'
        if over_stock_expected_message in cart_page.retrieve_over_shopping_cart_quantity_warning():
            assert True
            self.logger.info('***********modify the quantity in cart over stock pass***********')
        else:
            assert False
            self.logger.info('***********modify the quantity in cart over stock fail***********')
            

    def test_remove_one_product_cart(self):
        home_page = HomePage(self.driver)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying add mutiple products to cart  ***********')
        home_page.add_mac_to_cart()
        time.sleep(1)
        # switch to search page
        home_page.enter_product_into_search_box("iphone")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        search_page.add_product_to_cart_from_search()
        # switch to homepage
        search_page.click_homepage_link()
        # switch to menu page
        menu_page = MenuPage(self.driver)
        menu_page.navigate_to_category("Tablets")
        menu_page.add_product_from_category()
        time.sleep(1)
        menu_page.click_cart_link_after_add_product()

        cart_page = ShoppingCartPage(self.driver)
        cart_page.click_quantity_remove_one()
        time.sleep(1)
        if self.assert_price() == True:
            assert True
            self.logger.info("*****test the total price of cart after removing one product  Pass***")
        else:
            assert False
            self.logger.info("*****test the total price of cart after removing one product  Fail***")

    def test_remove_all_products_cart(self):
        home_page = HomePage(self.driver)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying add mutiple products to cart  ***********')
        home_page.add_mac_to_cart()
        time.sleep(1)
        # switch to search page
        home_page.enter_product_into_search_box("iphone")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        search_page.add_product_to_cart_from_search()
        # switch to homepage
        search_page.click_homepage_link()
        # switch to menu page
        menu_page = MenuPage(self.driver)
        menu_page.navigate_to_category("Tablets")
        menu_page.add_product_from_category()
        time.sleep(1)
        menu_page.click_cart_link_after_add_product()

        cart_page = ShoppingCartPage(self.driver)
        cart_page.click_quantity_remove_all()
        time.sleep(1)
        expected_empty_warning_text = 'Your shopping cart is empty!'

        if expected_empty_warning_text==cart_page.retrieve_empty_shopping_cart_warning():
            assert True
            self.logger.info('***********modify the quantity in cart 0 pass***********')
        else:
            assert False
            self.logger.info('***********modify the quantity in cart 0 fail***********')


    def assert_price(self):
        cart_page = ShoppingCartPage(self.driver)
        products_quantity = cart_page.retrieve_quantity()
        products_unit_price = cart_page.retrieve_unit_price()
        signal_product_total_price = cart_page.retrieve_single_total_price()
        total_price = cart_page.retrieve_total_price()
        expected_signal_product_total_price = []

        for i,j in zip(products_quantity,products_unit_price):
            expected_signal_product_total_price.append(round(float(i)*float(j),2))
        expected_total_price = round(sum(expected_signal_product_total_price),2)

        if expected_signal_product_total_price == signal_product_total_price and total_price == expected_total_price:
            return True
        else:
            return False




