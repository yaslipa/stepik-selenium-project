from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Page url is not login url'

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), 'Login form is not presented on Login page'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), 'Register form is not presented on Login page'

    def register_new_user(self, email, password):
        self.should_be_login_page()
        self.browser.find_element(
            *LoginPageLocators.REGISTER_DATA[0]).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.REGISTER_DATA[1]).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTER_DATA[2]).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTER_DATA[3]).click()
