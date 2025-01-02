import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from pageObjects.AccountPage import AccountPage
from pageObjects.RegisterPage import RegisterPage
from pageObjects.AccountSuccessPage import AccountSuccessPage
from utilities.CustomerLog import LogGen
from utilities.readconfig import readConfig
from utilities.ExcelUtility import writeData
import pytest
import time

def generate_name_random():
    randomstring =  ''.join(random.choices(string.ascii_lowercase+string.digits,k=7))
    while randomstring[0] in string.digits:
        randomstring = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
    return randomstring

@pytest.mark.usefixtures("setup_teardown")
class TestRegister:
    logger = LogGen.loggen()
    first_name = generate_name_random()
    laste_name = generate_name_random()
    email = first_name+'@test.com'

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        time.sleep(1)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying register page ***********')
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name(self.first_name)
        register_page.enter_last_name(self.laste_name)
        register_page.enter_email(self.email)
        register_page.enter_telephone("123456")
        register_page.enter_password("123456")
        register_page.enter_password_confirm("123456")
        register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()

        expected_heading_text = "Your Account Has Been Created!"
        account_success_page = AccountSuccessPage(self.driver)
        if account_success_page.retrieve_account_creation_message()==expected_heading_text:
            accountpage = AccountPage(self.driver)
            self.logger.info("****************register success with mandatoryfields***********")
            assert True
            accountpage.logout_click()
        else:
            self.logger.info("****************register fail with mandatory fields***********")
            assert False


    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        time.sleep(1)
        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying register page ***********')
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name(generate_name_random())
        register_page.enter_last_name(generate_name_random())
        register_page.enter_email(self.email)
        register_page.enter_telephone("123456")
        register_page.enter_password("123456")
        register_page.enter_password_confirm("123456")
        register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()

        expected_warning_text = "Warning: E-Mail Address is already registered!"
        #account_success_page = AccountSuccessPage(self.driver)
        if register_page.retrieve_dupliacte_email_warning() == expected_warning_text:
            self.logger.info("****************testing register pass with duplicated email fields***********")
            assert True
        else:
            self.logger.info("****************testing register fail with duplicated email fields***********")
            assert False

    def test_register_with_differernt_pass(self):
        home_page = HomePage(self.driver)
        time.sleep(1)
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name(self.first_name)
        register_page.enter_last_name(self.laste_name)
        register_page.enter_email(self.email)
        register_page.enter_telephone("123456")
        register_page.enter_password("123456")
        register_page.enter_password_confirm("1234561")
        register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()

        expected_password_confirm_warning_message = "Password confirmation does not match password!"
        if register_page.retrieve_password_confirm_warning()==expected_password_confirm_warning_message:
            assert True
            self.logger.info("****************testing register pass with different pass***********")
        else:
            assert False
            self.logger.info("****************testing register fail with different pass***********")
    def test_without_entering_any_field(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("")

        register_page.enter_last_name("")
        register_page.enter_email("")
        register_page.enter_telephone("")
        register_page.enter_password("")
        register_page.enter_password_confirm("")
        #register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()

        time.sleep(3)
        expected_privacy_policy_warning_text = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieve_privacy_policy_warning()==expected_privacy_policy_warning_text

        expected_last_name_warning_message = "Last Name must be between 1 and 32 characters!"
        assert register_page.retrieve_last_name_warning()==expected_last_name_warning_message

        expected_first_name_warning_message = "First Name must be between 1 and 32 characters!"
        assert register_page.retrieve_first_name_warning()==expected_first_name_warning_message

        expected_email_warning_message = "E-Mail Address does not appear to be valid!"
        assert register_page.retrieve_email_warning()==expected_email_warning_message

        expected_telephone_warning_message = "Telephone must be between 3 and 32 characters!"
        assert register_page.retrieve_telephone_warning()==expected_telephone_warning_message

        expected_password_warning_message = "Password must be between 4 and 20 characters!"
        assert register_page.retrieve_password_warning()==expected_password_warning_message
        self.logger.info("****************testing register pass without_entering any field***********")



