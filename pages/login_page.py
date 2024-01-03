from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegisterPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FORM), "Register form is not presented"