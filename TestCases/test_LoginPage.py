import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from pageObjects.AccountPage import AccountPage
from utilities.CustomerLog import LogGen
from utilities.readconfig import readConfig
import pytest
import time

@pytest.mark.usefixtures("setup_teardown")
class TestLogin:
    logger = LogGen.loggen()

    def test_login_with_valid_credentials(self):
        homepage = HomePage(self.driver) # return driver after invoke fixtures in conftest.py
        time.sleep(3)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying login page ***********')
        homepage.click_on_my_account_drop_menu()
        homepage.select_login_option()

        loginpage = LoginPage(self.driver)
        loginpage.enter_email_address('abcd@example.com')
        loginpage.enter_password('123456')
        loginpage.click_on_login_button()
        time.sleep(2)
        accountpage = AccountPage(self.driver)

        if accountpage.display_status_of_edit_your_account_information_option():
            self.logger.info("*******use correct username and password login page test passed********")
            assert True
        else:
            self.logger.info("*******use correct username and password login page test failed********")
            assert False

    def test_login_with_invalid_email(self):
        homepage = HomePage(self.driver)  # return driver after invoke fixtures in conftest.py
        time.sleep(3)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying login page ***********')
        homepage.click_on_my_account_drop_menu()
        homepage.select_login_option()

        loginpage = LoginPage(self.driver)
        loginpage.enter_email_address(self.generate_email_with_random_string())
        loginpage.enter_password('123456')
        loginpage.click_on_login_button()
        time.sleep(2)
        expected_warning_message='Warning: No match for E-Mail Address and/or Password.'
        if loginpage.retrieve_warning_message()==expected_warning_message:
            self.logger.info("*******use invalid username test login page passed********")
            assert True
        else:
            self.logger.info("*******use invalid username test login page failed********")
            assert False

    def test_login_with_invalid_password(self):
        homepage = HomePage(self.driver)  # return driver after invoke fixtures in conftest.py
        time.sleep(3)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying login page ***********')
        homepage.click_on_my_account_drop_menu()
        homepage.select_login_option()

        loginpage = LoginPage(self.driver)
        loginpage.enter_email_address('abcd@example.com')
        loginpage.enter_password('1234')
        loginpage.click_on_login_button()
        time.sleep(2)
        expected_warning_message='Warning: No match for E-Mail Address and/or Password.'
        if loginpage.retrieve_warning_message()==expected_warning_message:
            self.logger.info("*******use invalid password test login page passed********")
            assert True
        else:
            self.logger.info("*******use invalid password test login page failed********")
            assert False



    def generate_email_with_random_string(self):
        randomstring =  ''.join(random.choices(string.ascii_lowercase,k=7))
        return randomstring+'@gmail.com'






