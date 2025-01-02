from pageObjects.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_field_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button_xpath = "//input[@name='newsletter'][@value='1']"
    duplicate_email_warning_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"
    password_confirm_warning_xpath = "//input[@id='input-confirm']/following-sibling::div"
    def enter_first_name(self, first_name_text):
        self.type_into_element("first_name_field_id", self.first_name_field_id,first_name_text)

    def enter_last_name(self, last_name_text):
        self.type_into_element( "last_name_field_id", self.last_name_field_id,last_name_text)

    def enter_email(self, email_text):
        self.type_into_element("email_field_id", self.email_field_id,email_text)

    def enter_telephone(self, telephone_text):
        self.type_into_element("telephone_field_id", self.telephone_field_id,telephone_text)

    def enter_password(self, password_text):
        self.type_into_element( "password_field_id", self.password_field_id,password_text)

    def enter_password_confirm(self, password_text):
        self.type_into_element("confirm_password_field_id", self.confirm_password_field_id,password_text)

    def select_agree_checkbox_field(self):
        self.element_click("agree_field_name", self.agree_field_name)

    def click_on_continue_button(self):
        self.element_click("continue_button_xpath", self.continue_button_xpath)

    def select_yes_radio_button(self):
        self.element_click("yes_radio_button_xpath", self.yes_radio_button_xpath)

    def retrieve_dupliacte_email_warning(self):
        return self.retrieve_element_text("duplicate_email_warning_xpath", self.duplicate_email_warning_xpath)

    def retrieve_privacy_policy_warning(self):
        return self.retrieve_element_text("privacy_policy_warning_xpath", self.privacy_policy_warning_xpath)

    def retrieve_first_name_warning(self):
        return self.retrieve_element_text("first_name_warning_xpath", self.first_name_warning_xpath)

    def retrieve_last_name_warning(self):
        return self.retrieve_element_text("last_name_warning_xpath", self.last_name_warning_xpath)

    def retrieve_email_warning(self):
        return self.retrieve_element_text("email_warning_xpath", self.email_warning_xpath)

    def retrieve_telephone_warning(self):
        return self.retrieve_element_text("telephone_warning_xpath", self.telephone_warning_xpath)

    def retrieve_password_warning(self):
        return self.retrieve_element_text("password_warning_xpath", self.password_warning_xpath)

    def retrieve_password_confirm_warning(self):
        return self.retrieve_element_text("password_confirm_warning_xpath", self.password_confirm_warning_xpath)
