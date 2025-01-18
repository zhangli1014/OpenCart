from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage

class AccountPage(BasePage):
    logout_option_link_text = "Logout"
    def __init__(self,driver):
        super().__init__(driver)

    edit_your_account_information_option_link_text = "Edit your account information"

    def display_status_of_edit_your_account_information_option(self):
        return self.check_display_status_of_element("edit_your_account_information_option_link_text",
                                                    self.edit_your_account_information_option_link_text)

    def logout_click(self):
        logout_option = self.element_action_click("logout_option_link_text",self.logout_option_link_text)



