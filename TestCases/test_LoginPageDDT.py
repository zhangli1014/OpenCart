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
from utilities import ExcelUtility
from utilities.readconfig import readConfig
from utilities.s3_reader import *
@pytest.mark.usefixtures("setup_teardown")
class TestLogin:
    logger = LogGen.loggen()

    @pytest.mark.pc
    def test_login_ddt(self):
        self.path = ".//TestData//LoginInfo.xlsx"

        self.rows = ExcelUtility.getRowCount(self.path,'LoginInfo')
        self.columns = ExcelUtility.getColumnCount(self.path,'LoginInfo')

        homepage = HomePage(self.driver)  # return driver after invoke fixtures in conftest.py
        time.sleep(2)


        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying login page ddt***********')
        test_status = [] # record the test results
        for i in range(2,self.rows+1):
            self.email = ExcelUtility.readData(self.path,'LoginInfo',i,1)
            self.password = ExcelUtility.readData(self.path,'LoginInfo', i, 2)
            self.exp = ExcelUtility.readData(self.path,'LoginInfo', i, 3)
            self.alertinfo = ExcelUtility.readData(self.path,'LoginInfo', i, 4)
            homepage.click_on_my_account_drop_menu()
            homepage.select_login_option()
            loginpage = LoginPage(self.driver)
            loginpage.enter_email_address(self.email)
            loginpage.enter_password(self.password)
            loginpage.click_on_login_button()
            time.sleep(2)

            if self.exp=='Pass':
                accountpage = AccountPage(self.driver)
                if accountpage.display_status_of_edit_your_account_information_option():
                    self.logger.info("*******use correct username and password ddt test login page  passed********")
                    test_status.append('Pass')
                    accountpage.logout_click()
                else:
                    self.logger.info("*******use correct username and password ddt test login page  failed********")
                    test_status.append('Fail')
            elif self.exp == 'Fail':
                expected_warning_message = 'Warning: No match for E-Mail Address and/or Password.'
                if loginpage.retrieve_warning_message() == expected_warning_message:
                    self.logger.info("*******use invalid username or invalid pass test login page passed********")
                    test_status.append('Pass')
                else:
                    self.logger.info("*******use invalid username test login page failed********")
                    test_status.append('Fail')

        if 'Fail' not in test_status:
            self.logger.info('************Login DDT Test Passed***********')
            assert True
        else:
            self.logger.info('************Login DDT Test Fail***********')
            assert False

    @pytest.mark.ec2
    def test_login_ddt(self):
        self.bucket_name = readConfig('s3 info', 'bucketName')
        self.file_key = readConfig('s3 info', 'fileKey')
        self.workbook = get_data_s3(self.bucket_name,self.file_key)
        self.rows = getRowCount_froms3(self.workbook,'LoginInfo')
        self.columns = getColumnCount_froms3(self.workbook, 'LoginInfo')

        homepage = HomePage(self.driver)  # return driver after invoke fixtures in conftest.py
        time.sleep(2)

        self.logger.info('*****************Start*********************')
        self.logger.info('***********Verifying login page ddt***********')
        test_status = []  # record the test results
        for i in range(2, self.rows + 1):
            self.email = readData_froms3(self.workbook, 'LoginInfo', i, 1)
            self.password = readData_froms3(self.workbook,'LoginInfo', i, 2)
            self.exp = readData_froms3(self.workbook,'LoginInfo', i, 3)
            self.alertinfo = readData_froms3(self.workbook,'LoginInfo', i, 4)
            homepage.click_on_my_account_drop_menu()
            homepage.select_login_option()
            loginpage = LoginPage(self.driver)
            loginpage.enter_email_address(self.email)
            loginpage.enter_password(self.password)
            loginpage.click_on_login_button()
            time.sleep(2)

            if self.exp == 'Pass':
                accountpage = AccountPage(self.driver)
                if accountpage.display_status_of_edit_your_account_information_option():
                    self.logger.info("*******use correct username and password ddt test login page  passed********")
                    test_status.append('Pass')
                    accountpage.logout_click()
                else:
                    self.logger.info("*******use correct username and password ddt test login page  failed********")
                    test_status.append('Fail')
            elif self.exp == 'Fail':
                expected_warning_message = 'Warning: No match for E-Mail Address and/or Password.'
                if loginpage.retrieve_warning_message() == expected_warning_message:
                    self.logger.info("*******use invalid username or invalid pass test login page passed********")
                    test_status.append('Pass')
                else:
                    self.logger.info("*******use invalid username test login page failed********")
                    test_status.append('Fail')

        if 'Fail' not in test_status:
            self.logger.info('************Login DDT Test Passed***********')
            assert True
        else:
            self.logger.info('************Login DDT Test Fail***********')
            assert False







