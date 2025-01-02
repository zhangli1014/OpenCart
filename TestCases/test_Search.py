import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage
from utilities.CustomerLog import LogGen

@pytest.mark.usefixtures("setup_teardown")
class TestSearch:
    logger = LogGen.loggen()
    def test_search_for_a_valid_product(self):
        self.logger.info("*************** Start ****************")
        self.logger.info("********* Verifying search page *********")
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box("HP")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        if search_page.display_status_of_valid_product()==True:
            assert True
            self.logger.info("********* testing search page for a valid product succeed*********")
        else:
            assert False
            self.logger.info("********* testing search page for a valid product failed*********")
    def test_search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box("Honda")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        expected_text = "There is no product that matches the search criteria."
        if search_page.retrieve_no_product_message()==expected_text:
            assert True
            self.logger.info("********* testing search page for a invalid product succeed*********")
        else:
            assert False
            self.logger.info("********* testing search page for a invalid product failed*********")

    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box("")
        home_page.click_on_search_button()
        expected_text = "There is no product that matches the search criteria."

        search_page = SearchPage(self.driver)
        if search_page.retrieve_no_product_message()==expected_text:
            assert True
            self.logger.info("********* testing search page without entering any product succeed*********")
        else:
            assert False
            self.logger.info("********* testing search page without entering any product failed*********")
